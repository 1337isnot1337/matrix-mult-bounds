"""Apply the written critical-state obstruction to historical frontier records."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
FOLDER=ROOT/'results/rectangular-direct-sums-20261021'

def witness(shapes):
 dims=[sum(s[i]*s[(i+1)%3] for s in shapes) for i in range(3)]
 for block,s in enumerate(shapes):
  for leg in range(3):
   p,q,w=s[leg],s[(leg+1)%3],s[(leg+2)%3]
   lift=2*w+2720-sum(dims[j] for j in range(3) if j!=leg)
   outer=[max(2*(m+n-2),min(m,p)*min(n,q),min(m,q)*min(n,p))
          for m,n in [(136,10),(170,8)]]
   if min(p,q)>=2 and p*q>960 and 2*(p+q-2)>122 and max(outer)<p*q and lift<=641:
    return {'block':block,'leg':leg,'parameter_shape':[p,q],
            'rank_two_lift':lift,'rank_two_dimension':2*(p+q-2),
            'outer_compression_dimension_bounds':outer,'total_leg_dimensions':dims}
 return None

def report():
 path=FOLDER/'ruling-refined-two-sums.json';raw=path.read_bytes();old=json.loads(raw)
 formats=[]
 for row in old['formats']:
  excluded=[];kept=[]
  for shapes in row['remaining_shapes']:
   w=witness(shapes) if (row['a'],row['b'])==(8,10) else None
   if w:excluded.append({'shapes':shapes,'witness':w})
   else:kept.append(shapes)
  formats.append({'a':row['a'],'b':row['b'],'predecessor_count':len(row['remaining_shapes']),
                  'excluded_count':len(excluded),'excluded':excluded,
                  'remaining_count':len(kept),'remaining_shapes':kept})
 single=json.loads((FOLDER/'single-frontier-1500.json').read_text())
 survivors=[(r['a'],r['b'],v['shape']) for r in single['sources'] for v in r['records'] if v['gate']=='survives necessary tests']
 assert survivors==[(8,10,[32,33,33])]
 return {'status':'finite applications of written unreviewed critical-state proof',
         'predecessor_sha256':hashlib.sha256(raw).hexdigest(),
         'single_target_disposition':{'source':[8,10],'shape':[32,33,33],
              'witness':witness([[32,33,33]]),'ordinary_single_survivors_through1500':0},
         'two_block_new_exclusions':sum(r['excluded_count'] for r in formats),
         'two_block_remaining':sum(r['remaining_count'] for r in formats),
         'formats':formats,'improves_omega':False,'independent_review':False}
if __name__=='__main__':print(json.dumps(report(),indent=2))
