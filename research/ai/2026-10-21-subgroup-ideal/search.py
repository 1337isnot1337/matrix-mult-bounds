"""Split-cover construction search with exactly verified subgroup-ideal cuts."""
import argparse
import hashlib
import json
from pathlib import Path

from ideal import sources, verify, ROOT
from lazy_parity import run


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--control', action='store_true')
    parser.add_argument('--reuse-report', action='append', type=Path, default=[])
    args = parser.parse_args()
    path = ROOT/'results/subgroup-ideal-2026-10-21/certificates.json'
    records = json.loads(path.read_text())['records']
    G = sources()[1]
    record = next(row for row in records if row['group'] == G['name'])
    receipt = verify(G, record)
    result = run(args.output, args.seconds, control=args.control, reuse=args.reuse_report,
                 full_capacity=True, split_cover=True, ideal_record=record)
    result['verified_ideal'] = receipt
    result['ideal_certificate_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('source_and_normalization', 'witness')}))
