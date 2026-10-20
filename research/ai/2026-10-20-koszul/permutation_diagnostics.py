"""Replay full-tensor diagnostics for saved floating permutation probes."""
import argparse
import importlib.util
import json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    'fatpoint_probe_target', ROOT/'research/ai/2026-10-20-concavity-equivalence/fatpoint_route.py')
target_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target_module)


def diagnose(folder):
    dims, terms = target_module.tensor(4)
    desired = np.zeros(dims)
    for i,y,z in terms:
        desired[i,z,y] = 1
    degrees = np.array([d for d in range(4) for _ in range(d+1)])
    exponents = np.array([i for d in range(4) for i in range(d+1)])
    weight = (5*(degrees[None,:,None]+degrees[None,None,:]-3)
              + 2*(np.arange(4)[:,None,None]-exponents[None,:,None]-exponents[None,None,:]))
    records = []
    for path in sorted(folder.glob('*.npz')):
        with np.load(path) as data:
            p,q,g = [data[key] for key in ('P','Q','G')]
        raw = np.einsum('ih,hzy->izy',g,np.stack([q[:,h:h+10]@p for h in range(4)]))
        best = min((float(np.linalg.norm(raw*eps**weight-desired)/np.linalg.norm(desired)),float(eps))
                   for eps in np.geomspace(.05,1,300))
        records.append({'permutation':path.stem,'best_relative_full_tensor_error':best[0],
                        'epsilon':best[1],'epsilon_samples':300,'interval':[.05,1.0]})
    return records


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    args = parser.parse_args()
    print(json.dumps(diagnose(args.folder),indent=2))
