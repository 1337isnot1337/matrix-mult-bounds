"""Exact modular minors and algebraic row-support bounds for regular root maps."""
import importlib.util
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
from sympy import cyclotomic_poly,Symbol

_path=Path(__file__).resolve().parents[1]/'2026-10-20-quantum-recoupling/quantum.py'
_spec=importlib.util.spec_from_file_location('quantum',_path)
qmod=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(qmod)
PRIME=786433

def evaluate(poly,root):
    return sum(int(c.numerator)*pow(int(c.denominator),-1,PRIME)*pow(root,e[0],PRIME) for e,c in poly.items())%PRIME

@lru_cache(None)
def local_matrix(a):return qmod.cyclic_local_map(a)

@lru_cache(None)
def leading_parts(a,order):
    labels,entries=local_matrix(a)
    phi=qmod.R.from_expr(cyclotomic_poly(order,Symbol('q')))
    parts={key:qmod.initial_residue(value,phi) for key,value in entries.items()}
    minimum=min(v for v,polys in parts.values())
    leading={key:polys for key,(v,polys) in parts.items() if v==minimum}
    return labels,phi,minimum,leading

@lru_cache(None)
def root_map(a,order,power=1):
    labels,phi,minimum,leading=leading_parts(a,order)
    root=pow(10,(PRIME-1)//order*power,PRIME)
    if evaluate(phi,root):raise ArithmeticError('invalid cyclotomic residue root')
    support=sorted({i for i,j in leading})
    result={}
    for key,(num,den) in leading.items():
        denominator=evaluate(den,root)
        if not denominator:raise ArithmeticError('bad prime in residue denominator')
        value=evaluate(num,root)*pow(denominator,-1,PRIME)%PRIME
        if value:result[key]=value
    return {'a':a,'order':order,'root_power':power,'root':root,'global_minimum_valuation':minimum,
            'nonzero_rows_over_number_field':len(support),'row_labels':support,
            'local_leg_dimension':len(labels)},result

def projected_source(a,left,right):
    """Direct sparse contraction of every cyclic source coefficient; no float arithmetic."""
    D=a-1;h=2*D;V=a*a*(h+1)
    by_col_left=defaultdict(list);by_col_right=defaultdict(list)
    for (i,j),value in left.items():by_col_left[j].append((i,value))
    for (i,j),value in right.items():by_col_right[j].append((i,value))
    rows=[{} for _ in range(V)]
    for i in range(a):
        for j in range(a):
            for p in range(a):
                for q in range(a):
                    for r in range(a):
                        for s in range(a):
                            A=(i*a+s)*(h+1)+h-p-q
                            B=(p*a+j)*(h+1)+h-r-s
                            C=(r*a+q)*(h+1)+h-i-j
                            row=rows[A]
                            for b,x in by_col_left[B]:
                                for c,y in by_col_right[C]:
                                    col=b*V+c;row[col]=(row.get(col,0)+x*y)%PRIME
    return [{j:value for j,value in row.items() if value} for row in rows]

def independent_minor(rows):
    pivots={};row_indices=[];columns=[]
    for i,original in enumerate(rows):
        row=dict(original)
        while row:
            col=max(row)
            if col not in pivots:
                inv=pow(row[col],-1,PRIME)
                row={j:value*inv%PRIME for j,value in row.items()}
                pivots[col]=row;row_indices.append(i);columns.append(col);break
            factor=row[col];pivot=pivots[col]
            for j,value in pivot.items():
                new=(row.get(j,0)-factor*value)%PRIME
                if new:row[j]=new
                else:row.pop(j,None)
    return row_indices,columns

def determinant_mod(matrix):
    a=[list(row) for row in matrix];out=1
    for j in range(len(a)):
        pivot=next((i for i in range(j,len(a)) if a[i][j]),None)
        if pivot is None:return 0
        if pivot!=j:a[j],a[pivot]=a[pivot],a[j];out=-out
        value=a[j][j];out=out*value%PRIME;inverse=pow(value,-1,PRIME)
        for i in range(j+1,len(a)):
            factor=a[i][j]*inverse%PRIME
            for k in range(j+1,len(a)):a[i][k]=(a[i][k]-factor*a[j][k])%PRIME
    return out%PRIME

def report():
    records=[]
    for order in [3,4,6,8,12,16,24]:
        metadata,matrix=root_map(4,order)
        rows=projected_source(4,matrix,matrix)
        row_ids,columns=independent_minor(rows)
        minor=[[rows[i].get(j,0) for j in columns] for i in row_ids]
        determinant=determinant_mod(minor)
        if not determinant:raise ArithmeticError('invalid rank witness')
        upper=metadata['local_leg_dimension']-len(row_ids)+metadata['nonzero_rows_over_number_field']
        record={**metadata,'projection_rank_lower_bound':len(row_ids),
                'minor_rows':row_ids,'minor_columns':columns,'minor_determinant_mod_prime':determinant,
                'slice_rank_upper_bound_for_all_one_leg_Laurent_limits':upper}
        records.append(record);print(order,'rows',metadata['nonzero_rows_over_number_field'],'rank lower',len(row_ids),'slice ceiling',upper,flush=True)
    return {'prime':PRIME,'source_a':4,'records':records,
            'graded_order_three_six_controls':graded_controls(),
            'scope':'Two specified regular initial maps, arbitrary regular higher jets there and arbitrary Laurent maps on the first leg. Orders three and six need the additional grading hypotheses in graded_obstruction.md.',
            'proof_status':'Requires the written saturation/slice and graded arguments; no general all-leading-flags obstruction or exponent improvement.'}


def graded_controls():
    labels,_=local_matrix(4)
    phases=[(6,1),(3,1),(3,2),(6,5)]
    maps={};metadata={}
    for order,power in phases:
        meta,matrix=root_map(4,order,power)
        assert meta['nonzero_rows_over_number_field']==4
        assert [sum(labels[i]) for i in meta['row_labels']]==[4,5,7,8]
        key=(order,power);maps[key]=matrix;metadata[key]=meta
    records=[]
    for left in phases:
        for right in phases:
            rows=projected_source(4,maps[left],maps[right])
            choices=[(i,j,value) for i,row in enumerate(rows)
                     if i//7//4+i//7%4+i%7==6 for j,value in row.items() if value]
            if not choices:raise ArithmeticError('zero central projection; this graded obstruction would not apply')
            i,j,value=min(choices)
            exact=central_coefficient(left,right,i,j//112,j%112)
            if not exact:raise ArithmeticError('zero exact central coefficient')
            coefficients=[qmod.QQ.zero]*(2-len(exact.to_list()))+exact.to_list()
            pairs=[[int(c.numerator),int(c.denominator)] for c in coefficients]
            zeta_mod=pow(10,(PRIME-1)//6,PRIME)
            reduced=(pairs[0][0]*pow(pairs[0][1],-1,PRIME)*zeta_mod
                     +pairs[1][0]*pow(pairs[1][1],-1,PRIME))%PRIME
            if reduced!=value:raise ArithmeticError('number-field and modular coefficients disagree')
            records.append({'left_phase':list(left),'right_phase':list(right),
                            'left_root':metadata[left]['root'],'right_root':metadata[right]['root'],
                            'retained_row_grades':[4,5,7,8],'first_leg_grade':6,
                            'source_first_index':i,'left_output_index':j//112,'right_output_index':j%112,
                            'coefficient_mod_prime':value,
                            'exact_coefficient_basis_zeta6_then_one':pairs,
                            'rank_upper_bound_from_row_support':4})
    return {'source_central_dimension':16,'target_central_dimension':16,
            'target_minimum_nonzero_first_slice_rank':11,
            'full_target_grades_lost_on_each_large_leg':[3,9],
            'phase_pairs_checked':len(records),'nonzero_coefficient_witnesses':records,
            'scope':'Nonzero low-rank central matrices, not claimed exact complex ranks of the full projected tensor.'}


@lru_cache(None)
def quadratic_field():
    from sympy import sqrt
    zeta=(1+sqrt(-3))/2
    field=qmod.QQ.algebraic_field(zeta)
    return field,field.from_sympy(zeta)


@lru_cache(None)
def exact_phase_map(phase):
    order,power=phase;field,zeta=quadratic_field()
    root=zeta**(power*(6//order))
    _,_,_,parts=leading_parts(4,order)
    def evaluate_exact(poly):
        return sum((field.convert(c,qmod.QQ)*root**e[0] for e,c in poly.items()),field.zero)
    return {key:evaluate_exact(num)/evaluate_exact(den) for key,(num,den) in parts.items()}


def central_coefficient(left,right,A,Bout,Cout):
    """Independent exact number-field sum with the first source index fixed."""
    field,_=quadratic_field();B=exact_phase_map(left);C=exact_phase_map(right)
    i,s,k=A//7//4,A//7%4,A%7
    total=field.zero
    for p in range(4):
        q=6-k-p
        if not 0<=q<4:continue
        for j in range(4):
            for r in range(4):
                oldB=(p*4+j)*7+6-r-s
                oldC=(r*4+q)*7+6-i-j
                total+=B.get((Bout,oldB),field.zero)*C.get((Cout,oldC),field.zero)
    return total

if __name__=='__main__':
    import json,argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();args.output.write_text(json.dumps(report(),indent=2)+'\n')
