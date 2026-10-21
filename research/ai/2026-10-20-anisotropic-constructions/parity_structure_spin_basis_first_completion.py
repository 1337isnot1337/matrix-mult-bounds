"""Exact-field first-map completion probes after changed local spin bases."""
from itertools import product,combinations
from pathlib import Path
import json,sys
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/ai/2026-10-20-anisotropic-constructions'))
import parity_structure_spin_basis_compression as b
P=65521

def rref(a):
    a=np.asarray(a,dtype=np.int64).copy()%P;r=0;piv=[]
    for c in range(a.shape[1]):
        s=np.flatnonzero(a[r:,c])
        if not len(s):continue
        k=r+int(s[0]);a[[r,k]]=a[[k,r]]
        a[r]=a[r]*pow(int(a[r,c]),-1,P)%P
        f=a[:,c].copy();f[r]=0;a=(a-f[:,None]*a[r])%P
        piv.append(c);r+=1
        if r==a.shape[0]:break
    return a,piv

def response(y,z):
    R=np.zeros((112,81,81),dtype=np.int64)
    for i,p,r,j,q,s in product(range(4),repeat=6):
        x=(i*7+p+q)*4+s;cy=(p*7+r+s)*4+j;cz=(r*7+i+j)*4+q
        R[x]+=np.outer(y[:,cy],z[:,cz])
    return R

def solve(R,A,B):
    yrows=[9*j+k for j in B for k in range(9)]
    zrows=[9*k+i for i in A for k in range(9)]
    matrix=R[:,yrows,:][:,:,zrows].reshape(112,-1)
    T=np.zeros((len(A)*len(B),len(yrows)*len(zrows)),dtype=np.int64)
    for ii,jj,k in product(range(len(A)),range(len(B)),range(9)):
        T[ii*len(B)+jj,(9*jj+k)*len(zrows)+9*ii+k]=16
    reduced,piv=rref(np.concatenate([matrix,T],axis=0))
    # Rank additivity from the same deterministic coefficient ordering.
    rr,pp=rref(matrix)
    missing=len(piv)-len(pp)
    return {'A':list(A),'B':list(B),'source_response_rank':len(pp),'target_extra_rank':missing,'compatible':missing==0}

def main():
    controls={}
    controls['base']=[b.J,b.J,b.J]
    gs=[np.array([[1,1],[0,1]],float),np.array([[1,0],[-1,1]],float),np.array([[0,1],[-1,0]],float)]
    controls['integral_source_basis']=b.transformed_local(gs)
    allreports=[]
    for label,low in controls.items():
        maps=b.compress([low,[b.J,b.J,b.J]])
        nums=[np.rint(4*m).astype(np.int64) for m in maps]
        if any(not np.array_equal(4*m,n) for m,n in zip(maps,nums)):raise ArithmeticError('Nonintegral control')
        R=response(nums[1],nums[2]);good=[]
        for n in [9,8,7,6,5,4,3,2]:
            result=solve(R,range(n),range(n));result['control']=label
            allreports.append(result);print(json.dumps(result),flush=True)
            if result['compatible']:good.append(n)
        # Response arrays are regenerated from the exact fixed maps; only the report is retained.
    (ROOT/'results/anisotropic-constructions-2026-10-20/parity_structure_spin_basis_first_completion_discovery.json').write_text(json.dumps({'prime':P,'completed_prefix_controls':allreports,'rational_target_accepted':False},indent=2)+'\n')

if __name__=='__main__':main()
