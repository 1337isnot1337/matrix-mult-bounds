import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from pencil_obstruction import *
W,S=e.source_data(3);U=e.representation([4]);V=e.representation([2,2]);A=e.target_actions(U,U);B=e.target_actions(U,V);C=e.target_actions(V,U)
source0=physical(highest(S,0)[0],W);source8=physical(S[1]**4*highest(S,8)[0]/factorial(4),W)
SB=[physical(v,W) for v in highest(S,6)];SC=[physical(S[1]**6*v/factorial(6),W) for v in highest(S,6)]
target0=sp.Matrix(5,5,list(highest(A,0)[0]));target8=sp.Matrix(5,5,list(A[1]**4*highest(A,8)[0]/factorial(4)))
TB=[sp.Matrix(5,6,list(v)) for v in highest(B,6)];TC=[sp.Matrix(6,5,list(C[1]**6*v/factorial(6))) for v in highest(C,6)]
out={}
for name,Z0,Z8,X,Y in [('source',source0,source8,SB,SC),('target',target0,target8,TB,TC)]:
 G0=sp.Matrix([[sp.trace(Z0*x*y) for y in Y] for x in X]);G8=sp.Matrix([[sp.trace(Z8*x*y) for y in Y] for x in X]);H=G0.inv()*G8;out[name]={'G0':matrix_record(G0),'G8':matrix_record(G8),'H':matrix_record(H),'trace':str(sp.trace(H)),'trace2':str(sp.trace(H*H)),'ratio':str(sp.factor(sp.trace(H*H)/sp.trace(H)**2))}
assert out['source']['ratio']=='26/27' and out['target']['ratio']=='1/2'
for side in ['source','target']:
 G0=sp.Matrix(out[side]['G0']);G8=sp.Matrix(out[side]['G8']);Q=G0.adjugate()*G8
 out[side]['polynomial_invariant']=str(sp.factor(27*sp.trace(Q*Q)-26*sp.trace(Q)**2))
assert out['source']['polynomial_invariant']=='0' and out['target']['polynomial_invariant']=='-50'
print(json.dumps(out,indent=2))
