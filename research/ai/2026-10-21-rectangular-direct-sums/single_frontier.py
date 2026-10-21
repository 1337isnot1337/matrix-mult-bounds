"""Exhaust ordinary single matrix targets through source leg dimension1152."""
from pathlib import Path
from math import prod,isqrt
from collections import Counter
import argparse,json
import importlib.util
P=Path(__file__).with_name('extended_search.py');spec=importlib.util.spec_from_file_location('single_frontier_import',P);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
ROOT=Path(__file__).resolve().parents[3]
def report(maximum=1152):
 sources=[];totals=Counter();cap_sources=set()
 for a in range(2,isqrt(maximum)+1):
  for b in range(a,maximum+1):
   N=a*b*(a+b-1)
   if N>maximum:break
   records=[]
   for shape in e.screen.sorted_shapes(N):
    if 216*prod(shape)<=(3*(a+b)-2)**4:continue
    reason=e.screen.rejection(a,b,[shape]);record={'shape':list(shape)}
    if reason is not None:record.update(gate='baseline',reason=reason)
    else:
     row={'shapes':[shape],'leg_dimensions':list(e.screen.legs(shape))};excluded,remaining,counts=e.refine(a,b,[row])
     if excluded:
      record.update(gate=excluded[0]['method'],witness=excluded[0]['witness'])
      if record['gate']=='saturation':cap_sources.add((a,b))
     else:record['gate']='survives necessary tests'
    totals[record['gate']]+=1;records.append(record)
   sources.append({'a':a,'b':b,'source_leg_dimension':N,'score_eligible_shapes':len(records),'records':records})
 return {'status':'finite application of written unreviewed necessary-condition proofs; no construction or exponent improvement','maximum_source_leg_dimension':maximum,'source_format_count':len(sources),'score_eligible_shape_count':sum(totals.values()),'gate_counts':dict(totals),'hankel_cap_sources':[list(v) for v in sorted(cap_sources)],'sources':sources}
def verify_caps():
 folder=ROOT/'results/rectangular-direct-sums-20261021';records=json.loads((folder/'hankel-coordinate-certificates.json').read_text());records.append(json.loads((folder/'hankel-a8-b9.json').read_text()));assert {(r['a'],r['b']) for r in records}=={(7,9),(8,8),(8,9)}
 return [e.sat.verify(r) for r in records]
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--verify-caps',action='store_true');a=p.parse_args();r=report()
 if a.verify_caps:print('CAP CONTROLS',verify_caps(),flush=True)
 a.output.write_text(json.dumps(r,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in r.items() if k!='sources'},indent=2))
