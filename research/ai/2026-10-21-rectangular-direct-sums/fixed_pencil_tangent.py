from collections import defaultdict
import json,time
from fractions import Fraction

def rank_sparse(columns,prime=None):
 pivots={}
 for col in columns:
  v={k:(x%prime if prime else Fraction(x)) for k,x in col.items() if x}
  while v:
   k=min(v)
   if k not in pivots:
    inv=pow(v[k],-1,prime) if prime else 1/v[k];pivots[k]={j:(x*inv%prime if prime else x*inv) for j,x in v.items()};break
   scale=v[k]
   for j,x in pivots[k].items():
    z=v.get(j,0)-scale*x
    if prime:z%=prime
    if z:v[j]=z
    else:v.pop(j,None)
 return len(pivots)

def local_report(a,b):
 n=a+1;U={(0,0,0):1};V={(0,0,0):1}
 for h in range(1,n):U[1,h-1,h]=1;V[1,h,a-h]=1
 Ud=[];Vd=[]
 for p in range(a):
  for ss in range(b-1):Ud.append({(ss,p,0):1,(ss+1,p,1):1})
  for h in range(2,n):
   for ss in range(b):Ud.append({(ss,p,h):1})
 for q in range(b):
  for i in range(a-1):Vd.append({(i,0,q):1,(i+1,a,q):1})
  for h in range(1,a):
   for i in range(a):Vd.append({(i,h,q):1})
 def mult(U,V):
  C=defaultdict(int)
  for (ss,p,h),x in U.items():
   for (i,hh,q),y in V.items():
    if h==hh:C[i,p,q,ss]+=x*y
  return {k:x for k,x in C.items() if x}
 columns=[mult(u,V) for u in Ud]+[mult(U,v) for v in Vd]
 # Quotient general p,q coefficients by Hankel-constant anti-diagonals.
 reps={k:(max(0,k-b+1),k-max(0,k-b+1)) for k in range(a+b-1)}
 def defect(C):
  D={}
  for i in range(a):
   for ss in range(b):
    for p in range(a):
     for q in range(b):
      pp,qq=reps[p+q]
      if (p,q)==(pp,qq):continue
      z=C.get((i,p,q,ss),0)-C.get((i,pp,qq,ss),0)
      if z:D[i,p,q,ss]=z
  return D
 D=[defect(c) for c in columns];B_rank=rank_sparse(columns);D_rank=rank_sparse(D)
 return {'a':a,'b':b,'variables':len(columns),'exact_derivative_rank':B_rank,'exact_hankel_defect_rank':D_rank,'exact_image_tangent_dimension':B_rank-D_rank,'fixed_kernel_pencils':True,'local_linearization_only':True}
def report():
 return {'status':'exact tangent calculation only; no integrable family or exponent gain','controls':[local_report(a,b) for a,b in [(2,3),(3,4),(8,10)]]}

if __name__=='__main__':
 import argparse
 from pathlib import Path
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args();result=report();args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
