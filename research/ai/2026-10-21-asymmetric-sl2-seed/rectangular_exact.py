"""Replay rational A(3,3) -> M(5,5,3) maps on all original source terms."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from math import lcm
import json
ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/'results/asymmetric-sl2-seed-20261021'
def maps():
 data=json.loads((RESULT/'rectangular-exact.json').read_text());bases=json.loads((RESULT/data['basis_file']).read_text());out=[]
 for name in 'ABC':
  coeff=list(map(Fraction,data['coefficients'][name]));basis=bases[name]
  out.append([[sum((c*B[i][j] for c,B in zip(coeff,basis)),Fraction()) for j in range(len(basis[0][0]))] for i in range(45)])
 return out

def verify():
 matrices=maps();denoms=[lcm(*(v.denominator for row in M for v in row)) for M in matrices];rows=[[[ (j,int(v*d)) for j,v in enumerate(row) if v] for row in M] for d,M in zip(denoms,matrices)];out=defaultdict(int);terms=0
 def idx(i,k,s):return (i*5+k)*3+s
 # C(3,3)^cyc: (i,p+q,s), (p,r+s,j), (r,i+j,q).
 for i in range(3):
  for j in range(3):
   for p in range(3):
    for q in range(3):
     for r in range(3):
      for s in range(3):
       terms+=1
       for a,x in rows[0][idx(i,p+q,s)]:
        for b,y in rows[1][idx(p,r+s,j)]:
         for c,z in rows[2][idx(r,i+j,q)]:out[a,b,c]+=x*y*z
 scale=denoms[0]*denoms[1]*denoms[2];errors=[]
 for a in range(25):
  for b in range(15):
   for c in range(15):
    expected=scale*int(a%5==b//3 and b%3==c//5 and c%5==a//5)
    if out[a,b,c]!=expected:errors.append((a,b,c,out[a,b,c],expected))
 if errors:raise AssertionError(errors[:5])
 return {'source_terms_checked':terms,'target_coefficients_checked':5625,'target_nonzero_coefficients':75,'denominators':denoms,'status':'exact rational restriction verified','improves_omega':False}
if __name__=='__main__':print(json.dumps(verify(),indent=2))
