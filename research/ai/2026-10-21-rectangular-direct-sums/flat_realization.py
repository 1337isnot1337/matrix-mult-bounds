"""Exact sufficient flatness test, not a classification of all finite sequences."""
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix


def pivots(M):
    return list(DomainMatrix.from_Matrix(M).convert_to(s.QQ).rref()[1])


def hankel(moments, rows, cols):
    return s.BlockMatrix([[moments[p+q] for q in range(cols)]
                         for p in range(rows)]).as_explicit()


def realize(moments, rows, cols):
    """Return a verified rational realization if the inner block is flat."""
    if rows<2 or cols<2 or len(moments)!=rows+cols-1:
        raise ValueError('Need full moments and at least two block rows/columns')
    outdim,indim=moments[0].shape
    H=hankel(moments,rows,cols)
    inner=hankel(moments,rows-1,cols-1)
    js=pivots(inner); n=len(js)
    fullrank=len(pivots(H))
    if n!=fullrank:
        return {'flat':False,'inner_rank':n,'full_rank':fullrank}
    if not n:
        return {'flat':True,'state_dimension':0,'moments_verified':len(moments)}
    ii=pivots(inner[:,js].T)
    # Inner columns use the same q-major indexing as the complete matrix.
    minor=H.extract(ii,js); inv=minor.inv()
    O=H[:,js]; R=inv*H[ii,:]
    assert O*R==H
    # Shift the selected block row by one, keeping the output coordinate.
    A=inv*H.extract([i+outdim for i in ii],js)
    C=O[:outdim,:]; B=R[:,:indim]
    power=s.eye(n)
    for M in moments:
        assert C*power*B==M
        power=power*A
    return {'flat':True,'state_dimension':n,'moments_verified':len(moments),
            'selected_rows':ii,'selected_columns':js,
            'state_matrix':[[str(v) for v in A.row(i)] for i in range(n)]}


def report():
    # Fully observed state: a noncyclic size-nine realization is allowed.
    A=s.diag(*range(1,8),8,8)
    C=s.zeros(10,9); B=s.zeros(9,8)
    for j in range(9):
        C[j,j]=1
        B[j,j%8]=1
    moments=[C*(A**k)*B for k in range(17)]
    regular=realize(moments,8,10)
    # A genuine nine-state sequence can fail this sufficient inner-flatness test.
    sparse=[s.zeros(10,8) for _ in range(17)]
    sparse[0][0,0]=1; sparse[7][1,1]=1
    nonflat_regular=realize(sparse,8,10)
    # The rank-eight crossed example needs at least nine states.
    central=[s.zeros(10,8) for _ in range(17)]
    central[8][0,0]=1
    nonflat_central=realize(central,8,10)
    return {'status':'sufficient flatness criterion only',
            'regular_control':regular,'nonflat_nine_state_control':nonflat_regular,
            'nonflat_central_control':nonflat_central,
            'nonflat_implies_no_realization':False,'improves_omega':False}

if __name__=='__main__':print(json.dumps(report(),indent=2))
