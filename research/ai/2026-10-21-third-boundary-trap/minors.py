"""Repeated-minor certificate for the forced third-order first flattening."""
from collections import defaultdict
import importlib.util
from pathlib import Path
import sympy as sp

folder=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('third_previous_minors',folder/'2026-10-21-moving-boundary-flags/minimum_rank.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)


def calculate(E,minor_tools):
    _,pivots=E.to_DM().rref();pivots=list(pivots)
    if len(pivots)!=24:raise ArithmeticError('third block coefficient dimension changed')
    C=E[:,pivots];byrow=defaultdict(dict)
    for (i,j),value in C.todok().items():byrow[i][j]=value
    forms=[];indices={};positions=defaultdict(list);table=[[0]*256 for _ in range(16)]
    for flat in sorted(byrow):
        form=old.primitive_form(byrow[flat])
        if not form:continue
        if form not in indices:indices[form]=len(forms)+1;forms.append(form)
        index=indices[form];a,col=divmod(flat,256);table[a][col]=index;positions[index].append((a,col))
    chosen=[];minors=[]
    for index,form in enumerate(forms,1):
        witness=old.triangular_witness(table,sorted(positions[index]),size=8)
        if witness is None:continue
        scales=[]
        for k,(row,col) in enumerate(witness):
            diagonal={j:C[row*256+col,j] for j in range(C.cols) if C[row*256+col,j]}
            if old.primitive_form(diagonal)!=form:raise ArithmeticError('diagonal form mismatch')
            j,value=form[0];scales.append(diagonal[j]/value)
            for _,future in witness[k+1:]:
                if C[row*256+future,:]!=sp.zeros(1,C.cols):raise ArithmeticError('triangular zero failed')
        constant=sp.prod(scales)
        minors.append({'positions':[list(pair) for pair in witness],
                       'linear_form':[list(pair) for pair in form],
                       'determinant_constant':[int(constant.p),int(constant.q)]})
        chosen.append(form)
    constraints=sp.MutableSparseMatrix(len(chosen),24,{(i,j):value for i,row in enumerate(chosen) for j,value in row})
    if constraints.to_DM().nullspace().shape[0]:raise ArithmeticError('repeated minors do not force zero')
    sharp=None
    for column in range(C.cols):
        M=sp.Matrix(16,256,lambda i,j:C[i*256+j,column])
        if old.normal.extension.rational_rank(M)==8:
            sharp={'coefficient_parameter':pivots[column],'first_flattening_rank':8,
                   'minor':minor_tools.minor(M,8)};break
    if sharp is None:raise ArithmeticError('sharp rank-eight control missing')
    return {'coefficient_parameter_columns':pivots,'initial_parameter_dimension':24,
            'matrix_shape':[16,256],'minimum_nonzero_first_rank':8,'minors':minors,
            'forced_linear_rank':minor_tools.minor(constraints,24),
            'all_forced_zero_after_one_round':True,'sharp_control':sharp,
            'scope':'Exact determinant identities c*L^8 over Q; the rank implication holds over C.'}
