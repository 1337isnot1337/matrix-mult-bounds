"""Finite-field lower-rank certificates for the invariant source slice."""
import numpy as np,json,time
P=65519

def highest(a,l):
 assert 2<=a and 0<=l<2*a-1 and 2*a<P
 assert max(a*a*(P-1)**2,(P-1)**3)<2**63
 d=a-1;boundary=[(i,s) for i in range(a) for s in range(a) if i+s==2*d-l]
 out=[]
 for ii,ss in boundary:
  F=np.zeros((a,a),dtype=np.int64);F[ii,ss]=1
  for total in range(2*d-l-1,-1,-1):
   for i in range(a):
    s=total-i
    if not 0<=s<a:continue
    v=((i+1)*int(F[i+1,s]) if i+1<a else 0)+((s+1)*int(F[i,s+1]) if s+1<a else 0)
    F[i,s]=v*pow(total+l+1,-1,P)%P
  out.append(F)
 return np.array(out)
def rank(A):
 A=A.copy()%P;n,m=A.shape;r=0
 for j in range(m):
  piv=next((i for i in range(r,n) if A[i,j]),None)
  if piv is None:continue
  A[[r,piv]]=A[[piv,r]];A[r]=A[r]*pow(int(A[r,j]),-1,P)%P
  for i in range(r+1,n):A[i]=(A[i]-int(A[i,j])*A[r])%P
  r+=1
  if r==n:break
 return r

def pairing(a,l):
 d=a-1;F=highest(a,l);C=highest(a,0)[0];m=len(F);result=np.zeros((m,m),dtype=np.int64)
 for h in range(-d,d+1):
  t=h+l
  if not -d<=t<=d:continue
  I=[i for i in range(a) if 0<=i+t<a];J=[j for j in range(a) if 0<=j+h<a]
  C0=C[np.ix_(I,[i+t for i in I])]
  H=F[:,I,:][:,:,[j+h for j in J]]
  L=((-1)**l*F[:,[d-j for j in J],:][:,:,[d-i-t for i in I]])%P
  CH=np.array([C0@Hk%P for Hk in H]);result=(result+CH.reshape(m,-1)@L.transpose(0,2,1).reshape(m,-1).T)%P
 return result

def brute_pairing(a,l):
 from itertools import product
 F=highest(a,l);C=highest(a,0)[0];m=len(F);B=np.zeros((m,m),dtype=np.int64)
 for i,j,p,q,r,ss in product(range(a),repeat=6):
  if p+q!=i+ss or r+ss!=p+j+l or i+j!=r+q-l:continue
  left=F[:,p,j];right=((-1)**l*F[:,a-1-r,a-1-q])%P
  B=(B+int(C[i,ss])*np.outer(left,right))%P
 return B

def certificate(a):
 rows=[]
 for l in range(2*a-1):
  B=pairing(a,l);r=rank(B)
  rows.append({'half_weight':l,'multiplicity':len(B),'rank_mod_p':r,
               'matrix_mod_p':B.tolist()})
 return {'a':a,'prime':P,'channels':rows,
         'full_source_rank_lower_bound':sum((2*r['half_weight']+1)*r['rank_mod_p'] for r in rows),
         'source_leg_dimension':a*a*(2*a-1),'independent_review':False}

if __name__=='__main__':
 import argparse
 from pathlib import Path
 p=argparse.ArgumentParser();p.add_argument('--a',type=int,default=24);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
 report=certificate(args.a);args.output.write_text(json.dumps(report,indent=2)+'\n');print({k:v for k,v in report.items() if k!='channels'})
