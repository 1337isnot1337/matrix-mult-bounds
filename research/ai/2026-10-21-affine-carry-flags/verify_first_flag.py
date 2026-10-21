"""Exact affine first-flag controls, using only the Python standard library."""
import json
from pathlib import Path

def add(x,y):return [(x[i] if i<len(x) else 0)+(y[i] if i<len(y) else 0) for i in range(max(len(x),len(y)))]
def scale(x,c):return [c*t for t in x]
def mono(k,c=1):return [0]*k+[c]
def mul(x,y):
 z=[0]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):z[i+j]+=a*b
 return z
def rank_mod(rows,p=101):
 if not rows:return 0
 A=[[x%p for x in r] for r in rows];n=len(A[0]);r=0
 for c in range(n):
  q=next((q for q in range(r,len(A)) if A[q][c]),None)
  if q is None:continue
  A[r],A[q]=A[q],A[r];z=pow(A[r][c],-1,p);A[r]=[(x*z)%p for x in A[r]]
  for i in range(r+1,len(A)):
   z=A[i][c]
   if z:A[i]=[(x-z*y)%p for x,y in zip(A[i],A[r])]
  r+=1
 return r

def verify():
    reports=[];total=0
    for m in range(4,25):
     B=m*(m+1)//2+2;a,b=2,-1
     r=add(add([1],mono(m,b)),mono(m+1,a))
     U=[add(r,mono(m,-b)),mul([0,1],r)]+[mono(j) for j in range(3,m+1)]
     h=[((j*j+7*j+3*m)%11)-5 for j in range(B-1)]
     g=[((3*j*j+5*j+2*m+1)%13)-6 for j in range(B-2)]
     Y=[[1],h,mul([0,1],h),g,add([1],mul([0,1],g)),add([0,1],mul([0,0,1],g))]
     out=B+m+2
     products=[mul(u,y)+[0]*(out-len(u)-len(y)+1) for y in Y for u in U]
     pairs=[]
     u=[0]*m;u[0]=1;u[-1]=b;tu=[0]*m;tu[1]=1;pairs.append((u,tu))
     for j in range(3,m):
      u=[0]*m;tu=[0]*m;u[j-1]=1;tu[j]=1;pairs.append((u,tu))
     relations=[]
     for u,tu in pairs:
      R=[0]*(6*m)
      for i in range(m):R[m+i]=tu[i];R[2*m+i]=-u[i]
      relations.append(R)
      R=[0]*(6*m)
      for i in range(m):R[i]=u[i];R[3*m+i]=tu[i];R[4*m+i]=-u[i]
      relations.append(R)
      R=[0]*(6*m)
      for i in range(m):R[4*m+i]=tu[i];R[5*m+i]=-u[i]
      relations.append(R)
     for R in relations:
      if any(sum(c*v[j] for c,v in zip(R,products)) for j in range(out)):raise ValueError("polynomial relation failed")
     relrank=rank_mod(relations);prank=rank_mod(products)
     if relrank!=3*(m-2) or prank>3*m+6:raise ValueError("rank check failed")
     reports.append({"m":m,"B":B,"relations":len(relations),"relation_rank_mod101":relrank,"product_rank_mod101":prank,"bound":3*m+6})
     total+=len(relations)*out
    report={"scope":"first six labelled input rows only","integer_relation_coefficients_checked":total,"cases":reports}
    return report

if __name__ == "__main__":
    report=verify()
    ROOT=Path(__file__).resolve().parents[3]
    (ROOT/"results/affine-carry-flags-2026-10-21/first-flag-controls.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"cases":len(report["cases"]),"coefficients":report["integer_relation_coefficients_checked"],"all_bounds_attained":all(r["product_rank_mod101"]==r["bound"] for r in report["cases"])}))
