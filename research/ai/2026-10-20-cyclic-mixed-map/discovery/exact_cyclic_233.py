import json,math
from fractions import Fraction
from itertools import product
from pathlib import Path
import numpy as np
root=Path('results/local/cyclic-mixed-map');root.mkdir(parents=True,exist_ok=True)
w=np.load(root/'cyclic-als-a2-m233-normalized.npz');F=[];maxerr=0
for name in ('A','B','C'):
 entries=[]
 for (i,j),v in np.ndenumerate(w[name]):
  if abs(v)<1e-10:continue
  e=round(4*math.log2(abs(v)));s=1 if v>0 else -1;maxerr=max(maxerr,abs(v-s*2**(e/4)));entries.append([i,j,s,e])
 F.append(entries)
source=[]
for i,j,p,q,r,s in product(range(2),repeat=6):source.append(((i*3+p+q)*2+s,(j*2+p)*3+r+s,((i+j)*2+q)*2+r))
bycol=[]
for entries in F:
 d={j:[] for j in range(12)}
 for i,j,s,e in entries:d[j].append((i,s,e))
 bycol.append(d)
out={}
for a,b,c in source:
 for i,sa,ea in bycol[0][a]:
  for j,sb,eb in bycol[1][b]:
   for k,sc,ec in bycol[2][c]:
    e=ea+eb+ec;q,r=divmod(e,4);v=sa*sb*sc*(Fraction(2)**q);out[i,j,k,r]=out.get((i,j,k,r),Fraction(0))+v
wanted={(i*3+j,j*3+k,k*2+i,0):Fraction(1) for i,j,k in product(range(2),range(3),range(3))}
out={k:v for k,v in out.items() if v};print('maximum recognition error',maxerr,'exact equality',out==wanted,'nonzero coefficients',len(out),'support sizes',[len(x) for x in F])
assert out==wanted
report={'field':'Q(q), q^4=2, q positive real','source':'A_2','target':'M(2,3,3)','entry_format':['row','column','sign','exponent_of_q'],'maps':dict(zip(('A','B','C'),F)),'recognized_maximum_float_error':maxerr,'full_exact_equality':True,'coefficient_count':324}
(root/'cyclic-a2-m233-exact-algebraic.json').write_text(json.dumps(report,indent=2)+'\n')
