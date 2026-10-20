"""Bounded discovery on the exact surviving affine frontier, with checkpoints.

Skipping an already attempted case is search scheduling, never an exclusion.
The program stops at a witness so the full exponent bridge can be reviewed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import time

from search import run


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frontier',type=Path,required=True)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--partition',type=int,default=0)
    parser.add_argument('--partitions',type=int,default=3)
    parser.add_argument('--seconds',type=float,default=30)
    parser.add_argument('--max-cases',type=int,default=12)
    args=parser.parse_args()
    if not 0<=args.partition<args.partitions or args.seconds<=0 or args.max_cases<1:
        parser.error('invalid partition or limits')
    data=json.loads(args.frontier.read_text())
    attempted=set()
    for path in args.directory.glob('*.json'):
        try:r=json.loads(path.read_text())
        except (ValueError,OSError):continue
        affine=r.get('affine_parameters')
        if not affine or r.get('status')=='running':continue
        complete_negative=str(r.get('status','')).startswith('solver-reported-unsatisfiable')
        tables=r.get('encoding',{}).get('coset_normalization') or {}
        same_table_timeout=r.get('status')=='time-limit' and tables.get('complete_normal_table_cases',0)>0
        if complete_negative or same_table_timeout:
            attempted.add((*affine,*r['shape']))
    survivors=[r for r in data['survivors'] if (r['prime'],r['index'],*r['shape']) not in attempted]
    assigned=[r for i,r in enumerate(data['survivors']) if i%args.partitions==args.partition
              and (r['prime'],r['index'],*r['shape']) not in attempted]
    manifest={'partition':args.partition,'partitions':args.partitions,
        'frontier_sha256':hashlib.sha256(args.frontier.read_bytes()).hexdigest(),
        'seconds_per_case':args.seconds,'max_cases':args.max_cases,
        'source_frontier_count':len(data['survivors']),
        'skipped_already_attempted_cases':len(data['survivors'])-len(survivors),
        'assigned_cases':len(assigned),'completed':[], 'status':'running',
        'scope':'Discovery scheduling only. No skipped, timed-out or untraced '
                'UNSAT case is promoted to a nonexistence theorem.'}
    target=args.directory/f'campaign-partition-{args.partition}.json'
    args.directory.mkdir(parents=True,exist_ok=True)
    def save():
        tmp=target.with_suffix('.tmp');tmp.write_text(json.dumps(manifest,indent=2)+'\n');tmp.replace(target)
    save()
    for row in assigned[:args.max_cases]:
        p,r=row['prime'],row['index'];shape=row['shape']
        name=f'affine-{p}-{r}-shape'+('-'.join(map(str,shape)))+f'-campaign{args.partition}.json'
        result=run(shape,args.seconds,20261100+p*100+r,args.directory/name,2000,
                   [p,r],'cadical195')
        manifest['completed'].append({'path':name,'group':result['group'],'shape':shape,
             'status':result['status'],'pair_injective_models':result['pair_injective_models'],
             'exact_farkas_cuts':result['exact_farkas_cuts']})
        if result['witness']:
            manifest['status']='exact witness found; exponent bridge pending';save();return
        save()
    manifest['status']='assigned bounded batch finished; no witness';save()


if __name__=='__main__':main()
