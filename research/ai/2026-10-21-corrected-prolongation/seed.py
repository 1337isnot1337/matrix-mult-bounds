"""Full coefficient construction of a compatible second jet."""
import itertools
import sympy as sp

def calculate(m,data,parameters):
    column={}
    for i,j,n,q in data['entries']:
     if j in parameters:column[i]=column.get(i,0)+parameters[j]*sp.Rational(n,q)
    Ptop=[{k:column[112*b+k] for k in range(112) if column.get(112*b+k,0)} for b in range(4)]
    Qtop=[{k:column[448+112*b+k] for k in range(112) if column.get(448+112*b+k,0)} for b in range(4)]
    F,cb,cc,H,top,ann=m.matrices();F0=F.extract(m.A0,list(range(16)));_,pc=F0.to_DM().rref();pc=list(pc)
    firsttop=m.contract(Ptop,m.G,range(112))+m.contract(m.G,Qtop,range(112));Y=firsttop.extract(m.OUTSIDE,pc)*F0[:,pc].inv()
    assert firsttop.extract(m.OUTSIDE,list(range(16)))==Y*F0

    def solve(M,RHS):
     R,pivots=M.row_join(RHS).to_DM().rref();R=R.to_Matrix()
     if any(i>=M.cols for i in pivots):raise ArithmeticError('inconsistent full coefficient system')
     out=sp.zeros(M.cols,RHS.cols)
     for row,col in enumerate(pivots):out[col,:]=R[row,M.cols:]
     assert M*out==RHS
     return out

    RB=sp.zeros(400,16);RC=sp.zeros(400,16)
    for j in range(16):
     raw=m.contract([m.EB[j]],Qtop,m.OUTSIDE);D=m.contract([m.EB[j]],m.G,m.A0)
     rhs=-raw+Y*D
     for x,c in itertools.product(range(100),range(4)):RB[4*x+c,j]=rhs[x,c]
     raw=m.contract(Ptop,[m.EC[j]],m.OUTSIDE);D=m.contract(m.G,[m.EC[j]],m.A0)
     rhs=-raw+Y*D
     for x,b in itertools.product(range(100),range(4)):RC[4*x+b,j]=rhs[x,b]
    B2=solve(cb,RB);C2=solve(cc,RC)
    raw=m.contract(Ptop,Qtop,m.OUTSIDE)-Y*firsttop.extract(m.A0,list(range(16)))
    rhs=-(raw*ann.T);rhs=sp.Matrix(400,1,lambda i,j:rhs[i//4,i%4]);top2=solve(top,rhs)

    def dictionary(row):return {j:value for j,value in enumerate(row) if value}
    P0=m.G+[{} for _ in range(16)];Q0=m.G+[{} for _ in range(16)]
    P1=Ptop+m.EB[:16];Q1=Qtop+m.EC[:16]
    P2=[dictionary(top2[112*b:112*(b+1),0]) for b in range(4)]+[dictionary(B2[:,j]) for j in range(16)]
    Q2=[dictionary(top2[448+112*b:448+112*(b+1),0]) for b in range(4)]+[dictionary(C2[:,j]) for j in range(16)]
    S0=m.contract(P0,Q0,range(112));S1=m.contract(P1,Q0,range(112))+m.contract(P0,Q1,range(112))
    S2=m.contract(P2,Q0,range(112))+m.contract(P1,Q1,range(112))+m.contract(P0,Q2,range(112))
    A0rows=S0.extract(m.A0,list(range(400)))
    assert S1.extract(m.OUTSIDE,list(range(400)))==Y*A0rows
    Z2=S2.extract(m.OUTSIDE,list(range(400)))-Y*S1.extract(m.A0,list(range(400)))
    padded_pc=[(i//4)*20+i%4 for i in pc]
    Z=Z2[:,padded_pc]*F0[:,pc].inv()
    assert Z2==Z*A0rows

    def sparse(matrix):return {'shape':list(matrix.shape),'entries':[[i,j,int(v.p),int(v.q)] for (i,j),v in sorted(matrix.todok().items()) if v]}
    def maps(rows):return [[i,j,int(sp.Rational(value).p),int(sp.Rational(value).q)] for i,row in enumerate(rows) for j,value in sorted(row.items())]
    report=dict(parameters=[[i,value] for i,value in sorted(parameters.items())],parameter_selection='Explicit deterministic rational assignment; not randomized.',output_dimension=110,active_output_rows_through_order_two=20,P=[maps(x) for x in [P0,P1,P2]],Q=[maps(x) for x in [Q0,Q1,Q2]],first_correction=sparse(Y),second_correction=sparse(Z),source_first_leading_indices=m.A0,source_first_kernel_indices=m.OUTSIDE,all_first_coefficients_verified=True,all_second_coefficients_verified=True,first_coefficient_entries_checked=100*20*20,second_coefficient_entries_checked=100*20*20,generic_full_rank_completion='Add t^3 times the110-by112 matrix [I110 0] to each map. Its selected110-by110 determinant has highest coefficient1; later partial-space conditions are not asserted.',scope='Complete exact second-jet witness. It supplies no matrix tensor limit or exponent improvement; all higher-order lifting conditions remain open.')
    return report
