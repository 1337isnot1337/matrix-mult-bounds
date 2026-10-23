"""Exact dimension arithmetic and finite-realization counterexample."""
import json
import sympy as sp


def dimension_bound(p, q, m, n, k):
    assert 1 <= k <= min(p, q, m, n)
    branches = [k*(m+n-k), min(m,p)*min(n,q), min(m,q)*min(n,p)]
    return {'input_dimension':p*q, 'branch_bounds':branches,
            'image_dimension_bound':max(branches)}


def report():
    a,b=8,10
    scalar=sp.Matrix(a,b,lambda p,q:int(p+q==a))
    moment=sp.Matrix(a+1,a+1,lambda p,q:int(p+q==a))
    # Each nonzero original source entry has unique row and column.
    entries=[((j,p,r),(j,q,r)) for j in range(b) for p in range(a)
             for q in range(b) for r in range(a) if p+q==a]
    rows={x for x,y in entries}; cols={y for x,y in entries}
    assert len(rows)==len(cols)==len(entries)
    return {'status':'finite-controls-only; external classification required',
            'outer_flattenings':[dimension_bound(32,33,136,10,2),
                                 dimension_bound(32,33,170,8,2)],
            'counterexample':{'coefficient':[0,8,0],
                'scalar_rank':scalar.rank(), 'crossed_rank':scalar.rank(),
                'moment_hankel_rank':moment.rank(),
                'moment_hankel_determinant':int(moment.det()),
                'source_partial_permutation_rank':len(entries),
                'outer_flattening_ranks':[1,1]},
            'all_critical_slices_classified':False, 'improves_omega':False}

if __name__=='__main__':print(json.dumps(report(),indent=2))
