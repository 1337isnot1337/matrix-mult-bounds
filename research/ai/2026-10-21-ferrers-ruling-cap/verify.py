"""Independent exact controls for written Ferrers ruling and dominance bounds."""
import argparse
from functools import lru_cache
import importlib.util
from pathlib import Path
import sympy as sp


def ruling_cap(r,k):
    if r<1 or k<1:raise ValueError('Need positive r,k')
    values=[r,2*r-2*k+1]
    if r>=k*k:
        q,s=divmod(r,k);values.append(q*q+2*s)
    return max(values)


def closed_target_cap(r,k):
    if r<1 or k<1:raise ValueError('Need positive r,k')
    if r<k*(k+1):return r,'linear_space_saturation'
    q,s=divmod(r,k)
    return q*q+2*s,'nondominant_ferrers_bound'


def square_extension(r,k):
    q,s=divmod(r,k)
    if q<k:raise ValueError('Square-extension case requires r>=k^2')
    return [q+1]*s+[q]*(q-s)+([s] if s else [])


def extremizer(r,k):
    best=[r]
    if 2*r-2*k+1>sum(best):
        width=r-k+1;best=[width]+[1]*(width-1)
    if r>=k*k:
        shape=square_extension(r,k)
        if sum(shape)>sum(best):best=shape
    return best


def durfee(shape):
    return sum(width>=i+1 for i,width in enumerate(shape))


def partition_optima(r,k):
    # Enumerate complete diagrams. This does not use either closed formula
    # or the first-k-row optimization in the written proof.
    @lru_cache(None)
    def search(last,rows,top_used,left_used,nondominant):
        all_best=0;proper_best=0 if nondominant else -1
        for width in range(1,last+1):
            top_new=top_used+(width if rows<k else 0)
            left_new=left_used+min(k,width)
            if top_new>r or left_new>r:continue
            new_flag=nondominant or (rows==k and width>=k+1)
            a,b=search(width,rows+1,top_new,left_new,new_flag)
            all_best=max(all_best,width+a)
            if b>=0:proper_best=max(proper_best,width+b)
        return all_best,proper_best
    a,b=search(r,0,0,0,False)
    return a,(None if b<0 else b),search.cache_info().currsize


def ruling_budgets(shape,k):
    return sum(shape[:k]),sum(min(k,w) for w in shape)


def jacobian_control(shape,k):
    """Compute d(B(A*C)) at the leading identity factor, using rational rank."""
    u=len(shape);v=shape[0];h=min(k,durfee(shape))
    A=sp.Matrix(u,k,lambda i,t:1 if i==t and t<h else 0)
    C=sp.Matrix(k,v,lambda t,j:1 if t==j and t<h else 0)
    cells=[(i,j) for i,w in enumerate(shape) for j in range(w)]
    J=sp.zeros(len(cells),k*(u+v))
    for row,(i,j) in enumerate(cells):
        for t in range(k):
            J[row,i*k+t]=C[t,j]
            J[row,u*k+t*v+j]=A[i,t]
    rank=J.to_DM().rank()
    expected=sum(w if i<h else min(h,w) for i,w in enumerate(shape))
    assert rank==expected
    return {'shape':shape,'input_rank':k,'durfee_number':durfee(shape),
            'coefficient_dimension':len(cells),'jacobian_rank':rank,
            'dominant_on_rank_k':rank==len(cells),
            'full_rank_jacobian_iff_durfee_at_most_k':(rank==len(cells))==(durfee(shape)<=k)}


def report():
    records=[]
    for r in range(1,21):
        for k in range(1,min(r+2,8)):
            actual,nondominant,states=partition_optima(r,k)
            shape=extremizer(r,k);row,col=ruling_budgets(shape,k)
            assert actual==ruling_cap(r,k)==sum(shape) and max(row,col)<=r
            cap,method=closed_target_cap(r,k)
            if r<k*(k+1):assert nondominant is None and cap==r
            else:
                assert nondominant==cap
                other=square_extension(r,k)
                assert durfee(other)>k and sum(other)==cap
                assert max(ruling_budgets(other,k))<=r
            records.append({'r':r,'k':k,'sharp_ruling_cap':actual,
                'sharp_nondominant_ruling_cap':nondominant,'closed_target_cap':cap,
                'closed_target_method':method,'extremizing_partition':shape,
                'first_k_rows':row,'first_k_columns':col,'independent_dp_states':states})
    diagrams={(tuple(extremizer(r,k)),k) for r in range(1,13) for k in range(1,5)}
    diagrams.update((tuple(square_extension(r,k)),k) for k in range(1,4) for r in range(k*(k+1),13))
    jacobians=[jacobian_control(list(shape),k) for shape,k in sorted(diagrams)]
    return {'scope':'Finite exact controls for the written proofs; not an all-size proof or an exponent result.',
            'partition_optima':records,'ferrers_jacobians':jacobians,
            'countercontrols':{'hook_on_C4_times_C4':{'ruling_rank':2,'ruling_cap':5,
                'linear_span_dimension':7,'rank_one_image_is_dominant':True,
                'can_lie_in_closed_target_with_linear_space_cap_5':False},
                'full_M3_rank_2':{'ruling_cap':6,'input_rank':2,'dimension':9,
                    'rank_two_image_is_dominant':False,'threshold_r_less_than_k_k_plus_1':False},
                'ruling_cap_alone_does_not_imply_linear_space_saturation':True},
            'independent_review':False,'improves_omega':False}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();args.output.parent.mkdir(parents=True,exist_ok=True)
    path=Path(__file__).parents[1]/'2026-10-21-hankel-wronskian-cap/verify.py'
    spec=importlib.util.spec_from_file_location('ferrers_formatter',path)
    formatter=importlib.util.module_from_spec(spec);spec.loader.exec_module(formatter)
    result=report();formatter.write_json(args.output,result)
    print(len(result['partition_optima']),'partition optima and',len(result['ferrers_jacobians']),'exact Jacobians passed.')
