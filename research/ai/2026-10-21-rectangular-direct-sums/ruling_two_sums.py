"""Apply the new ruling gate to hash-verified prior two-summand survivors."""
from pathlib import Path
from math import prod
from collections import Counter
import argparse,json,importlib.util
P=Path(__file__).with_name('extended_search.py');spec=importlib.util.spec_from_file_location('ruling_two_sums_import',P);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e);t=e.module('two_ruling_cap');ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/'results/rectangular-direct-sums-20261021'
def reconstruct(a,b,shapes):
 intervals=[e.screen.score_interval(prod(s)) for s in shapes];lo=sum(x[0] for x in intervals);hi=sum(x[1] for x in intervals);return {'shapes':shapes,'leg_dimensions':[sum(x) for x in zip(*(e.screen.legs(s) for s in shapes))],'score_interval_numerators':[lo,hi],'strict_score_gain_certified':lo>(3*(a+b)-2)**3*e.screen.SCALE}
def check_manifest(data,previous):
 a,b=data['a'],data['b'];rows=[reconstruct(a,b,s) for s in data['shapes']];assert len(rows)==previous['remaining_count'];assert e.digest(rows)==data['predecessor_sha256']==previous['remaining_sha256'];return rows
def report():
 previous=json.loads((RESULT/'extended-frontier.json').read_text());out=[]
 for a,b in [(8,9),(8,10),(9,9)]:
  old=next(r for r in previous if (r['a'],r['b'])==(a,b));data=json.loads((RESULT/f'two-sum-ruling-input-a{a}-b{b}.json').read_text());rows=check_manifest(data,old);kept=[];excluded=[];counts=Counter()
  for row in rows:
   w=t.exclusion(a,b,row['shapes'],row['leg_dimensions'])
   if w:excluded.append({'shapes':row['shapes'],'witness':w});counts[str(w['input_rank_cap'])]+=1
   else:kept.append(row)
  out.append({'a':a,'b':b,'source_leg_dimension':a*b*(a+b-1),'predecessor_count':len(rows),'predecessor_sha256':e.digest(rows),'excluded_count':len(excluded),'excluded_sha256':e.digest(excluded),'exclusion_counts_by_parameter_rank':dict(counts),'remaining_count':len(kept),'remaining_sha256':e.digest(kept),'remaining_shapes':[r['shapes'] for r in kept]})
 return {'status':'finite necessary tests; written general proofs remain unreviewed; no maps or exponent gain','source_range':'the previously exhaustive two-positive-summand scan through source dimension1500','predecessor_survivors':sum(r['predecessor_count'] for r in out),'new_exclusions':sum(r['excluded_count'] for r in out),'remaining':sum(r['remaining_count'] for r in out),'formats':out}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=report();a.output.write_text(json.dumps(r,separators=(',',':'))+'\n');print(json.dumps({k:v for k,v in r.items() if k!='formats'},indent=2));print([(r['a'],r['b'],r['remaining_count']) for r in r['formats']])
