"""One bounded ordinary R16x18x18 -> diagonal-deleted M4 experiment."""
from pathlib import Path
from itertools import product
import json,sys,time
import numpy as np
REPO=Path(__file__).resolve().parents[3]
from q64_complete_flag_search import bounded_step
from narrow_rectangle_balanced import balance_pair


def run(seed, iterations, budget, prefix):
    SEED=seed;ITERATIONS=iterations;BUDGET=budget;PREFIX=Path(prefix)
    raw=(REPO/'research/ai/2026-10-20-paired-construction/m1-endpoint-corner.json').read_bytes()
    certificate=json.loads(raw);source=np.zeros((16,18,18))
    for a,b,c,x in certificate['corner_terms']:source[a,b,c]=x
    pairs=[(i,k) for i,k in product(range(4),repeat=2) if i!=k]
    target=np.zeros((12,16,16))
    for a,(i,k) in enumerate(pairs):
        for j in range(4):target[a,4*i+j,4*j+k]=1
    assert np.count_nonzero(target)==48
    # Exact rational right inverse of the rank-seven product matrix. It splits
    # the single duplicate pair (P1,w1),(P3,w0) evenly.
    L=np.zeros((8,7));L[0,0]=1;L[1,5]=-1;L[2,1]=1;L[3,3]=0.5
    L[4,2]=L[4,5]=L[5,4]=1;L[6,3]=0.5;L[7,6]=1
    maps=[np.zeros((12,16),complex),np.zeros((16,18),complex),np.zeros((16,18),complex)]
    for a,(i,k) in enumerate(pairs):maps[0][a,4*k+i]=1
    for i,y,v,s in product(range(4),range(2),range(2),range(7)):
        maps[1][4*i+2*y+v,7*y+s]=L[2*i+v,s]
    for k,y,v,s in product(range(4),range(2),range(2),range(7)):
        maps[2][4*(2*y+v)+k,2*s+v]=L[2*k+y,s]
    rng=np.random.default_rng(SEED)
    for axis in [1,2]:
        maps[axis][:,14:]=0.1*(rng.normal(size=(16,4))+1j*rng.normal(size=(16,4)))/np.sqrt(8)
        maps[axis][:,:14]+=0.01*(rng.normal(size=(16,14))+1j*rng.normal(size=(16,14)))/np.sqrt(28)
    PREFIX.with_name(PREFIX.name+'-initial.json').write_text(json.dumps({'source':'reduced endpoint corner R','source_dimensions':[16,18,18],'target_pairs':pairs,'maps_real':[m.real.tolist() for m in maps],'maps_imag':[m.imag.tolist() for m in maps],'seed':SEED,'auxiliary_rank':0},separators=(',',':'))+'\n')
    
    def gauge(mm):
        a,b,c=mm[0],mm[1].reshape(4,4,18),mm[2].reshape(4,4,18)
        for _ in range(2):
            b,c=balance_pair(b,1,c,0)
            for i in range(4):
                rows=[r for r,pair in enumerate(pairs) if pair[0]==i]
                ea=np.linalg.norm(a[rows]);eb=np.linalg.norm(b[i])
                if ea and eb:
                    s=np.sqrt(eb/ea);a[rows]*=s;b[i]/=s
            for k in range(4):
                rows=[r for r,pair in enumerate(pairs) if pair[1]==k]
                ea=np.linalg.norm(a[rows]);ec=np.linalg.norm(c[:,k])
                if ea and ec:
                    s=np.sqrt(ec/ea);a[rows]*=s;c[:,k]/=s
        out=[a,b.reshape(16,18),c.reshape(16,18)]
        norms=np.array([np.linalg.norm(x) for x in out]);common=np.exp(np.mean(np.log(norms)))
        return [m*(common/n) for m,n in zip(out,norms)]
    
    layouts=[]
    for axis in range(3):
        other=[i for i in range(3) if i!=axis]
        layouts.append((other,np.transpose(source,(axis,*other)),np.transpose(target,(axis,*other)).reshape(target.shape[axis],-1)))
    started=time.monotonic();best=float('inf');history=[];ridges=[None]*3
    for step in range(ITERATIONS+1):
        if step%50==0 or step==ITERATIONS:
            actual=np.einsum('is,jt,ku,stu->ijk',*maps,source,optimize=True);err=actual-target
            relative=float(np.linalg.norm(err)/np.sqrt(48))
            record={'iteration':step,'relative_full_coefficient_error':relative,'maximum_coefficient_error':float(np.max(np.abs(err))),'map_norms':[float(np.linalg.norm(m)) for m in maps],'map_smallest_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],'ridge_parameters':ridges.copy(),'elapsed_seconds':time.monotonic()-started}
            history.append(record);print(json.dumps(record),flush=True)
            if relative<best:
                best=relative;PREFIX.with_name(PREFIX.name+'-checkpoint.json').write_text(json.dumps({'source':'reduced endpoint corner R','source_dimensions':[16,18,18],'target':'M4 with diagonal A entries deleted','target_dimensions':[12,16,16],'target_A_pairs':pairs,'seed':SEED,'iteration':step,'auxiliary_rank':0,'norm_budget':BUDGET,'maps_real':[m.real.tolist() for m in maps],'maps_imag':[m.imag.tolist() for m in maps],'relative_full_coefficient_error':relative,'exact_coefficient_certificate':False},separators=(',',':'))+'\n')
            if relative<1e-12 or not np.isfinite(relative):break
        if step==ITERATIONS:break
        for axis,(other,st,wanted) in enumerate(layouts):
            env=np.einsum('jt,ku,stu->sjk',maps[other[0]],maps[other[1]],st,optimize=True).reshape(source.shape[axis],-1)
            gram=env@env.conj().T;cross=wanted@env.conj().T
            grams=np.broadcast_to(gram,(target.shape[axis],*gram.shape))
            maps[axis],ridges[axis]=bounded_step(grams,cross,BUDGET)
        if step%10==0:maps=gauge(maps)
        else:
            ns=np.array([np.linalg.norm(m) for m in maps]);common=np.exp(np.mean(np.log(ns)))
            maps=[m*(common/n) for m,n in zip(maps,ns)]
    result={'source':'reduced endpoint corner R','target':'M4 with diagonal A entries deleted','source_nonzero_terms':90,'all_target_positions_checked':3072,'target_nonzero_terms':48,'auxiliary_rank':0,'seed':SEED,'maximum_iterations':ITERATIONS,'iterations_completed':step,'actual_stop_reason':'iteration_budget' if step==ITERATIONS else ('coefficient_tolerance' if np.isfinite(best) and best<1e-12 else 'nonfinite'),'norm_budget':BUDGET,'target_gauge':'diagonal physical outer factors and full middle GL4','history':history,'best_relative_full_coefficient_error':best,'exact_coefficient_certificate':False,'restriction_proved':False,'improves_omega':False}
    PREFIX.with_name(PREFIX.name+'-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='history'},indent=2))
    return result


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=202610454)
    parser.add_argument('--iterations',type=int,default=1500)
    parser.add_argument('--norm-budget',type=float,default=20.0)
    parser.add_argument('--prefix',type=Path,required=True)
    args=parser.parse_args()
    run(args.seed,args.iterations,args.norm_budget,args.prefix)
