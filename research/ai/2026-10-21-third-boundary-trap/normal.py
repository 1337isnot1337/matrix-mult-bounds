"""Normal lemma for boundary first frames, at an arbitrary formal order."""
from functools import lru_cache
import importlib.util
from pathlib import Path
import sympy as sp

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

folder=Path(__file__).resolve().parents[1]
normal=load(folder/'2026-10-21-moving-boundary-flags/normal_directions.py','third_previous_normal')
minor_tools=load(folder/'2026-10-21-corrected-prolongation/linear.py','third_primal_minors')

def sparse(matrix):
    return {'shape':list(matrix.shape),'entries':[[i,j,int(value.p),int(value.q)]
            for (i,j),value in sorted(matrix.todok().items()) if value]}

@lru_cache(None)
def calculate():
    m=normal.extension;data=normal.data();NF=data['first_kernel']
    assert all(set(row).issubset(set().union(*(set(x) for x in m.EB[:16]))) for row in data['E_B_complement'][:12])
    for key,basis in [('E_B_complement',m.EB),('E_C_complement',m.EC)]:
        if m.rational_rank(normal.row_matrix(m.G+data[key][:12]))!=16:
            raise ArithmeticError('boundary complement is incomplete')
        if any(set(row)-set().union(*(set(x) for x in basis[:16])) for row in data[key][:12]):
            raise ArithmeticError('complement includes a mixed row')
    constraints=data['left_obstruction'][:2400,:].col_join(data['right_obstruction'][:2400,:])
    small,_=normal.sparse_nullspace(constraints);assert small.cols==28
    Dnormal=NF*small;D=sp.zeros(896,28)
    for i,row in enumerate(normal.NORMAL):D[row,:]=Dnormal[i,:]
    operator=data['operator'];Yflat=sp.kronecker_product(sp.eye(64),data['recover'])*operator[:,normal.NORMAL]*Dnormal
    Y=[sp.Matrix(64,28,lambda x,j:Yflat[12*x+k,j]) for k in range(12)]
    identity=[{i:1} for i in range(112)];P=[D[112*b:112*(b+1),:] for b in range(4)];Q=[D[448+112*c:448+112*(c+1),:] for c in range(4)]
    
    def solve_normal(C,R,side):
     cols=[i for i in range(112) if (i//28 if side=='B' else i//7%4) in [1,2]]
     _,rr=C[:,cols].T.to_DM().rref();rr=list(rr);assert len(rr)==56
     out=sp.zeros(112,R.cols);values=C.extract(rr,cols).inv()*R[rr,:]
     for i,col in enumerate(cols):out[col,:]=values[i,:]
     assert C*out==R
     return out
    
    B2=[];C2=[]
    for side in ['B','C']:
     left=side=='B';basis=m.EB[:16] if left else m.EC[:16];base=data['left_constraints' if left else 'right_constraints']
     raw=m.contract(basis,identity,normal.KERNEL) if left else m.contract(identity,basis,normal.KERNEL)
     old=m.contract(basis,m.G,m.A0) if left else m.contract(m.G,basis,m.A0)
     for j in range(16):
      R=m.sp.zeros(256,28)
      for c in range(4):
       M=raw[:,112*j:112*(j+1)] if left else raw[:,[u*16+j for u in range(112)]]
       part=M*(Q[c] if left else P[c])
       for k in range(12):
        coefficient=old[k,j*4+c] if left else old[k,c*16+j]
        if coefficient:part-=coefficient*Y[k]
       for x in range(64):R[4*x+c,:]=-part[x,:]
      (B2 if left else C2).append(solve_normal(base,R,side))
    
    first=[m.index(i,j,z) for i in [1,2] for j in [1,2] for z in m.LONG]
    positions=[normal.KERNEL.index(a) for a in first]
    Ynew=[M[positions,:] for M in Y];entries={}
    # Contract each of28 coefficient directions from the full source, then assemble.
    F0=m.contract(m.EB[:16],m.EC[:16],m.A0)
    for parameter in range(28):
     b=[{i:M[i,parameter] for i in range(112) if M[i,parameter]} for M in B2]
     c=[{i:M[i,parameter] for i in range(112) if M[i,parameter]} for M in C2]
     Yp=sp.Matrix(16,12,lambda x,k:Ynew[k][x,parameter])
     R=m.contract(b,m.EC[:16],first)+m.contract(m.EB[:16],c,first)-Yp*F0
     for (i,j),value in R.todok().items():
      if value:entries[i*256+j,parameter]=value
    E=sp.MutableSparseMatrix(4096,28,entries);assert m.rational_rank(E)==24
    kernel,_=normal.sparse_nullspace(E);assert kernel.cols==4
    remaining=Dnormal*kernel
    plane=sp.Matrix.hstack(*(sp.Matrix([row.get(j,0) for row in rows for j in range(112)]) for rows in normal.plane_directions()))[normal.NORMAL,:]
    assert m.rational_rank(remaining.row_join(plane))==4
    if E*kernel!=sp.zeros(4096,4):raise ArithmeticError('plane kernel mismatch')
    if data['first_constraints']*Dnormal!=sp.zeros(256,28):
        raise ArithmeticError('first normal equations failed')
    for a,b,c in __import__('itertools').product(range(16),range(4),range(16)):
        if E[(a*16+4+b)*16+c,:]!=E[(a*16+8+b)*16+c,:]:raise ArithmeticError('B radical failed')
        if E[(a*16+c)*16+4+b,:]!=E[(a*16+c)*16+8+b,:]:raise ArithmeticError('C radical failed')
    FB=[{m.index(i,j,z):1} for i in (0,3) for j in range(4) for z in range(7)]
    FC=[{m.index(i,j,z):1} for i in range(4) for j in (0,3) for z in range(7)]
    if m.contract(FB,m.EC[:16],first)!=sp.zeros(16,56*16):raise ArithmeticError('B boundary freedom matters')
    if m.contract(m.EB[:16],FC,first)!=sp.zeros(16,16*56):raise ArithmeticError('C boundary freedom matters')
    if constraints*small!=sp.zeros(constraints.rows,28):raise ArithmeticError('prolongation kernel failed')
    control_parameter=next(j for j in range(28) if E[:,j].todok() and Yflat[:,j].todok())
    control={'parameter':control_parameter,
             'leading_B':sparse(D[:448,control_parameter].reshape(4,112)),
             'leading_C':sparse(D[448:,control_parameter].reshape(4,112)),
             'B_corrections':sparse(sp.Matrix(16,112,lambda row,col:B2[row][col,control_parameter])),
             'C_corrections':sparse(sp.Matrix(16,112,lambda row,col:C2[row][col,control_parameter])),
             'source_correction':sparse(sp.Matrix(64,12,lambda x,k:Yflat[12*x+k,control_parameter])),
             'K_inf_indices':normal.KERNEL,'A0_indices':m.A0}
    report={'normal_first_parameters':228,'boundary_prolonged_parameters':28,
            'boundary_prolongation_rank':minor_tools.minor(constraints,200),
            'normal_basis_independence':minor_tools.minor(Dnormal,28),
            'third_block_coefficient_rank':minor_tools.minor(E,24),
            'remaining_normal_parameters':4,'common_plane_independence':minor_tools.minor(plane,4),
            'remaining_directions_are_common_plane':True,'four_fixed_radicals_each_side':True,
            'free_boundary_coefficients_annihilate_new_block':True,
            'source_first_indices':first,'normal_basis':sparse(Dnormal),'plane_kernel':sparse(kernel),
            'plane_directions':sparse(plane),'proof_status':'Written and unreviewed; no exponent improvement.'}
    report['coefficient_control']=control
    block=sparse(E);block['source_first_indices']=first
    return report,block
