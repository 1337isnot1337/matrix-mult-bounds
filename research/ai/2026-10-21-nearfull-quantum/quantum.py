"""Exact prescribed root-of-unity subspace families for two rectangles.

These maps define genuine restrictions of the constant source Q(n,m).
They do not supply a matrix multiplication restriction.
"""
from collections import defaultdict
from pathlib import Path
import argparse,importlib.util,json,time

ROOT=Path(__file__).resolve().parents[3]
SPEC=importlib.util.spec_from_file_location('nearfull_narrow_quantum_dependency',
    ROOT/'research/ai/2026-10-21-narrow-quantum/quantum.py')
q=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(q)


def choices(N,m,leg):
    if (N,m) not in ((3,2),(4,4)):
        raise ValueError('This certificate covers only (N,m)=(3,2),(4,4).')
    ell=N+m//2
    data=q.local_map(N+1,m,leg)
    if leg==0:
        selected=[j for j,(k,l) in enumerate(data[1]) if k>=1]
    else:
        degrees=[N+2*m-2-2*k for k in range(m)]
        selected=[]
        for j,(k,l) in enumerate(data[1]):
            d=degrees[k]
            reflected=2*ell-2-d
            if reflected in degrees or d<ell:
                selected.append(j)
            elif d-ell+1<=l<=ell-1:
                selected.append(j)
    return data,selected


def dvr_limit(data,selected,order):
    shape,labels,entries=data
    field,poly=q.screen.residue_field(order)
    ncols=(shape[0]+1)*(shape[1]+1)
    rows=[];records=[];generic=[]
    for weight in sorted({sum(labels[i]) for i in selected}):
        inds=[i for i in selected if sum(labels[i])==weight]
        matrix=[[entries.get((i,j),q.K.zero) for j in range(ncols)] for i in inds]
        pivots=[]
        for rank in range(len(matrix)):
            choices=[(q.core.valuation(matrix[i][j],poly),i,j)
                     for i in range(rank,len(matrix)) for j in range(ncols)
                     if j not in pivots and matrix[i][j]]
            if not choices:raise ArithmeticError('Rows unexpectedly dependent')
            val,i,j=min(choices)
            matrix[rank],matrix[i]=matrix[i],matrix[rank]
            factor=matrix[rank][j]
            matrix[rank]=[x/factor for x in matrix[rank]]
            for i in range(len(matrix)):
                if i!=rank and matrix[i][j]:
                    factor=matrix[i][j]
                    matrix[i]=[x-factor*y for x,y in zip(matrix[i],matrix[rank])]
            pivots.append(j)
        initial=[]
        for row in matrix:
            values=[]
            for value in row:
                if not value:values.append(field.zero);continue
                val,parts=q.core.initial_residue(value,poly)
                if val<0:raise ArithmeticError(('nonintegral row',weight,val))
                if val>0:values.append(field.zero);continue
                numerator,denominator=[sum((field.convert(c)*field.unit**e[0] for e,c in part.items()),field.zero) for part in parts]
                values.append(numerator/denominator)
            initial.append(values)
        assert q.core.rank_over_field(initial,field.zero)==len(matrix)
        for i,row in enumerate(matrix):
            assert all(row[j]==(q.K.one if i==k else q.K.zero) for k,j in enumerate(pivots))
        rows.extend(initial)
        generic.extend(matrix)
        records.append({'weight':weight,'selected_labels':[labels[i] for i in inds],
                        'pivot_columns':pivots,'generic_rows':[[str(x) for x in row] for row in matrix]})
    return field,rows,records,generic


def tensor(N,m,maps,field):
    n=N+1;h=N+m-1
    columns=[{j:[(i,row[j]) for i,row in enumerate(matrix) if row[j]] for j in range(len(matrix[0]))} for matrix in maps]
    out=defaultdict(lambda:field.zero)
    for p in range(n):
        for r in range(n):
            for y in range(m):
                for v in range(m):
                    coords=(p*n+r,y*(h+1)+h-r-v,(h-p-y)*m+v)
                    for i,a in columns[0][coords[0]]:
                        for j,b in columns[1][coords[1]]:
                            for k,c in columns[2][coords[2]]:out[i,j,k]+=a*b*c
    return {key:value for key,value in out.items() if value}


def run(N,m,make_family=False):
    start=time.monotonic();order=2*N+m
    maps=[];local=[];generic_maps=[]
    for leg in range(3):
        data,selected=choices(N,m,leg)
        print('local',leg,'selected',len(selected),'building',flush=True)
        field,matrix,record,generic=dvr_limit(data,selected,order)
        maps.append(matrix);local.append(record)
        generic_maps.append(generic)
        print('local',leg,'rank',len(matrix),'elapsed',time.monotonic()-start,flush=True)
    T=tensor(N,m,maps,field)
    shape=[len(matrix) for matrix in maps]
    weights=[[record['weight'] for record in rows for _ in record['generic_rows']]
             for rows in local]
    assert all(sum(weights[k][key[k]] for k in range(3))==2*(N+m-1) for key in T)
    ranks=[]
    for axis in range(3):
        other=[j for j in range(3) if j!=axis]
        columns=sorted({tuple(key[j] for j in other) for key in T})
        matrix=[[T.get(tuple(i if j==axis else col[other.index(j)] for j in range(3)),field.zero) for col in columns] for i in range(shape[axis])]
        ranks.append(q.core.rank_over_field(matrix,field.zero))
    slices=[]
    for i in range(shape[0]):
        S=[[T.get((i,j,k),field.zero) for k in range(shape[2])] for j in range(shape[1])]
        slices.append(q.core.rank_over_field(S,field.zero))
    result={'N':N,'m':m,'order':order,'map_shape':shape,'flattening_ranks':ranks,
            'basis_slice_ranks':slices,'tensor_nonzero_count':len(T),'local_records':local,
            'maps':[[[q.screen.encode_field(x) for x in row] for row in M] for M in maps],
            'tensor':[{'positions':list(key),'coefficient':q.screen.encode_field(value)} for key,value in sorted(T.items())],
            'seconds':time.monotonic()-start,'improves_omega':False}
    result['coordinate_weights']=weights
    if make_family:
        polynomial=q.screen.residue_field(order)[1]
        print('generic tensor contraction',flush=True)
        generic_tensor=tensor(N,m,generic_maps,q.K)
        print('generic tensor nonzeros',len(generic_tensor),flush=True)
        coefficients=[]
        for positions,value in sorted(generic_tensor.items()):
            valuation,parts=q.core.initial_residue(value,polynomial)
            numerator,denominator=[sum((field.convert(c)*field.unit**e[0] for e,c in part.items()),field.zero) for part in parts]
            assert valuation>=0
            coefficients.append({'positions':positions,'generic_coefficient':str(value),
                                 'baseline_valuation':valuation,'leading_residue_coefficients':q.screen.encode_field(numerator/denominator)})
        result.update({'source_format':shape,'coefficients':coefficients,'generic_nonzero_count':len(coefficients)})
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--N',type=int,default=3);parser.add_argument('--m',type=int,default=2)
    parser.add_argument('--family',action='store_true')
    parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    result=run(args.N,args.m,args.family)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['N','m','order','map_shape','flattening_ranks','basis_slice_ranks','tensor_nonzero_count','seconds']}))
