"""Exact corrected prolongation with fixed boundary first-row frames."""
from functools import lru_cache
import importlib.util
from pathlib import Path
import sympy as sp

folder=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('canonical_extensions',folder/'2026-10-21-quantum-extension-spaces/extensions.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
spec=importlib.util.spec_from_file_location('prolongation_minor_tools',folder/'2026-10-20-graded-quantum-flags/one_leg.py')
one=importlib.util.module_from_spec(spec);spec.loader.exec_module(one)


def sparse(matrix):
    return {'shape':list(matrix.shape),'entries':[[i,j,int(value.p),int(value.q)]
            for (i,j),value in sorted(matrix.todok().items()) if value]}


def minor(matrix,expected):
    rows=[{} for _ in range(matrix.rows)];p=one.PRIME
    for (i,j),value in matrix.todok().items():
        v=int(value.p)*pow(int(value.q),-1,p)%p
        if v:rows[i][j]=v
    rr,cc=one.independent_minor(rows)
    if len(rr)!=expected:raise ArithmeticError('unexpected modular lower rank')
    determinant=one.determinant_mod([[rows[i].get(j,0) for j in cc] for i in rr])
    if not determinant:raise ArithmeticError('zero selected minor')
    return {'rank_lower_bound':expected,'minor_rows':rr,'minor_columns':cc,
            'minor_determinant_mod_prime':determinant}


@lru_cache(None)
def calculate():
    first,cb,cc,H,top,ann=m.matrices()
    N=top.to_DM().nullspace().to_Matrix().T
    if N.shape!=(896,532):raise ArithmeticError('canonical first-jet dimension changed')
    identity=[{i:1} for i in range(112)]
    left=m.contract(identity,m.G,m.OUTSIDE);right=m.contract(m.G,identity,m.OUTSIDE)
    P=[N[112*b:112*(b+1),:] for b in range(4)]
    Q=[N[448+112*c:448+112*(c+1),:] for c in range(4)]
    @lru_cache(None)
    def rhs(position):
        b,c=divmod(position,4)
        return left[:,list(range(c,448,4))]*P[b]+right[:,112*b:112*(b+1)]*Q[c]
    F=first.extract(m.A0,list(range(16)));_,pc=F.to_DM().rref();pc=list(pc)
    inverse=F[:,pc].inv()
    Y=[sum((inverse[j,k]*rhs(c) for j,c in enumerate(pc) if inverse[j,k]),sp.zeros(100,532))
       for k in range(12)]
    for position in range(16):
        expected=sum((F[k,position]*Y[k] for k in range(12) if F[k,position]),sp.zeros(100,532))
        if rhs(position)!=expected:raise ArithmeticError('first-row correction mismatch')
    constraints=[]
    for side,Cbase,newfirst,variable in [('left',cb,m.EB[:16],Q),('right',cc,m.EC[:16],P)]:
        cokernel=Cbase.T.to_DM().nullspace().to_Matrix()
        if cokernel.shape!=(308,400):raise ArithmeticError('extension cokernel dimension changed')
        pieces=[cokernel[:,list(range(c,400,4))] for c in range(4)]
        data=m.contract(newfirst,identity,m.OUTSIDE) if side=='left' else m.contract(identity,newfirst,m.OUTSIDE)
        small=m.contract(newfirst,m.G,m.A0) if side=='left' else m.contract(m.G,newfirst,m.A0)
        @lru_cache(None)
        def corrected(c,k):return pieces[c]*Y[k]
        for j in range(16):
            M=data[:,112*j:112*(j+1)] if side=='left' else data[:,[b*16+j for b in range(112)]]
            R=sum((pieces[c]*M*variable[c] for c in range(4)),sp.zeros(308,532))
            D=sp.Matrix(12,4,lambda k,c:small[k,j*4+c] if side=='left' else small[k,c*16+j])
            R-=sum((D[k,c]*corrected(c,k) for k,c in D.todok() if D[k,c]),sp.zeros(308,532))
            constraints.append(sp.SparseMatrix(R))
    stack=sp.SparseMatrix.vstack(*constraints)
    null=stack.to_DM().nullspace().to_Matrix().T
    actual=N*null
    if null.cols!=172 or stack*null!=sp.zeros(stack.rows,172) or top*actual!=sp.zeros(400,172):
        raise ArithmeticError('prolongation upper certificate failed')
    outside=[]
    for leg in range(2):
        for row in range(4):
            for old in range(112):
                i,j=old//28,old//7%4
                if (i if leg==0 else j) not in [0,3]:outside.append(leg*448+row*112+old)
    departure=actual[outside,:];_,departure_columns=departure.to_DM().rref()
    if len(departure_columns)!=28:raise ArithmeticError('unexpected boundary departure dimension')
    report={'first_parameters':532,'prolonged_parameters':172,'leading_boundary_departure_rank':28,
            'corrected_equation_count':stack.rows,'nonzero_constraint_coefficients':len(stack.todok()),
            'prolongation_lower_certificate':minor(stack,360),
            'parameter_basis_independence_certificate':minor(actual,172),
            'departure_lower_certificate':minor(departure,28),
            'first_row_correction_identities_checked':16,
            'all_first_and_off_diagonal_coefficient_identities':True,
            'scope':'Fixed DB/DC outside first-row frames; complete corrected second-order off-diagonal equations. No matrix tensor limit.'}
    basis=sparse(actual);basis['departure_columns']=list(departure_columns)
    return report,basis
