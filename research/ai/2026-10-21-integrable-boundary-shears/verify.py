"""Exact two-parameter source fiber and complete off-origin annihilators."""
from functools import lru_cache
import argparse
import importlib.util
import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
A,B=sp.symbols('a b')
KEPT=list(range(2,16))


def extension():
    path=ROOT/'research/ai/2026-10-21-quantum-extension-spaces/extensions.py'
    spec=importlib.util.spec_from_file_location('boundary_shear_source',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


def decode(data):
    return sp.MutableSparseMatrix(*data['shape'],{(i,j):sp.Rational(n,q) for i,j,n,q in data['entries']})


def maps(rows):
    records=[]
    for i,row in enumerate(rows):
        for j,value in sorted(row.items()):
            p=sp.Poly(value,A,B);c=[p.coeff_monomial(m) for m in [1,A,B]]
            if sp.expand(value-(c[0]+c[1]*A+c[2]*B)):raise ArithmeticError('map not affine in parameters')
            if any(c):records.append([i,j,*map(int,c)])
    return records


def family(e):
    left=[dict(e.EB[j]) for j in KEPT];right=[dict(e.EC[j]) for j in KEPT]
    for j in [8,9]:
        z=e.LONG[j%4]
        for k,value in [(1,A),(2,B)]:
            left[KEPT.index(j)][e.index(k,3,z+3)]=-value
            right[KEPT.index(j)][e.index(3,k,z+3)]=value
    return left,right


def row_matrix(rows):
    return sp.MutableSparseMatrix(len(rows),112,{(i,j):value for i,row in enumerate(rows) for j,value in row.items() if value})


def selected_minor(M,rank,substitution=None):
    control=M.subs(substitution) if substitution is not None else M
    _,columns=control.to_DM().rref();columns=list(columns)
    _,rows=control[:,columns].T.to_DM().rref();rows=list(rows)
    if len(rows)!=rank or len(columns)!=rank:raise ArithmeticError('control rank changed')
    determinant=sp.factor(M.extract(rows,columns).det(method='domain-ge'))
    return {'rows':rows,'columns':columns,'determinant':str(determinant)}


def polynormal(e,left,right):
    P0=[dict(g) for g in e.G]+[{} for _ in range(14)]
    Q0=[dict(g) for g in e.G]+[{} for _ in range(14)]
    P1=[{} for _ in range(4)]+[dict(e.EB[j]) for j in KEPT]
    Q1=[{} for _ in range(4)]+[dict(e.EC[j]) for j in KEPT]
    P2=[{} for _ in range(18)];Q2=[{} for _ in range(18)]
    full=sp.zeros(896,2)
    for row,z in enumerate([1,2]):
        for k,value,column in [(1,A,0),(2,B,1)]:
            p=e.index(k,3,z+3);q=e.index(3,k,z+3)
            P1[row][p]=value;Q1[row][q]=value
            P2[4+KEPT.index(8+row)][p]=-value
            Q2[4+KEPT.index(8+row)][q]=value
            full[112*row+p,column]=1;full[448+112*row+q,column]=1
    P=[P0,P1,P2];Q=[Q0,Q1,Q2];coefficient_counts=[]
    t=sp.Symbol('t')
    for coefficients,basis,sign in [(P,left,1),(Q,right,-1)]:
        polynomial=sum((t**j*row_matrix(rows) for j,rows in enumerate(coefficients)),sp.zeros(18,112))
        expected=t*row_matrix(basis).subs({A:t*A,B:t*B},simultaneous=True)
        if any(sp.expand(value) for value in polynomial[4:,:]-expected):
            raise ArithmeticError('new rows do not equal the exact shear family')
        for row in range(4):
            first=4+KEPT.index(4+row);second=4+KEPT.index(8+row)
            if any(sp.expand(value) for value in t*polynomial[row,:]-sign*(polynomial[first,:]-polynomial[second,:])):
                raise ArithmeticError('leading row relation failed')
    if len(row_matrix(e.G).to_DM().rref()[1])!=4 or len(row_matrix(e.G+[e.EB[j] for j in KEPT]).to_DM().rref()[1])!=14:
        raise ArithmeticError('effective first rank changed')
    for degree in range(5):
        coefficient=sp.zeros(112,18*18)
        for i in range(3):
            j=degree-i
            if 0<=j<3:coefficient+=e.contract(P[i],Q[j],range(112))
        if any(sp.expand(value) for value in coefficient[e.OUTSIDE,:]):raise ArithmeticError('polynomial first-space growth')
        coefficient_counts.append(len({p:value for p,value in coefficient.todok().items() if sp.expand(value)}))
    previous=json.loads((ROOT/'results/third-boundary-trap-2026-10-21/normal.json').read_text())
    plane=decode(previous['plane_directions']);normal_indices=[112*b+j for b in range(8) for j in range(112)
        if (j//28 if b<4 else j//7%4) in [1,2]]
    combined=plane.row_join(full[normal_indices,:])
    if len(combined.to_DM().rref()[1])!=6:raise ArithmeticError('new derivatives are common-plane directions')
    return {'P':[maps(rows) for rows in P],'Q':[maps(rows) for rows in Q],
            'map_degree':2,'leading_rank_each':4,'generic_row_rank_each':14,
            'all_leading_row_relations_verified':True,
            'effective_first_quotient_dimensions':[10,10],
            'all_five_tensor_coefficients_annihilate_K':True,
            'tensor_coefficient_nonzero_counts':coefficient_counts,
            'common_plane_plus_new_normal_rank':6,
            'normal_rank_six_minor':selected_minor(combined,6),
            'source_row_corrections':'Zero at every order; the full polynomial contraction annihilates K.',
            'scope':'Exact integrable low-rank source family, not a full-rank matrix-target lift.'}


@lru_cache(None)
def reports():
    e=extension();left,right=family(e)
    baseline=e.contract([e.EB[j] for j in KEPT],[e.EC[j] for j in KEPT],range(112))
    actual=e.contract(left,right,range(112));difference=actual-baseline
    if any(sp.expand(value) for value in difference):raise ArithmeticError('source fiber identity failed')
    if baseline[e.OUTSIDE,:].todok():raise ArithmeticError('source tensor leaves A0')
    first_minor=selected_minor(baseline[e.A0,:],12)
    pivotsB=[next(iter(e.EB[j])) for j in KEPT];pivotsC=[next(iter(e.EC[j])) for j in KEPT]
    if row_matrix(left)[:,pivotsB]!=sp.eye(14) or row_matrix(right)[:,pivotsC]!=sp.eye(14):
        raise ArithmeticError('fixed source projection no longer the identity')
    identity=[{i:1} for i in range(112)];raw=e.contract(identity,right,e.OUTSIDE)
    CB=sp.MutableSparseMatrix(1400,112,{(14*x+c,j):value for (x,col),value in raw.todok().items() for j,c in [divmod(col,14)]})
    raw=e.contract(left,identity,e.OUTSIDE)
    CC=sp.MutableSparseMatrix(1400,112,{(14*x+b,j):value for (x,col),value in raw.todok().items() for b,j in [divmod(col,112)]})
    annihilators={}
    for side,M,basis,boundary in [('B',CB,left,e.EB[:16]),('C',CC,right,e.EC[:16])]:
        product=M*row_matrix(basis).T
        if any(sp.expand(value) for value in product):raise ArithmeticError('claimed kernel basis fails')
        charts=[]
        for variable,substitution,power in [(A,{A:1,B:0},2 if side=='B' else 4),(B,{A:0,B:1},2 if side=='B' else 4)]:
            witness=selected_minor(M,98,substitution)
            if sp.sympify(witness['determinant'])!=-variable**power:raise ArithmeticError('chart determinant changed')
            witness['parameter']=str(variable);witness['power']=power;charts.append(witness)
        origin=M.subs({A:0,B:0})
        if origin*row_matrix(boundary).T!=sp.zeros(1400,16):raise ArithmeticError('origin boundary kernel fails')
        annihilators[side]={'shape':[1400,112],'off_origin_dimension':14,'charts':charts,
                            'origin_dimension':16,'origin_minor':selected_minor(origin,96)}
    return {'family':{'parameters':['a','b'],'raw_boundary_indices':KEPT,
                     'B':maps(left),'C':maps(right),'full_source_shape':[112,14,14],
                     'full_coefficient_identity':True,'first_rank':12,'first_minor':first_minor,
                     'source_first_leading_indices':e.A0,'source_first_kernel_indices':e.OUTSIDE,
                     'fixed_pivot_columns':{'B':pivotsB,'C':pivotsC},
                     'pivot_determinants':[1,1],'scope':'Exact full two-parameter polynomial source fiber.'},
            'annihilators':annihilators,'polynomial_maps':polynormal(e,left,right)}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    for name,report in reports().items():
        (args.output_dir/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n');print(name,'written',flush=True)
