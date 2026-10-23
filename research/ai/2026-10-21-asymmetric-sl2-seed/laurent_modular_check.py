"""Exact finite-field rejection gate for dyadic numerical Laurent maps.

Nonzero residues refute exactness of the supplied maps. Zero residues at
one prime do not certify an identity over Q(i).
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import argparse,json,hashlib,io
import numpy as np
from rectangular_exact import maps
P=65519

def residue(x):
 n,d=float(x).as_integer_ratio();return (n%P)*pow(d%P,-1,P)%P

def multiply(A,B):
 ar,ai=A;br,bi=B;k=ar.shape[-1];assert 2*k*(P-1)**2<2**63
 return ((ar@br-ai@bi)%P,(ar@bi+ai@br)%P)

def tensor(M):
 dims=[m[0].shape[1] for m in M];A,B,C=[(r.T,i.T) for r,i in M];groups=[[] for _ in range(45)]
 def ix(i,k,s):return (i*5+k)*3+s
 for i,j,p,q,r,s in product(range(3),repeat=6):groups[ix(i,p+q,s)].append((ix(p,r+s,j),ix(r,i+j,q)))
 R=np.empty((45,dims[1]*dims[2]),dtype=np.int64);I=R.copy()
 for x,pairs in enumerate(groups):
  ys,zs=map(list,zip(*pairs));v=multiply((B[0][:,ys],B[1][:,ys]),(C[0][:,zs].T,C[1][:,zs].T));R[x]=v[0].ravel();I[x]=v[1].ravel()
 return multiply(A,(R,I))

def inverse_mod(A):
 n=len(A);B=[[int(x)%P for x in row]+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  k=next(k for k in range(i,n) if B[k][i]);B[i],B[k]=B[k],B[i];v=pow(B[i][i],-1,P);B[i]=[(x*v)%P for x in B[i]]
  for k in range(n):
   if k!=i:
    v=B[k][i];B[k]=[(x-v*y)%P for x,y in zip(B[k],B[i])]
 return np.array([r[n:] for r in B],dtype=np.int64)

def check(coeffs):
 H=coeffs[0][0].shape[0];d=(H-1)//2;degree=3*d;count=2*degree+1;values=[[],[]]
 for t in range(1,count+1):
  M=[]
  for R,I in coeffs:
   powers=np.array([pow(t,h,P) if h>=0 else pow(pow(t,-1,P),-h,P) for h in range(d,-d-1,-1)],dtype=np.int64)
   M.append((np.einsum('h,hst->st',powers,R)%P,np.einsum('h,hst->st',powers,I)%P))
  out=tensor(M);shift=pow(t,degree,P)
  for c in range(2):values[c].append((out[c].ravel()*shift)%P)
 inv=inverse_mod([[pow(t,j,P) for j in range(count)] for t in range(1,count+1)]);assert count*(P-1)**2<2**63
 polys=[(inv@np.array(v,dtype=np.int64))%P for v in values];w=coeffs[1][0].shape[2]//5;target=np.zeros((25,5*w,5*w),dtype=np.int64)
 for i,j,k in product(range(5),range(5),range(w)):target[5*i+j,w*j+k,5*k+i]=1
 mismatches={}
 for exponent in range(degree+1):
  R=polys[0][degree+exponent]-(target.ravel() if exponent==0 else 0);I=polys[1][degree+exponent];mismatches[str(exponent)]=int(np.count_nonzero((R%P!=0)|(I%P!=0)))
 return {'prime':P,'field':'F_p[i], i^2=-1','map_degree':d,'original_source_terms_per_evaluation':729,'evaluation_points':count,'required_coefficient_mismatch_counts':mismatches,'exact_supplied_maps_rejected':any(mismatches.values()),'zero_result_would_not_certify_Q_i_identity':True}

def control():
 out=[]
 for leg,M in enumerate(maps()):
  R=np.zeros((3,45,len(M[0])),dtype=np.int64);I=R.copy()
  for s,row in enumerate(M):
   for t,x in enumerate(row):
    exponent=(t//5%2) if leg==0 else (-(t%5%2) if leg==2 else 0)
    R[1-exponent,s,t]=x.numerator*pow(x.denominator,-1,P)%P
  out.append((R,I))
 result=check(out);assert not result['exact_supplied_maps_rejected'];return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args();raw=a.input.read_bytes();z=np.load(io.BytesIO(raw));coeffs=[]
 for n in 'ABC':
  m=z[n];coeffs.append((np.array([residue(x.real) for x in m.ravel()],dtype=np.int64).reshape(m.shape),np.array([residue(x.imag) for x in m.ravel()],dtype=np.int64).reshape(m.shape)))
 result={'status':'exact finite-field rejection test, not a positive identity certificate','input_sha256':hashlib.sha256(raw).hexdigest(),'positive_control':control(),'candidate':check(coeffs)};a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
