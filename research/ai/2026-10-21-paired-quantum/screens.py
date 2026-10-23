"""Exact calibration of prescribed paired-source quantum maps.

This verifies finite local-map and small-tensor statements only. It does not
provide the desired matrix direct-sum degeneration or improve omega.
"""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sys
import time

from sympy import QQ, I, pi, exp, cyclotomic_poly, Symbol

CORE = Path(__file__).resolve().parents[1]/'2026-10-20-quantum-recoupling'/'quantum.py'
spec = importlib.util.spec_from_file_location('quantum_core', CORE)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
q, K = core.q, core.K


def diagonal_factor(a,leg,i,j):
    D,h=a-1,2*a-2
    if leg==0:
        return q**(-i*(i-1)//2-j*(j-1)//2)
    z,v=(j,i) if leg==1 else (i,j)
    s=h-z
    return ((-1)**s*q**(-D*v-v*(v-1)//2+s*(s-1)//2+s*(h-s-1))
            /core.qchoose(h,s))


def source_controls(sizes=(2,3,4)):
    checks=0
    for a in sizes:
        D,h=a-1,2*a-2
        for p in range(a):
            for q0 in range(a):
                for y in range(a):
                    for v in range(a):
                        value=(diagonal_factor(a,0,p,q0)*diagonal_factor(a,1,y,h-q0-v)
                               *diagonal_factor(a,2,h-p-y,v))
                        expected=(core.invariant_coefficient(D,D,p,y)
                                  *core.invariant_coefficient(D,D,q0,v))
                        if value!=expected:
                            raise ArithmeticError(('local diagonal source identity',a,p,q0,y,v))
                        checks+=1
    return checks


def paired_local_map(a, leg):
    D, h = a-1, 2*a-2
    m, n = [(D,D), (D,h), (h,D)][leg]
    inverse = core.inverse_cg(m,n)
    labels = [(k,l) for k in range(min(m,n)+1)
              for l in range(m+n-2*k+1)]
    rows = {label:r for r,label in enumerate(labels)}
    entries = {}
    for i in range(m+1):
        for j in range(n+1):
            factor=diagonal_factor(a,leg,i,j)
            for label, value in inverse[i,j]:
                entries[rows[label],i*(n+1)+j] = value*factor
    return (m,n),labels,entries


@lru_cache(None)
def residue_field(order):
    field=QQ.algebraic_field(exp(2*pi*I/order))
    polynomial=core.R.from_expr(cyclotomic_poly(order,Symbol('q')))
    return field,polynomial


def regular_initial_entries(data,order):
    (m,n),labels,entries=data
    field,poly=residue_field(order)
    def residue(parts):
        values=[]
        for p in parts:
            values.append(sum((field.convert(c)*field.unit**e[0]
                               for e,c in p.items()),field.zero))
        return values[0]/values[1]
    expansions={key:core.initial_residue(value,poly)
                for key,value in entries.items()}
    minima=[min(v for (i,j),(v,parts) in expansions.items() if i==row)
            for row in range(len(labels))]
    initial={(i,j):residue(parts) for (i,j),(v,parts) in expansions.items()
             if v==minima[i]}
    return field,minima,initial


def regular_initial(data,order):
    (m,n),labels,entries=data
    field,minima,initial=regular_initial_entries(data,order)
    blocks=[]
    for s in range(m+n+1):
        rows=[r for r,label in enumerate(labels) if sum(label)==s]
        cols=[i*(n+1)+s-i for i in range(max(0,s-n),min(m,s)+1)]
        matrix=[[initial.get((r,c),field.zero) for c in cols] for r in rows]
        rank=core.rank_over_field(matrix,field.zero)
        blocks.append({'weight_index':s,'dimension':len(rows),'rank':rank})
    return {'m':m,'n':n,'root_order':order,'dimension':len(labels),
            'row_minimum_valuation_histogram':dict(sorted(Counter(minima).items())),
            'regular_initial_rank':sum(r['rank'] for r in blocks),
            'weight_blocks':blocks}


def regular_initial_tensor(a,order):
    """Contract the original constant paired tensor over the cyclotomic field."""
    h=2*a-2
    data=[paired_local_map(a,leg) for leg in range(3)]
    initials=[regular_initial_entries(d,order) for d in data]
    field=initials[0][0]
    maps=[]
    for (_,_,initial),((m,n),labels,_) in zip(initials,data):
        by_column={j:[] for j in range((m+1)*(n+1))}
        for (r,c),value in initial.items():
            by_column[c].append((r,value))
        maps.append(by_column)
    tensor={}
    for p in range(a):
        for q0 in range(a):
            for y in range(a):
                for v in range(a):
                    positions=(p*a+q0,y*(h+1)+h-q0-v,(h-p-y)*a+v)
                    for i,x in maps[0][positions[0]]:
                        for j,y0 in maps[1][positions[1]]:
                            for k,z in maps[2][positions[2]]:
                                key=i,j,k
                                tensor[key]=tensor.get(key,field.zero)+x*y0*z
    tensor={key:value for key,value in tensor.items() if value}
    dimensions=[len(d[1]) for d in data]
    flattenings=[]
    for leg in range(3):
        other=[j for j in range(3) if j!=leg]
        cols=sorted(set((index[other[0]],index[other[1]]) for index in tensor))
        matrix=[[tensor.get(tuple(row if k==leg else col[other.index(k)] for k in range(3)),field.zero)
                 for col in cols] for row in range(dimensions[leg])]
        flattenings.append(core.rank_over_field(matrix,field.zero))
    return {'a':a,'root_order':order,'source_format':dimensions,
            'nonzero_coefficients':len(tensor),'flattening_ranks':flattenings},data,field,tensor


def independent_rows(matrix,zero):
    echelon={}
    selected=[]
    for index,row in enumerate(matrix):
        row=list(row)
        for pivot,existing in sorted(echelon.items()):
            if row[pivot]:
                factor=row[pivot]/existing[pivot]
                row=[x-factor*y for x,y in zip(row,existing)]
        pivot=next((j for j,x in enumerate(row) if x!=zero),None)
        if pivot is not None:
            echelon[pivot]=row
            selected.append(index)
    return selected,echelon


def inverse_field(matrix,field):
    size=len(matrix)
    rows=[list(row)+[field.one if i==j else field.zero for j in range(size)]
          for i,row in enumerate(matrix)]
    for j in range(size):
        pivot=next((i for i in range(j,size) if rows[i][j]),None)
        if pivot is None:return None
        rows[j],rows[pivot]=rows[pivot],rows[j]
        factor=rows[j][j]
        rows[j]=[x/factor for x in rows[j]]
        for i in range(size):
            if i==j or not rows[i][j]:continue
            factor=rows[i][j]
            rows[i]=[x-factor*y for x,y in zip(rows[i],rows[j])]
    return [row[size:] for row in rows]


def multiply_matrices(left,right,zero):
    return [[sum((x*y for x,y in zip(row,col)),zero) for col in zip(*right)]
            for row in left]


def determinant_field(matrix,field):
    rows=[list(row) for row in matrix]
    out=field.one
    for j in range(len(rows)):
        pivot=next((i for i in range(j,len(rows)) if rows[i][j]),None)
        if pivot is None:return field.zero
        if pivot!=j:
            rows[pivot],rows[j]=rows[j],rows[pivot]
            out=-out
        value=rows[j][j]
        out*=value
        for i in range(j+1,len(rows)):
            if not rows[i][j]:continue
            factor=rows[i][j]/value
            for k in range(j+1,len(rows)):
                rows[i][k]-=factor*rows[j][k]
    return out


def encode_field(value):
    return [str(coefficient) for coefficient in value.to_list()]


def algebra_screen(a,order):
    report,data,field,tensor=regular_initial_tensor(a,order)
    dimensions=report['source_format']
    support=[]
    for leg in range(3):
        other=[j for j in range(3) if j!=leg]
        cols=sorted(set((index[other[0]],index[other[1]]) for index in tensor))
        matrix=[[tensor.get(tuple(row if k==leg else col[other.index(k)] for k in range(3)),field.zero)
                 for col in cols] for row in range(dimensions[leg])]
        support.append(independent_rows(matrix,field.zero)[0])
    if len(support[1])!=len(support[2]):
        report['matrix_algebra_screen']='unequal output dimensions'
        return report
    n=len(support[1]);dim=len(support[0])
    slices=[[[tensor.get((i,j,k),field.zero) for k in support[2]] for j in support[1]]
            for i in support[0]]
    # Deterministic small slice combinations; no success inference from a failed list.
    import random
    randomizer=random.Random(1)
    trials=[[int(i==j) for i in range(dim)] for j in range(dim)]
    trials+=[[randomizer.randrange(-5,6) for _ in range(dim)] for _ in range(10)]
    base_inverse=None
    for coefficients in trials:
        base=[[sum((field.convert(c)*s[i][j] for c,s in zip(coefficients,slices)),field.zero)
               for j in range(n)] for i in range(n)]
        base_inverse=inverse_field(base,field)
        if base_inverse is not None:break
    if base_inverse is None:
        report['matrix_algebra_screen']='no invertible tested slice; inconclusive'
        return report
    normalized=[multiply_matrices(base_inverse,s,field.zero) for s in slices]
    vectors=[sum(s,[]) for s in normalized]
    _,echelon=independent_rows(vectors,field.zero)
    failures=[]
    first_failure=None
    for i in range(dim):
        for j in range(dim):
            product=sum(multiply_matrices(normalized[i],normalized[j],field.zero),[])
            vector=list(product)
            for pivot,row in sorted(echelon.items()):
                if vector[pivot]:
                    factor=vector[pivot]/row[pivot]
                    vector=[x-factor*y for x,y in zip(vector,row)]
            if any(vector):
                failures.append([i,j])
                if first_failure is None:
                    witness_vectors=vectors+[product]
                    _,witness_echelon=independent_rows(witness_vectors,field.zero)
                    columns=sorted(witness_echelon)
                    minor=[[row[k] for k in columns] for row in witness_vectors]
                    first_failure={'product_indices':[i,j],
                                   'product_span_rank':len(columns),
                                   'minor_columns':columns,
                                   'minor_determinant_coefficients':encode_field(determinant_field(minor,field))}
    report.update(matrix_algebra_dimension=dim,matrix_size=n,
                  tested_invertible_slice_coefficients=coefficients,
                  compression_row_indices=support,
                  invertible_slice_determinant_coefficients=encode_field(determinant_field(base,field)),
                  product_closure_failures=failures,
                  first_product_failure=first_failure,
                  matrix_algebra_screen=('not a square-matrix multiplication tensor' if failures else
                                        'closed algebra; simplicity and multiplicity untested'))
    return report


def report():
    records=[]
    for a in (2,3,4):
        for leg in (0,1,2):
            data=paired_local_map(a,leg)
            for order in (3,4,6,8,10,12,14):
                record=regular_initial(data,order)
                record.update(a=a,leg=leg)
                records.append(record)
    record=regular_initial(paired_local_map(10,0),14)
    record.update(a=10,leg=0)
    records.append(record)
    return {'claim_id':'AI-PAIRED-QUANTUM-001',
            'status':'Exact finite calculations and written interpretation; unreviewed.',
            'improves_omega':False,
            'normalization':'Each local-map row is divided by its minimum cyclotomic valuation; take the residue.',
            'source_identity_checks':source_controls(),
            'local_map_records':records,
            'small_tensor_records':[algebra_screen(2,3),algebra_screen(3,10)],
            'scope':'Only the specified rowwise regular local maps and their ordinary tensor limits. Coupled singular tensor normalizations and other bases remain open.'}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('Verified',len(result['local_map_records']),'local maps and',
          len(result['small_tensor_records']),'small tensor limits; no omega improvement.')
