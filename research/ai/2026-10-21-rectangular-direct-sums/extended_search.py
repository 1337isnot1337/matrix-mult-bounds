"""Continue the finite search, certifying each additional Hankel-space cap."""
import argparse
import importlib.util
import json
import hashlib
from math import isqrt
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent

def module(name):
 spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
 result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
 return result

screen=module('screen');sat=module('saturation');boundary=module('second_boundary');blockdim=module('block_hankel_dimension');bundle=module('bundle_hankel_dimension')

def saturation_witness(a,b,target):
 ab=a*b;N=ab*(a+b-1);r=a-1;k=isqrt(2*r+1);D=target['leg_dimensions']
 assert 2*r<k*(k+2)
 for j,s in enumerate(target['shapes']):
  for i,(d,p) in enumerate(zip(screen.legs(s),screen.slice_minima(s))):
   lift=k*p+2*N-sum(D)+D[i]
   if d>r*ab and lift<(r+1)*ab:
    return {'block':j,'leg':i,'input_rank_cap':k,'lift_upper':lift,
            'next_symbol_threshold':(r+1)*ab,'parameter_dimension':d,
            'symbol_injection_cap':r*ab}
 return None

def digest(rows):
 return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def refine(a,b,survivors):
 excluded=[];remaining=[];counts={'saturation':0,'second_boundary':0,'crossed_dimension':0,'bundle_dimension':0}
 for row in survivors:
  w=saturation_witness(a,b,row)
  method='saturation'
  if w is None:
   w=boundary.exclusion(a,b,row['shapes'],row['leg_dimensions'])
   method='second_boundary'
  if w is None:
   w=blockdim.exclusion(a,b,row['shapes'],row['leg_dimensions'])
   method='crossed_dimension'
  if w is None:
   w=bundle.exclusion(a,b,row['shapes'],row['leg_dimensions'])
   method='bundle_dimension'
  if w is None:remaining.append(row)
  else:
   counts[method]+=1
   excluded.append({'shapes':row['shapes'],'method':method,'witness':w})
 return excluded,remaining,counts

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--maximum',type=int,default=1500)
 parser.add_argument('--directory',type=Path,required=True);args=parser.parse_args()
 args.directory.mkdir(parents=True,exist_ok=True);formats=[]
 for a in range(2,isqrt(args.maximum)+1):
  for b in range(a,args.maximum+1):
   N=a*b*(a+b-1)
   if N>args.maximum:break
   if N>960:formats.append((N,a,b))
 start=time.monotonic();results=[]
 for N,a,b in sorted(formats):
  rec=screen.screen_source(a,b)
  survivors=rec['surviving_targets'];excluded=[];remaining=[]
  if survivors:
   cert=sat.generate(a,b);summary=sat.verify(cert)
   (args.directory/f'hankel-a{a}-b{b}.json').write_text(json.dumps(cert,separators=(',',':'))+'\n')
  excluded,remaining,counts=refine(a,b,survivors)
  if not survivors:summary=None
  out={'a':a,'b':b,'source_leg_dimension':N,'initial_counts':rec['counts'],
       'hankel_certificate_summary':summary,'excluded_counts':counts,
       'remaining_count':len(remaining),'excluded_sha256':digest(excluded),
       'remaining_sha256':digest(remaining),'remaining_first_20':remaining[:20],
       'scope':'Necessary tests only; no maps constructed; proofs unreviewed.'}
  results.append(out)
  (args.directory/'extended-frontier.json').write_text(json.dumps(results,indent=2)+'\n')
  print(a,b,N,len(survivors),len(remaining),round(time.monotonic()-start,2),flush=True)
 print('DONE',len(results),flush=True)
