"""Exact certificates for the fixed-family all-weight obstruction.

The invariant-theory implication is proved in README.md. This program
verifies the finite hypotheses, including complete rational contractions.
"""
from collections import Counter
from fractions import Fraction
import importlib.util
import json
from pathlib import Path

from sympy import QQ

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result


quantum=module('nearfull_certificate_quantum',HERE/'quantum.py')
faces=module('nearfull_certificate_faces',ROOT/'research/ai/2026-10-21-narrow-quantum/faces.py')


def uniform_marginals(data,certificate):
    dimensions=data['source_format']
    marginals=[[Fraction(0) for _ in range(d)] for d in dimensions]
    total=Fraction(0)
    seen=set()
    for item in certificate['support']:
        index=item['index'];probability=Fraction(item['probability'])
        if index in seen or probability<=0:
            raise ArithmeticError('Distribution has duplicate or nonpositive terms.')
        seen.add(index)
        row=data['coefficients'][index]
        if row['baseline_valuation']!=0:
            raise ArithmeticError('Distribution uses a positive-valuation coefficient.')
        total+=probability
        for axis,coordinate in enumerate(row['positions']):
            marginals[axis][coordinate]+=probability
    assert total==1
    assert all(all(p==Fraction(1,d) for p in row) for d,row in zip(dimensions,marginals))
    return {'positive_support_size':len(seen),'total_probability':str(total),
            'marginals':[[str(p) for p in row] for row in marginals]}


def tensor_from_initial(data):
    field,_=faces.screen.residue_field(data['order'])
    tensor={tuple(r['positions']):faces.decode(r['leading_residue_coefficients'],field)
            for r in data['coefficients'] if r['baseline_valuation']==0}
    assert all(tensor.values())
    return field,tensor


def k1_all_legs(tensor,dimensions,weights,field):
    result=[]
    for axis in range(3):
        order=[axis]+[j for j in range(3) if j!=axis]
        transformed={tuple(key[j] for j in order):value for key,value in tensor.items()}
        result.append(faces.graded_koszul(transformed,[dimensions[j] for j in order],
                      [weights[j] for j in order],1,field))
    return result


def target(N,m):
    tensor={(i*N+j,j*m+k,k*N+i):QQ.one
            for i in range(N) for j in range(N) for k in range(m)}
    dimensions=[N*N,N*m,N*m]
    weights=[[i+j for i in range(N) for j in range(N)],
             [N-1-j+k for j in range(N) for k in range(m)],
             [N+m-2-i-k for k in range(m) for i in range(N)]]
    return tensor,dimensions,weights


def face32(data):
    w=[0,5,-4,10,1,-8,15,6,-3,-12,11,2,-7,7,-2,3]
    indices,exponents=faces.leading_indices(data,27,w*3)
    row_index=[0,1,0,2,1,0,3,2,1,0,3,2,1,3,2,3]
    z=[3-2*i for i in row_index]
    assert sum(z)==0
    supported_weights=[sum(z[p] for p in data['coefficients'][j]['positions']) for j in indices]
    assert supported_weights and min(supported_weights)>0
    field,_=faces.screen.residue_field(data['order'])
    tensor={tuple(data['coefficients'][j]['positions']):
            faces.decode(data['coefficients'][j]['leading_residue_coefficients'],field)
            for j in indices}
    weights=[[row['weight'] for row in records for _ in row['generic_rows']]
             for records in data['local_records']]
    ranks=k1_all_legs(tensor,data['source_format'],weights,field)
    assert ranks==[256,256,256]
    return {'denominator':27,'integer_weights':w*3,'face_size':len(indices),
            'k1_ranks':ranks,
            'trace_zero_instability_weights':[z,z,z],
            'supported_instability_weight_histogram':dict(sorted(Counter(supported_weights).items()))}


def report_case(N,m,rebuild=True):
    if rebuild:
        data=quantum.run(N,m,True)
    else:
        data=json.loads((ROOT/f'results/nearfull-quantum-2026-10-21/N{N}-m{m}-family.json').read_text())
    weights=[[row['weight'] for row in records for _ in row['generic_rows']]
             for records in data['local_records']]
    certificate=json.loads((HERE/f'N{N}-m{m}-balanced.json').read_text())
    balance=uniform_marginals(data,certificate)
    field,tensor=tensor_from_initial(data)
    source_ranks=k1_all_legs(tensor,data['source_format'],weights,field)
    target_tensor,dimensions,target_weights=target(N,m)
    assert data['source_format']==dimensions
    target_ranks=k1_all_legs(target_tensor,dimensions,target_weights,QQ)
    assert any(s<t for s,t in zip(source_ranks,target_ranks))
    output={'N':N,'m':m,'root_order':data['order'],'target_format':dimensions,
            'coefficient_count':len(data['coefficients']),
            'valuation_histogram':dict(sorted(Counter(r['baseline_valuation'] for r in data['coefficients']).items())),
            'source_initial_k1_ranks':source_ranks,'target_k1_ranks':target_ranks,
            'balanced_distribution':balance,
            'all_diagonal_Laurent_weights_excluded_by_written_lemma':True,
            'improves_omega':False}
    if (N,m)==(4,4):output['explicit_unstable_face']=face32(data)
    return output,data


def report(rebuild=True):
    pairs=[report_case(N,m,rebuild) for N,m in [(3,2),(4,4)]]
    return {'status':'Exact finite hypotheses and written all-weight theorem; mathematical review is separate.',
            'scope':'Two prescribed regular q-families, arbitrary diagonal Laurent weights and further degenerations to the same full matrix target.',
            'improves_omega':False,'cases':[row for row,_ in pairs]},[data for _,data in pairs]


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--stored',action='store_true')
    args=parser.parse_args()
    result,data=report(not args.stored)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    if not args.stored:
        for row in data:
            path=args.output.parent/f"N{row['N']}-m{row['m']}-family.json"
            path.write_text(json.dumps(row,indent=2)+'\n')
    print(json.dumps(result))
