"""Exact weight-restricted SL2 intertwiner bases for physical Hankel matrices."""
from itertools import product
from pathlib import Path
import json
import sympy as sp


def irrep(d):
 E=sp.zeros(d+1);F=sp.zeros(d+1)
 for j in range(1,d+1):E[j-1,j]=j
 for j in range(d):F[j+1,j]=d-j
 return E,F,sp.diag(*[d-2*j for j in range(d+1)])

def representation(degrees):
 blocks=[irrep(d) for d in degrees]
 return tuple(sp.diag(*[b[k] for b in blocks]) for k in range(3))

def source_data(a):
 m=2*a-1;order=list(product(range(a),range(m),range(a)));basis=[]
 for i,k,s in order:
  W=sp.zeros(a*a)
  for p in range(a):
   q=k-p
   if 0<=q<a:W[i*a+q,p*a+s]=1
  basis.append(W)
 E,F,H=irrep(a-1);actions=[]
 for G in (E,F,H):
  physical=sp.kronecker_product(G,sp.eye(a))-sp.kronecker_product(sp.eye(a),G.T)
  cols=[]
  for W in basis:
   V=physical*W-W*physical
   c=[V[i*a+k-min(k,a-1),min(k,a-1)*a+s] for i,k,s in order]
   assert sum((v*B for v,B in zip(c,basis)),sp.zeros(a*a))==V
   cols.append(sp.Matrix(c))
  actions.append(sp.Matrix.hstack(*cols))
 assert actions[0]*actions[1]-actions[1]*actions[0]==actions[2]
 return basis,actions

def target_actions(left,right):
 rows=left[0].rows;cols=right[0].rows;basis=[]
 for i,j in product(range(rows),range(cols)):
  B=sp.zeros(rows,cols);B[i,j]=1;basis.append(B)
 return [sp.Matrix.hstack(*[sp.Matrix(list(L*B-B*R)) for B in basis])
         for L,R in zip(left,right)]

def intertwiner_basis(source,target):
 S=source[0].rows;T=target[0].rows
 assert source[2].is_diagonal() and target[2].is_diagonal()
 variables=[(s,t) for s in range(S) for t in range(T) if source[2][s,s]==target[2][t,t]]
 equations={}
 for k in range(2):
  A,B=source[k],target[k]
  for index,(s,t) in enumerate(variables):
   for u in range(S):
    if A[u,s]:equations.setdefault((k,u,t),{})[index]=A[u,s]
   for v in range(T):
    if B[t,v]:
     row=equations.setdefault((k,s,v),{})
     row[index]=row.get(index,0)-B[t,v]
 rows=list(equations.values());matrix=sp.SparseMatrix(len(rows),len(variables),
     {(i,j):c for i,row in enumerate(rows) for j,c in row.items() if c})
 kernel=matrix.nullspace();out=[]
 for v in kernel:
  den=sp.ilcm(*[x.q for x in v]);ints=[int(x*den) for x in v];g=abs(int(sp.igcd(*ints)))
  Q=sp.zeros(S,T)
  for (s,t),c in zip(variables,ints):Q[s,t]=c//g
  assert all(source[k]*Q==Q*target[k] for k in range(3))
  out.append(Q)
 return out,{'weight_variables':len(variables),'equations':len(rows),'dimension':len(out)}

if __name__=='__main__':
 import numpy as np
 _,source=source_data(3);U=representation([4]);W=representation([2,0,0])
 result={};report={}
 for name,L,R in [('A',U,U),('B',U,W),('C',W,U)]:
  basis,meta=intertwiner_basis(source,target_actions(L,R));report[name]=meta
  result[name]=np.array([np.array(Q).astype(np.int64) for Q in basis])
 assert [report[x]['dimension'] for x in 'ABC']==[9,13,13]
 dest=Path('results/asymmetric-sl2-seed-20261021');dest.mkdir(parents=True,exist_ok=True)
 (dest/'intertwiner-bases.json').write_text(json.dumps({k:v.tolist() for k,v in result.items()},separators=(',',':'))+'\n')
 (dest/'basis-report.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
