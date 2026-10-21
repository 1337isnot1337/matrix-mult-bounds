"""Numerical infinitesimal symmetry diagnostic; no exclusion certificate."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
import sympy as sp
from intertwiners import irrep,source_data
from rectangular_exact import maps

def traceless(n):
 out=[]
 for i in range(n):
  for j in range(n):
   if i!=j:
    X=np.zeros((n,n));X[i,j]=1;out.append(X)
 for i in range(n-1):
  X=np.zeros((n,n));X[i,i]=1;X[-1,-1]=-1;out.append(X)
 return out

def diagnostic(M):
 short=irrep(2);long=irrep(4);axis=[]
 for position in range(3):
  axis.append([np.array(sp.kronecker_product(*(G if i==position else sp.eye([3,5,3][i]) for i in range(3)))).astype(float) for G in (short if position!=1 else tuple(-x.T for x in long))])
 _,diagonal=source_data(3)
 assert all(np.array_equal(sum(axis[j][k] for j in range(3)),np.array(diagonal[k]).astype(float)) for k in range(3))
 w=M[1].shape[1]//5;dims=[5,5,w];positions=[[0,1,2],[2,0,1],[1,2,0]] # source factor -> axis for each leg
 cols=[]
 for factor in range(3):
  for generator in range(3):cols.append(np.concatenate([(axis[positions[leg][factor]][generator]@m).ravel() for leg,m in enumerate(M)]))
 for vertex,n in enumerate(dims):
  for G in traceless(n):
   parts=[]
   for leg,m in enumerate(M):
    rows,cs=dims[leg],dims[(leg+1)%3];T=np.zeros((rows*cs,rows*cs))
    if vertex==leg:T+=np.kron(G,np.eye(cs))
    if vertex==(leg+1)%3:T-=np.kron(np.eye(rows),G.T)
    parts.append((-m@T).ravel())
   cols.append(np.concatenate(parts))
 K=np.stack(cols,axis=1);norms=np.linalg.norm(K,axis=0);assert min(norms)>0
 _,singular,V=np.linalg.svd(K/norms,full_matrices=False)
 return {'status':'numerical symmetry diagnostic only','target':[5,5,w],'equations':K.shape[0],'unknowns':K.shape[1],'smallest_singular_values':singular[-12:].tolist(),'relative_smallest_singular_values':(singular[-12:]/singular[0]).tolist(),'near_null_count_at_1e_minus_10':int(sum(singular<singular[0]*1e-10))}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args();control=diagnostic([np.array(m,dtype=complex) for m in maps()]);assert control['near_null_count_at_1e_minus_10']>=3
 z=np.load(a.input);r={'input_npz_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),'exact_seed_positive_control':control,'candidate':diagnostic([z[n] for n in 'ABC'])};a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
