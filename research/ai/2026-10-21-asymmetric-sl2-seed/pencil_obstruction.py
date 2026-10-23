"""Exact pencil invariant for the asymmetric five-dimensional vertex action."""
from collections import Counter
from itertools import product
from math import factorial
from pathlib import Path
import importlib.util,json
import sympy as sp
spec=importlib.util.spec_from_file_location('asymmetric_intertwiners',Path(__file__).with_name('intertwiners.py'))
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)

def highest(actions,d):
 indices=[i for i in range(actions[0].rows) if actions[2][i,i]==d]
 out=[]
 for v in actions[0][:,indices].nullspace():
  z=sp.zeros(actions[0].rows,1)
  for i,x in zip(indices,v):z[i]=x
  out.append(z)
 return out

def physical(v,basis):
 return sum((x*B for x,B in zip(v,basis)),sp.zeros(basis[0].rows,basis[0].cols))

def trace_source_control(a=3):
 m=2*a-1;idx=lambda i,k,s:(i*m+k)*a+s
 physical_points=Counter()
 for u,v,w in product(range(a*a),repeat=3):
  physical_points[(idx(u//a,u%a+v//a,v%a),idx(v//a,v%a+w//a,w%a),idx(w//a,w%a+u//a,u%a))]+=1
 original_points=Counter()
 for i,j,p,q,r,s in product(range(a),repeat=6):
  original_points[(idx(i,p+q,s),idx(p,r+s,j),idx(r,i+j,q))]+=1
 assert physical_points==original_points and len(original_points)==a**6
 assert set(original_points.values())=={1}
 return len(original_points)

def matrix_record(M):return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

def report():
 W,S=e.source_data(3);U=e.representation([4]);V=e.representation([2,0,0])
 A=e.target_actions(U,U);B=e.target_actions(U,V);C=e.target_actions(V,U)
 mult=[len(highest(S,d)) for d in (0,2,4,6,8)];assert mult==[1,2,3,2,1]
 source0=physical(highest(S,0)[0],W)
 source8=physical(S[1]**4*highest(S,8)[0]/factorial(4),W)
 sh=highest(S,4);SB=[physical(v,W) for v in sh]
 SC=[physical(S[1]**4*v/factorial(4),W) for v in sh]
 target0=sp.Matrix(5,5,list(highest(A,0)[0]))
 target8=sp.Matrix(5,5,list(A[1]**4*highest(A,8)[0]/factorial(4)))
 TB=[sp.Matrix(5,5,list(v)) for v in highest(B,4)]
 TC=[sp.Matrix(5,5,list(C[1]**4*v/factorial(4))) for v in highest(C,4)]
 out={'source_terms_checked':trace_source_control(),'source_multiplicities':mult,
      'status':'exact finite invariant; general symmetry-class proof written and unreviewed'}
 for name,Z0,Z8,X,Y in [('source',source0,source8,SB,SC),('target',target0,target8,TB,TC)]:
  G0=sp.Matrix([[sp.trace(Z0*x*y) for y in Y] for x in X])
  G8=sp.Matrix([[sp.trace(Z8*x*y) for y in Y] for x in X])
  assert G0.det()!=0
  H=G0.inv()*G8;Q=G0.adjugate()*G8
  invariant=sp.factor(43923*sp.trace(Q*Q)-43216*sp.trace(Q)**2)
  out[name]={'G0':matrix_record(G0),'G8':matrix_record(G8),'det_G0':str(G0.det()),
             'trace_H':str(sp.trace(H)),'trace_H_squared':str(sp.trace(H*H)),
             'scale_invariant_ratio':str(sp.factor(sp.trace(H*H)/sp.trace(H)**2)),
             'characteristic_coefficients':[str(c) for c in H.charpoly().all_coeffs()],
             'polynomial_invariant':str(invariant)}
 assert out['source']['scale_invariant_ratio']=='43216/43923'
 assert out['target']['scale_invariant_ratio']=='11/8'
 assert out['source']['polynomial_invariant']=='0'
 assert out['target']['polynomial_invariant']=='137425/8'
 return out

def verify_saved(saved):
 actual=report()
 if saved!=actual:raise ArithmeticError('Pencil certificate differs from exact source/target reconstruction')
 return actual

if __name__=='__main__':print(json.dumps(report(),indent=2))
