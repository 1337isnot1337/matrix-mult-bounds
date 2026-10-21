"""Exact boundary-hyperplane obstruction and rank-one-free slice span."""
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

def encode(M):
    return {'shape':list(M.shape),'entries':[[i,j,int(v.p),int(v.q)] for (i,j),v in sorted(M.todok().items()) if v]}

def decode(data):
    return sp.MutableSparseMatrix(*data['shape'],{(i,j):sp.Rational(n,q) for i,j,n,q in data['entries']})


def obstruction_chain(M,old):
    E=M;rounds=[]
    while E.todok():
        forms=[];indices={};positions=defaultdict(list)
        table=[[0]*12 for _ in range(200)];byrow=defaultdict(dict)
        for (i,j),value in E.todok().items():byrow[i][j]=value
        for flat,row in sorted(byrow.items()):
            form=old.primitive_form(row)
            if form not in indices:indices[form]=len(indices)+1;forms.append(form)
            index=indices[form];column,row=divmod(flat,200)
            table[row][column]=index;positions[index].append((row,column))
        chosen=[];records=[]
        for index,form in enumerate(forms,1):
            witness=old.triangular_witness(table,positions[index],size=2)
            if witness is None:continue
            scales=[]
            for k,(row,column) in enumerate(witness):
                j,value=form[0];scale=E[200*column+row,j]/value
                expected=sp.Matrix(1,E.cols,lambda _,j:scale*dict(form).get(j,0))
                if not scale or E[200*column+row,:]!=expected:raise ArithmeticError('wrong repeated form')
                scales.append(scale)
                for _,future in witness[k+1:]:
                    if E[200*future+row,:].todok():raise ArithmeticError('wrong triangular zero')
            chosen.append(form)
            records.append({'positions':[list(p) for p in witness],
                            'linear_form':[list(p) for p in form],
                            'determinant_ratio':str(sp.prod(scales))})
        if not chosen:raise ArithmeticError('rank-one obstruction cover incomplete')
        constraints=sp.MutableSparseMatrix(len(chosen),E.cols,{(i,j):v for i,row in enumerate(chosen) for j,v in row})
        kernel,_=old.normal.sparse_nullspace(constraints)
        rounds.append({'parameter_dimension':E.cols,'forced_rank':E.cols-kernel.cols,
                       'kernel':encode(kernel),'minors':records})
        E=E*kernel
    sharp=None
    for column in range(M.cols):
        X=sp.Matrix(200,12,lambda a,b:M[200*b+a,column])
        if len(X.to_DM().rref()[1])==2:sharp=column;break
    if sharp is None:raise ArithmeticError('sharp obstruction control missing')
    return {'matrix_shape':[200,12],'initial_parameter_dimension':228,
            'minimum_nonzero_rank':2,'sharp_parameter':sharp,'rounds':rounds,
            'final_matrix_zero':True,'final_parameter_dimension':E.cols}


# Certificates discovered from the exact annihilator; no minor search is needed here.
PEEL=[(0,[(0,None,1),(1,None,1),(2,None,1),(3,None,1),(7,None,1),(8,None,1)],[0,1,2,3,4,5]),
      (5,[(15,None,1),(13,None,1),(14,None,1),(11,None,1),(10,None,1),(12,None,1)],[5,3,4,1,0,2]),
      (1,[(1,None,1),(7,None,1),(5,None,1),(10,None,1),(8,None,1),(11,None,1)],[0,1,2,4,3,5]),
      (4,[(7,None,1),(10,None,1),(11,None,1),(8,None,1),(14,None,1),(9,12,-1)],[0,1,4,2,5,3]),
      (2,[(2,None,1),(4,None,1),(5,None,1),(3,None,1),(8,None,1),(9,None,1)],[0,3,1,2,4,5]),
      (3,[(5,None,1),(6,None,1),(8,None,1),(9,None,1),(12,None,1),(13,None,1)],[0,2,1,3,4,5])]


def matrix_space():
    block=json.loads((ROOT/'results/third-boundary-trap-2026-10-21/block.json').read_text())
    E=decode(block);keep=list(range(8))+list(range(12,16));entries={}
    for x in range(16):
        for parameter in range(28):
            for i,b in enumerate(keep):
                for j,c in enumerate(keep):
                    value=E[(x*16+b)*16+c,parameter]
                    if value:entries[x*28+parameter,12*i+j]=value
    span=sp.MutableSparseMatrix(448,144,entries)
    _,pivots=span.T.to_DM().rref();C=span[list(pivots),:].T
    if C.cols!=80:raise ArithmeticError('full matrix span changed')
    C0=C[[(2*i)*12+2*j for i in range(6) for j in range(6)],:]
    _,pivots=C0.to_DM().rref();basis=C0[:,list(pivots)]
    annihilator=C0.T.to_DM().nullspace().to_Matrix()
    if basis.cols!=20 or annihilator.rows!=16:raise ArithmeticError('reduced span changed')
    for a in range(2):
        for b in range(2):
            rows=[(2*i+a)*12+2*j+b for i in range(6) for j in range(6)]
            if annihilator*C[rows,:]!=sp.zeros(16,80):raise ArithmeticError('parity block not in reduced span')
    u=sp.symbols('u:6');v=sp.symbols('v:6')
    polynomials=[sp.expand(sum(row[6*i+j]*u[i]*v[j] for i in range(6) for j in range(6))) for row in annihilator.tolist()]
    previous=[];peeling=[]
    for coordinate,combinations,columns in PEEL:
        restricted=[f.subs({u[i]:0 for i in previous}) for f in polynomials]
        equations=[restricted[i]+(k*restricted[j] if j is not None else 0) for i,j,k in combinations]
        matrix=sp.Matrix([[sp.expand(f).coeff(v[j]) for j in columns] for f in equations])
        for i in range(6):
            if matrix[i,i] not in [u[coordinate],-u[coordinate]]:raise ArithmeticError('peeling diagonal changed')
            for j in range(i+1,6):
                if matrix[i,j]!=0:raise ArithmeticError('peeling triangular zero changed')
        ratio=sp.prod(matrix[i,i]/u[coordinate] for i in range(6))
        peeling.append({'forced_u_coordinate':coordinate,'previous_zero_coordinates':previous[:],
                        'equation_combinations':[list(c) for c in combinations],
                        'v_column_order':columns,'determinant_ratio':str(ratio)})
        previous.append(coordinate)
    if sorted(previous)!=list(range(6)):raise ArithmeticError('peeling misses a coordinate')
    return {'full_matrix_shape':[12,12],'full_space_dimension':80,
            'reduced_matrix_shape':[6,6],'reduced_space_dimension':20,
            'factorization':'reduced matrix space tensor Mat2',
            'full_space_basis':encode(C),'reduced_space_basis':encode(basis),
            'annihilators':encode(annihilator),'triangular_peeling':peeling,
            'no_nonzero_rank_one_matrix':True,
            'arbitrary_two_hyperplane_kernel_dimension_at_most':5,
            'minimum_projected_first_rank_if_nonzero_normal':3,
            'scope':'Exact identities over Q; implications hold over C. Compression bound uses the written general lemma.'}


def compression_control():
    # A sharp control for the general lemma: skew6 tensor Mat2.
    matrices=[]
    for i in range(6):
        for j in range(i+1,6):
            skew=sp.zeros(6);skew[i,j]=1;skew[j,i]=-1
            for a in range(2):
                for b in range(2):
                    unit=sp.zeros(2);unit[a,b]=1
                    matrices.append(sp.kronecker_product(skew,unit))
    retained=list(range(1,12))
    original=sp.Matrix.vstack(*(sp.Matrix(1,144,list(M)) for M in matrices))
    projected=sp.Matrix.vstack(*(sp.Matrix(1,121,list(M.extract(retained,retained))) for M in matrices))
    before=len(original.to_DM().rref()[1]);after=len(projected.to_DM().rref()[1])
    if (before,after)!=(60,55):raise ArithmeticError('sharp compression control changed')
    return {'base_space':'skew-symmetric6-by6 matrices','auxiliary_matrix_dimension':2,
            'full_matrix_shape':[12,12],'space_dimension':before,
            'projected_matrix_shape':[11,11],'projected_dimension':after,
            'compression_kernel_dimension':before-after,
            'scope':'Sharp general compression-lemma control, not a source degeneration or an assertion of sharpness for its specific80-dimensional space.'}


@lru_cache(None)
def reports():
    old=load(ROOT/'research/ai/2026-10-21-moving-boundary-flags/minimum_rank.py','hyperplane_previous_minors')
    data=old.normal.data()
    return {'boundary_obstruction':{side:obstruction_chain(data[key][:2400,:],old)
                for side,key in [('B','left_obstruction'),('C','right_obstruction')]},
            'matrix_space':matrix_space(),'compression_control':compression_control()}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,report in reports().items():
        (args.output_dir/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')
        print(name,'written',flush=True)
