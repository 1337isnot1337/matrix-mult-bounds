import json
from math import lcm
from fractions import Fraction
from pathlib import Path
import z3

root=Path('/home/cinna/matrix-mult-schur-20261020')
w=json.loads((root/'results/mixed-restrictions-2026-10-20/collision-m3-control.json').read_text())['witness']
m=w['m'];pts=[(a,d-a) for d in range(m) for a in range(d+1)];xp=w['source_x_indices'];yp=w['source_y_indices']
wx=[z3.Real(f'wx{p}') for p in range(m)];wy=[z3.Real(f'wy{i}') for i in range(len(pts))]
nu={k:z3.Real(f'nu{k}') for row in w['output_source_indices'] for k in row}
s=z3.Solver();s.add(wx[0]==0,wx[1]==0,wx[2]==1)
for p in range(m):
 for y,(a,b) in enumerate(pts):
  k=xp[p]+yp[y]
  for z,(c,d) in enumerate(pts):
   if k not in w['output_source_indices'][z]:continue
   total=wx[p]+wy[y]+nu[k]
   wanted=p==a+c and a+b+c+d==m-1
   s.add(total==0 if wanted else total>0)
result=s.check();print(result)
if result==z3.sat:
 model=s.model()
 def get(value):
  value=model.eval(value,model_completion=True)
  return Fraction(value.numerator_as_long(),value.denominator_as_long())
 values=[get(v) for v in wx+wy+list(nu.values())];scale=lcm(*(v.denominator for v in values))
 report={'m':m,'B':w['B'],'source_x_indices':xp,'source_y_indices':yp,
         'input_weights':{'x':[int(get(v)*scale) for v in wx],'y':[int(get(v)*scale) for v in wy]},
         'output_rows':[[[k,int(get(nu[k])*scale)] for k in row] for row in w['output_source_indices']],
         'construction':'Each output row sums source coordinates with the listed Laurent monomial exponents.'}
 Path('/tmp/matrix-mult-source-20261020/laurent-m3-control.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report,indent=2))
