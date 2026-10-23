"""Bounded numerical discovery of a coordinate slice cover; no acceptance."""
import argparse
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_array

ROOT = Path(__file__).resolve().parents[3]


def run(component, seconds, extra_c2=False):
    data = json.loads((ROOT/'results/sl2-finite-slices-2026-10-21/lift-pilot.json').read_text())
    labels = list(range(88)) if component == 'principal' else list(range(88, 120))
    terms = [row[:3] for row in data['support'] if row[0] in set(labels)]
    if extra_c2:
        labels = [2*a+d for a in labels for d in range(2)]
        central = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0))
        terms = [[2*a+d for a, d in zip(term, digits)] for term in terms for digits in central]
    lookup = {a: i for i, a in enumerate(labels)}
    rows, cols = [], []
    for i, term in enumerate(terms):
        for leg, a in enumerate(term):
            rows.append(i)
            cols.append(leg*len(labels)+lookup[a])
    A = coo_array((np.ones(len(rows)), (np.array(rows), np.array(cols))),
                  shape=(len(terms), 3*len(labels))).tocsc()
    started = time.monotonic()
    result = milp(np.ones(A.shape[1]), integrality=np.ones(A.shape[1]),
                  bounds=Bounds(0, 1), constraints=LinearConstraint(A, 1, np.inf),
                  options={'time_limit': seconds, 'mip_rel_gap': 0})
    selected = None
    if result.x is not None:
        selected = [[a for i, a in enumerate(labels) if result.x[leg*len(labels)+i] > .5]
                    for leg in range(3)]
        if any(all(a not in selected[leg] for leg, a in enumerate(term)) for term in terms):
            raise ArithmeticError('rounded discovery cover leaves a support term')
    return {'status': 'bounded-discovery-only', 'component': component, 'extra_C2': extra_c2,
            'seconds_limit': seconds, 'elapsed_seconds': time.monotonic()-started,
            'solver_status': int(result.status), 'solver_message': result.message,
            'objective_float': None if result.fun is None else float(result.fun),
            'dual_bound_float': float(result.mip_dual_bound),
            'selected_coordinates': selected,
            'integer_cover_size': None if selected is None else sum(map(len, selected)),
            'exclusion_established': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--component', choices=('principal', 'matrix'), required=True)
    parser.add_argument('--seconds', type=float, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--extra-c2', action='store_true')
    args = parser.parse_args()
    report = run(args.component, args.seconds, args.extra_c2)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))
