"""Joint-sign S5 x C2 search with actual index-five normalization."""
import argparse
import json
from pathlib import Path

from s5_source import data, ROOT
from lazy_parity import run


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--control', action='store_true')
    parser.add_argument('--canonical', action='store_true')
    args = parser.parse_args()
    normalize = None
    known = ROOT/'results/s5-split-2026-10-21/control3.json'
    if args.canonical:
        from symmetry import append, canonical_control
        normalize = append
        if args.control:
            known = ROOT/'results/s5-split-2026-10-21/canonical-control3.json'
            known.write_text(json.dumps(canonical_control(), indent=2)+'\n')
    report = run(args.output, args.seconds, control=args.control, full_capacity=True,
                 data_provider=data, target_shape=(13, 14, 14),
                 known_control=known, normalizer=normalize)
    print(json.dumps({k: v for k, v in report.items()
                      if k not in ('source_and_normalization', 'witness')}))
