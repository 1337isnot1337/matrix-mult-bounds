"""Finite-field discovery only: exact truncated root expansions of a cyclic q family."""
import importlib.util
from pathlib import Path
_spec=importlib.util.spec_from_file_location("quantum_core",Path(__file__).resolve().parents[1]/"quantum.py")
m=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(m)
from functools import lru_cache
import numpy as np
from math import comb

PRIME=65537

def rational_mod(c):return int(c.numerator)*pow(int(c.denominator),-1,PRIME)%PRIME

def expand_poly(poly,root,length):
    out=[0]*length
    for (e,),c in poly.items():
        c=rational_mod(c)
        for k in range(min(e,length-1)+1):out[k]=(out[k]+c*comb(e,k)*pow(root,e-k,PRIME))%PRIME
    return out

@lru_cache(None)
def series(value,root,length):
    if not value:return 10**6,tuple([0]*length)
    # The degrees are small enough that expanding the complete polynomial
    # identifies its exact finite-field order, rather than guessing a pole.
    num=expand_poly(value.numer,root,value.numer.degree()+1)
    den=expand_poly(value.denom,root,value.denom.degree()+1)
    a=next(i for i,c in enumerate(num) if c);b=next(i for i,c in enumerate(den) if c)
    num=num[a:]+[0]*length;den=den[b:]+[0]*length
    inv=pow(den[0],-1,PRIME);out=[]
    for k in range(length):out.append((num[k]-sum(den[j]*out[k-j] for j in range(1,k+1)))*inv%PRIME)
    return a-b,tuple(out)

def cyclic_local_map(a):return m.cyclic_local_map(a)

def source(a):
    D=a-1;h=2*D;V=a*a*(h+1);out=np.zeros((V,V,V),dtype=np.float64)
    for i in range(a):
        for j in range(a):
            for p in range(a):
                for q in range(a):
                    for r in range(a):
                        for s in range(a):
                            A=(i*a+s)*(h+1)+h-p-q
                            B=(p*a+j)*(h+1)+h-r-s
                            C=(r*a+q)*(h+1)+h-i-j
                            out[A,B,C]+=1
    return out

def contract(tensor,A,B,C):
    V=len(A)
    t=np.remainder(np.rint(A@tensor.reshape(V,-1)),PRIME).reshape(V,V,V)
    t=np.remainder(np.rint(B@t.transpose(1,0,2).reshape(V,-1)),PRIME).reshape(V,V,V).transpose(1,0,2)
    return np.remainder(np.rint(C@t.transpose(2,0,1).reshape(V,-1)),PRIME).reshape(V,V,V).transpose(1,2,0).astype(np.int64)

def matrix_rank_mod(matrix):
    a=np.array(matrix,dtype=np.int64,copy=True);rank=0
    for j in range(a.shape[1]):
        choices=np.flatnonzero(a[rank:,j])
        if not len(choices):continue
        k=rank+int(choices[0]);a[[rank,k]]=a[[k,rank]]
        a[rank]=a[rank]*pow(int(a[rank,j]),-1,PRIME)%PRIME
        for i in range(rank+1,len(a)):
            if a[i,j]:a[i]=(a[i]-a[i,j]*a[rank])%PRIME
        rank+=1
        if rank==len(a):break
    return rank

def initial(a,output_dir,root=256,length=4):
    import time
    started=time.time();labels,entries=cyclic_local_map(a);V=len(labels)
    print('local map',a,V,len(entries),'seconds',time.time()-started,flush=True)
    expansions={(i,j):series(c,root,length) for (i,j),c in entries.items()}
    minima=[min(v for (i,j),(v,c) in expansions.items() if i==row) for row in range(V)]
    mats=np.zeros((length,V,V),dtype=np.float64)
    for (i,j),(v,c) in expansions.items():
        shift=v-minima[i]
        for k in range(shift,length):mats[k,i,j]=c[k-shift]
    tensor=source(a);lead=contract(tensor,*([mats[0]]*3))
    print('row-normalized constant map rank',matrix_rank_mod(mats[0]),'tensor nonzero',np.count_nonzero(lead),flush=True)
    report={'a':a,'prime':PRIME,'root':root,'series_length':length,'row_minimum_valuations':minima,
            'constant_map_rank':matrix_rank_mod(mats[0]),'constant_tensor_nonzero_coefficients':int(np.count_nonzero(lead))}
    for p in range(length):
        if p==0:t=lead
        else:
            t=np.zeros_like(lead)
            for i in range(p+1):
                for j in range(p-i+1):
                    k=p-i-j
                    t=(t+contract(tensor,mats[i],mats[j],mats[k]))%PRIME
        count=int(np.count_nonzero(t));print('power',p,'nonzeros',count,flush=True)
        if count:
            report['first_nonzero_power']=p
            report['first_tensor_flattening_ranks']=[matrix_rank_mod(t.transpose(i,*[j for j in range(3) if j!=i]).reshape(V,-1)) for i in range(3)]
            np.savez_compressed(output_dir/f'quantum-cyclic-a{a}-root{root}-initial.npz',tensor=t,matrices=mats)
            break
    return report

if __name__=='__main__':
    import json,argparse,sys,sympy
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    reports=[]
    for a in [2,3,4]:reports.append(initial(a,args.output_dir))
    result={'scope':'Finite-field discovery only. The complex acceptance calculation is in quantum.py. No exponent improvement.',
            'environment':{'python':sys.version.split()[0],'sympy':sympy.__version__,'numpy':np.__version__},'records':reports}
    (args.output_dir/'cyclic-initial-discovery.json').write_text(json.dumps(result,indent=2)+'\n')
