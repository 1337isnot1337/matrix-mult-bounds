"""Exact polynomial structure of the third block and asymmetric boundary trap."""
from collections import defaultdict
from functools import lru_cache
import argparse
import importlib.util
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


@lru_cache(None)
def previous_minors():
    return load(ROOT/'research/ai/2026-10-21-moving-boundary-flags/minimum_rank.py','biform_previous_minors')


def encode(M):
    return {'shape':list(M.shape),'entries':[[i,j,int(v.p),int(v.q)] for (i,j),v in sorted(M.todok().items()) if v]}


def decode(data):
    return sp.MutableSparseMatrix(*data['shape'],{(i,j):sp.Rational(n,q) for i,j,n,q in data['entries']})


def repeated_minors(M,rows,columns,size,column_order,old):
    E=M;rounds=[]
    def flat(i,j):return j*rows+i if column_order else i*columns+j
    while E.todok():
        forms=[];indices={};positions=defaultdict(list);table=[[0]*columns for _ in range(rows)]
        byrow=defaultdict(dict)
        for (i,j),value in E.todok().items():byrow[i][j]=value
        for position,row in sorted(byrow.items()):
            form=old.primitive_form(row)
            if form not in indices:indices[form]=len(indices)+1;forms.append(form)
            index=indices[form]
            if column_order:column,row=divmod(position,rows)
            else:row,column=divmod(position,columns)
            table[row][column]=index;positions[index].append((row,column))
        chosen=[];records=[]
        for index,form in enumerate(forms,1):
            witness=old.triangular_witness(table,positions[index],size=size)
            if witness is None:continue
            scales=[]
            for k,(row,column) in enumerate(witness):
                j,value=form[0];scale=E[flat(row,column),j]/value
                expected=sp.Matrix(1,E.cols,lambda _,j:scale*dict(form).get(j,0))
                if not scale or E[flat(row,column),:]!=expected:raise ArithmeticError('repeated form mismatch')
                scales.append(scale)
                for _,future in witness[k+1:]:
                    if E[flat(row,future),:].todok():raise ArithmeticError('triangular zero mismatch')
            records.append({'positions':[list(p) for p in witness],
                            'linear_form':[list(p) for p in form],
                            'determinant_ratio':str(sp.prod(scales))});chosen.append(form)
        if not chosen:raise ArithmeticError('minor cover incomplete')
        R=sp.MutableSparseMatrix(len(chosen),E.cols,{(i,j):value for i,row in enumerate(chosen) for j,value in row})
        K,_=old.normal.sparse_nullspace(R)
        rounds.append({'parameter_dimension':E.cols,'forced_linear_rank':E.cols-K.cols,
                       'minors':records,'kernel':encode(K)})
        E=E*K
    return {'matrix_shape':[rows,columns],'minor_size':size,'vectorization':'column' if column_order else 'row',
            'initial_parameter_dimension':M.cols,'rounds':rounds,
            'final_parameter_dimension':E.cols,'final_matrix_zero':True}


def biform_structure():
    previous=json.loads((ROOT/'results/boundary-hyperplanes-2026-10-21/matrix_space.json').read_text())
    S=decode(previous['reduced_space_basis']);x,y=sp.symbols('x y')
    A=[1,-y,y-x,-y*y+x*y,-x*y,x*y*y]
    B=[1,x,y-x,x*y-x*x,-x*y,-x*x*y]
    monU=[1,x,y,x*y,y*y,x*y*y];monV=[1,x,x*x,y,x*y,x*x*y]
    monOut=[x**i*y**j for i in range(4) for j in range(4)]
    def coeff(f,mon):return [sp.Poly(f,x,y).coeff_monomial(m) for m in mon]
    AU=sp.Matrix([coeff(f,monU) for f in A]);BV=sp.Matrix([coeff(f,monV) for f in B])
    multiplication=sp.Matrix.hstack(*(sp.Matrix(coeff(a*b,monOut)) for a in A for b in B))
    if AU.det()!=1 or BV.det()!=1:raise ArithmeticError('biform basis change is not unimodular')
    if multiplication*S!=sp.zeros(16,20) or len(multiplication.to_DM().rref()[1])!=16:
        raise ArithmeticError('biform product kernel changed')
    block=json.loads((ROOT/'results/third-boundary-trap-2026-10-21/block.json').read_text())
    E=decode(block);keep=list(range(8))+list(range(12,16))
    core=E[[((k*16+keep[2*b+1])*16+keep[2*c+1]) for k in range(4) for b in range(6) for c in range(6)],:]
    for a in range(16):
        short_i=a//8;short_s=a//4%2;long=a%4
        for b in range(12):
            for c in range(12):
                got=E[(a*16+keep[b])*16+keep[c],:]
                expected=core[(long*6+b//2)*6+c//2,:] if (b%2,c%2)==(1-short_s,1-short_i) else sp.zeros(1,28)
                if got!=expected:raise ArithmeticError('tensor product factorization changed')
    for k in range(4):
        if multiplication*core[36*k:36*(k+1),:]!=sp.zeros(16,28):raise ArithmeticError('core leaves product kernel')
    if len(core.to_DM().rref()[1])!=24:raise ArithmeticError('core coefficient rank changed')
    normal=json.loads((ROOT/'results/third-boundary-trap-2026-10-21/normal.json').read_text())
    plane=decode(normal['plane_kernel'])
    if core*plane!=sp.zeros(144,4) or len(plane.to_DM().rref()[1])!=4:
        raise ArithmeticError('core kernel is not the common plane')
    operator=multiplication[:,[6*k for k in range(6)]].row_join(multiplication[:,list(range(6))])
    K=operator.to_DM().nullspace().to_Matrix().T
    images=sp.Matrix.hstack(*(sp.Matrix(36,1,lambda flat,_:
        (K[flat//6,k] if flat%6==0 else 0)+(K[6+flat%6,k] if flat//6==0 else 0)) for k in range(K.cols)))
    if K.cols!=4 or len(images.to_DM().rref()[1])!=3:raise ArithmeticError('sharp specific compression control changed')
    return {'U_bidegree':[1,2],'V_bidegree':[2,1],'output_bidegree':[3,3],
            'U_basis':[str(a) for a in A],'V_basis':[str(b) for b in B],
            'U_basis_change':encode(AU),'V_basis_change':encode(BV),
            'U_basis_determinant':1,'V_basis_determinant':1,
            'multiplication':encode(multiplication),'kernel_dimension':20,
            'core':encode(core),'core_shape':[4,6,6],'coefficient_dimension':24,
            'tensor_product_auxiliary_dimensions':[4,2,2],'tensor_factorization_all_coefficients':True,
            'specific_two_hyperplane_kernel_ceiling':3,'sharp_compression_kernel_dimension':3,
            'pair_syzygy_kernel':encode(K),'pair_syzygy_matrix_images':encode(images),
            'scope':'Exact identities over Q; the bound3 uses the written bihomogeneous gcd argument.'}


def conditioned_obstructions(old):
    data=old.normal.data();B=data['left_obstruction'][:2400,:];C=data['right_obstruction'][:2400,:];out={}
    for side,full,remaining in [('C',B,C),('B',C,B)]:
        K,_=old.normal.sparse_nullspace(full)
        if K.cols!=100:raise ArithmeticError('full-side kernel changed')
        M=remaining*K;chain=repeated_minors(M,200,12,4,True,old)
        if [r['forced_linear_rank'] for r in chain['rounds']]!=[56,14,2]:raise ArithmeticError('conditioned minor ranks changed')
        sharp=next((j for j in range(M.cols) if len(sp.Matrix(200,12,lambda a,b:M[200*b+a,j]).to_DM().rref()[1])==4),None)
        if sharp is None:raise ArithmeticError('sharp conditioned rank4 control missing')
        out[side]={'other_side_full_boundary_kernel':encode(K),'minimum_nonzero_conditioned_rank':4,
                   'sharp_parameter':sharp,'chain':chain}
    return out


def puncture_control():
    Z=[]
    for i in [1,2]:
        M=sp.zeros(3);M[0,i]=1;M[i,0]=-1;Z.append(M)
    matrices=[]
    for M in Z:
        for a in range(2):
            for b in range(2):
                unit=sp.zeros(2);unit[a,b]=1;matrices.append(sp.kronecker_product(M,unit))
    before=sp.Matrix.vstack(*(sp.Matrix(1,36,list(M)) for M in matrices))
    images=[M.extract(range(1,6),[3,4,5]) for M in matrices]
    after=sp.Matrix.vstack(*(sp.Matrix(1,15,list(M)) for M in images))
    if len(before.to_DM().rref()[1])!=8 or len(after.to_DM().rref()[1])!=3:raise ArithmeticError('sharp puncture control changed')
    both_two=[M.extract(range(2,6),range(2,6)) for M in matrices]
    if any(M.todok() for M in both_two):raise ArithmeticError('two-by-two loss counterexample changed')
    return {'base_space':'span of E01-E10 and E02-E20 in Mat3',
            'base_space_dimension':2,'minimum_nonzero_base_matrix_rank':2,
            'auxiliary_matrix_dimension':2,'original_first_rank':8,
            'projection_kernel_dimensions':[1,3],'projected_first_rank':3,
            'projected_matrices':[encode(M) for M in images],
            'two_by_two_loss_counterexample_first_rank':0,
            'scope':'Sharp general puncture-lemma control, not a matrix-target source degeneration.'}


@lru_cache(None)
def reports():
    old=previous_minors()
    structure=biform_structure();core=decode(structure['core'])
    minimum=repeated_minors(core,4,36,2,False,old)
    if minimum['final_parameter_dimension']!=4:raise ArithmeticError('core does not have plane kernel4')
    sharp=next((j for j in range(28) if len(sp.Matrix(4,36,lambda a,b:core[36*a+b,j]).to_DM().rref()[1])==2),None)
    if sharp is None:raise ArithmeticError('sharp core rank2 control missing')
    minimum['minimum_nonzero_first_rank']=2;minimum['sharp_parameter']=sharp
    return {'structure':structure,'core_minimum':minimum,
            'conditioned_obstructions':conditioned_obstructions(old),'puncture_control':puncture_control()}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,report in reports().items():
        (args.output_dir/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n');print(name,'written',flush=True)
