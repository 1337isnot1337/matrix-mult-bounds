"""Test a low-degree Laurent interpolation of numerical maps; no proof claim."""
import json
from pathlib import Path
from itertools import product
import numpy as np
from intertwiners import source_data
root=Path('results/local/asymmetric-sl2-seed');names=['gauss-newton-preconditioned','sparse-gauss-newton','sparse-gauss-newton-restart','sparse-gauss-newton-third'];samples=[];ts=[]
for name in names:
 z=np.load(root/name/'best.npz');M=[z[n].copy() for n in 'ABC'];norms=[np.linalg.norm(m) for m in M];t=float(np.prod(norms)**(1/3));ts.append(t);samples.append([m*t/n for m,n in zip(M,norms)])
V=np.array([[t,1,1/t] for t in ts[:3]]);coeff=[np.linalg.solve(V,np.stack([M[leg].ravel() for M in samples[:3]])).reshape(3,*samples[0][leg].shape) for leg in range(3)];W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);P=[np.einsum('ast,sxy->atxy',m,W,optimize=True) for m in coeff]
def contract(X,Y,Z):return np.einsum('ixy,jyz,kzx->ijk',X,Y,Z,optimize=True)
terms={d:np.zeros((25,20,20),dtype=complex) for d in range(-3,4)}
for i,j,k in product(range(3),repeat=3):terms[3-i-j-k]+=contract(P[0][i],P[1][j],P[2][k])
target=np.zeros((25,20,20))
for i,j,k in product(range(5),range(5),range(4)):target[5*i+j,4*j+k,5*k+i]=1
prediction=sum(ts[3]**d*T for d,T in terms.items());map_prediction=[sum(c*t for c,t in zip(C,[ts[3],1,1/ts[3]])) for C in coeff]
r={'status':'numerical interpolation diagnostic only, not a degeneration certificate','input_stages':names,'balanced_leg_norm_parameters':ts,'coefficient_tensor_norms_relative_to_target':{str(d):float(np.linalg.norm(T)/10) for d,T in terms.items()},'constant_term_error':float(np.linalg.norm(terms[0]-target)/10),'fourth_tensor_prediction_error':float(np.linalg.norm(prediction-target)/10),'fourth_map_prediction_relative_errors':[float(np.linalg.norm(A-B)/np.linalg.norm(B)) for A,B in zip(map_prediction,samples[3])],'acceptance_requirement':'All positive Laurent powers must vanish exactly and the constant coefficient must equal the target exactly.'};(root/'laurent-diagnostic.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
