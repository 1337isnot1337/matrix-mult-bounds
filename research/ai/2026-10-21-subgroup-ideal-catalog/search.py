"""Bounded split-cover M10 discovery with the complete certified coset cuts."""
import argparse
import hashlib
import json
from pathlib import Path

from subgroup_catalog import ideal, read
from verify_catalog import split_search_record


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--control', action='store_true')
    parser.add_argument('--reuse-report', action='append', type=Path, default=[])
    args = parser.parse_args()
    path = ideal.ROOT/'results/subgroup-ideal-catalog-2026-10-21/catalog.json.gz'
    G = ideal.sources()[1]
    record, receipt = split_search_record(G, read(path)['records'][1])
    # Optional discovery dependencies are kept out of certificate replay.
    from lazy_parity import run
    result = run(args.output, args.seconds, control=args.control,
                 reuse=args.reuse_report, full_capacity=True, split_cover=True,
                 ideal_record=record)
    result['verified_subgroup_catalog'] = receipt
    result['catalog_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    result['common_ideal_dimension_upper_bound'] = record['ideal_dimension']
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('source_and_normalization', 'witness',
                                   'verified_subgroup_catalog', 'sat_statistics')}))
