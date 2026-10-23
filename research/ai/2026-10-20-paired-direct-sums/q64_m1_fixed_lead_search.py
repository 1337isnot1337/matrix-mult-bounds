"""One fixed-Q54-M1-leading, free-corner-kernel bounded Laurent pilot."""
from itertools import product
import json
from pathlib import Path
import sys,time
import numpy as np
REPO=Path(__file__).resolve().parents[3]
from q64_m1_leading_search import initial,setup
from q64_m1_leading_exact import embedded_product_maps
from q64_complete_flag_search import bounded_step



def run(seed, iterations, budget, prefix):
    SEED=seed;ITERATIONS=iterations;BUDGET=budget;PREFIX=Path(prefix)
    weights,target,degree=setup(None)
    source=np.zeros((36,36,36))
    for p,q,y,v in product(range(6),range(6),range(4),range(4)):
        source[6*p+q,9*y+q+v,4*(p+y)+v]=1
    # An orthonormal basis of ker(f tensor f), f(X)=(X1,X0+X4).
    vectors=np.zeros((6,6));vectors[0,1]=1
    vectors[1,0]=vectors[1,4]=1/np.sqrt(2)
    vectors[2,0]=1/np.sqrt(2);vectors[2,4]=-1/np.sqrt(2)
    vectors[3,2]=vectors[4,3]=vectors[5,5]=1
    K=np.array([np.outer(vectors[i],vectors[j]).ravel() for i,j in product(range(6),repeat=2) if i>=2 or j>=2])
    assert np.max(np.abs(K@K.T-np.eye(32)))<1e-14
    fixed=[np.array(x,complex) for x in embedded_product_maps()]
    maps=initial('product',SEED)
    newrows=[list(range(1,25)),list(range(4,20)),[5*j+k for j,k in product(range(4),range(1,5))]]
    rng=np.random.default_rng(SEED+1)
    for axis in [1,2]:
        for row in newrows[axis]:
            maps[axis][row]+=0.03*(rng.normal(size=36)+1j*rng.normal(size=36))/np.sqrt(72)
    maps[0][0]=fixed[0][0]
    maps[0][1:]=(maps[0][1:]@K.T)@K
    maps[1][:4]=fixed[1][:4]
    maps[2][[0,5,10,15]]=fixed[2][[0,5,10,15]]
    PREFIX.with_name(PREFIX.name+'-initial.json').write_text(json.dumps({'maps_real':[m.real.tolist() for m in maps],'maps_imag':[m.imag.tolist() for m in maps],'seed':SEED,'auxiliary_rank':0,'initialization':'Q54 product seed plus t5 first-map extension; noise 0.2 on fourth outer B/C row and noise0.03 on all16 new rows; old leading rows fixed; all24 other A rows projected into K0'},separators=(',',':'))+'\n')
    layouts=[]
    for axis in range(3):
        other=[x for x in range(3) if x!=axis]
        od=(weights[other[0]][:,None]+weights[other[1]][None,:]).ravel()
        order=np.argsort(od,kind='stable');count=np.searchsorted(od[order],-weights[axis],side='right')
        wanted=np.transpose(target,(axis,*other)).reshape(target.shape[axis],-1)[:,order]
        layouts.append((other,order,count,wanted,np.transpose(source,(axis,*other))))
    fixednorms=[np.linalg.norm(m[[i for i in range(m.shape[0]) if i not in rows]]) for m,rows in zip(maps,newrows)]
    budgets=[float(np.sqrt(BUDGET**2-x*x)) for x in fixednorms]
    started=time.monotonic();history=[];best=float('inf');ridges=[None]*3
    for step in range(ITERATIONS+1):
        if step%50==0 or step==ITERATIONS:
            actual=np.einsum('is,jt,ku,stu->ijk',*maps,source,optimize=True);error=actual-target
            relative=float(np.linalg.norm(error[degree<=0])/10)
            h0=np.einsum('is,jt,ast->aij',maps[1][:4],maps[2][[0,5,10,15]],source,optimize=True).reshape(36,16)
            h1b=np.einsum('is,jt,ast->aij',maps[1][newrows[1]],maps[2][[0,5,10,15]],source,optimize=True).reshape(36,64)
            h1c=np.einsum('is,jt,ast->aij',maps[1][:4],maps[2][newrows[2]],source,optimize=True).reshape(36,64)
            h1=K@np.concatenate([h1b,h1c],axis=1);s=np.linalg.svd(h1,compute_uv=False)
            rec={'iteration':step,'relative_nonpositive_coefficient_error':relative,'maximum_nonpositive_error':float(np.max(np.abs(error[degree<=0]))),'negative_coefficient_norm':float(np.linalg.norm(actual[degree<0])),'constant_coefficient_error_norm':float(np.linalg.norm(error[degree==0])),'positive_coefficient_norm':float(np.linalg.norm(actual[degree>0])),'map_norms':[float(np.linalg.norm(m)) for m in maps],'map_smallest_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],'A_rows_outside_K0_norm':float(np.linalg.norm(maps[0][1:]@h0)),'first_jet_singular_values':s.tolist(),'first_jet_tail_after16':float(np.linalg.norm(s[16:])),'first_jet_relative_tail_after16':float(np.linalg.norm(s[16:])/np.linalg.norm(s)),'ridge_parameters':ridges.copy(),'elapsed_seconds':time.monotonic()-started}
            history.append(rec);print(json.dumps(rec),flush=True)
            if relative<best:
                best=relative
                PREFIX.with_name(PREFIX.name+'-checkpoint.json').write_text(json.dumps({'n':6,'b':4,'target_outer':5,'auxiliary_rank':0,'seed':SEED,'iteration':step,'map_row_powers':[w.tolist() for w in weights],'maps_real':[m.real.tolist() for m in maps],'maps_imag':[m.imag.tolist() for m in maps],'relative_nonpositive_coefficient_error':relative,'exact_coefficient_certificate':False,'leading_B_C_fixed':True,'A_non_old_parameter_space':'K0=ker(f tensor f), dimension32','corner_kernel_free':True,'norm_budget':BUDGET},separators=(',',':'))+'\n')
            if not np.isfinite(relative) or relative<1e-12:break
        if step==ITERATIONS:break
        for axis,(other,order,count,wanted,st) in enumerate(layouts):
            env=np.einsum('jt,ku,stu->sjk',maps[other[0]],maps[other[1]],st,optimize=True).reshape(36,-1)[:,order]
            if axis==0:env=K@env
            grams=np.cumsum(np.einsum('ik,jk->kij',env,env.conj()),axis=0)
            cross=wanted[newrows[axis]]@env.conj().T
            solved,ridges[axis]=bounded_step(grams[count[newrows[axis]]-1],cross,budgets[axis])
            maps[axis][newrows[axis]]=solved@K if axis==0 else solved
    result={'source':'Q(6,4)','target':'M(5,4,5)','auxiliary_rank':0,'seed':SEED,'maximum_iterations':ITERATIONS,'iterations_completed':step,'actual_stop_reason':'iteration_budget' if step==ITERATIONS else ('coefficient_tolerance' if np.isfinite(best) and best<1e-12 else 'nonfinite'),'history':history,'best_relative_nonpositive_coefficient_error':best,'norm_budget':BUDGET,'fixed_old_map_norms':[float(x) for x in fixednorms],'free_row_norm_budgets':budgets,'target_gauge':'none; leading B/C and A00 held fixed','leading_pre_A_rank':4,'all24_other_A_rows_parameterized_in_K0':True,'all16_new_B_C_rows_free':True,'exact_coefficient_certificate':False,'degeneration_proved':False,'improves_omega':False}
    PREFIX.with_name(PREFIX.name+'-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='history'},indent=2))
    return result


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=202610453)
    parser.add_argument('--iterations',type=int,default=1500)
    parser.add_argument('--norm-budget',type=float,default=30.0)
    parser.add_argument('--prefix',type=Path,required=True)
    args=parser.parse_args()
    run(args.seed,args.iterations,args.norm_budget,args.prefix)
