"""Small integer central-projection upper bounds for subgroup ideals.

The verifier checks z^2=z and z*sum(H)=sum(H) directly in the class algebra.
It does not trust imported character values or a modular rank upper bound.
"""
import argparse
from functools import lru_cache
from fractions import Fraction
from itertools import product
import json
from math import lcm
from pathlib import Path
import sys

PARENT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(PARENT/'2026-10-21-semisimple-koszul'))
from sl2_f8_source import group,derive
from sl2_f8_frames import subgroup


@lru_cache(None)
def class_data():
    G = group()
    unseen = set(range(504))
    classes = []
    while unseen:
        x = min(unseen)
        orbit = sorted({G['mul'][G['mul'][g][x]][G['inv'][g]] for g in range(504)})
        classes.append(orbit)
        unseen.difference_update(orbit)
    labels = {g:i for i,row in enumerate(classes) for g in row}
    constants = []
    for A in classes:
        plane = []
        for B in classes:
            counts = [0]*len(classes)
            for a,b in product(A,B):
                counts[labels[G['mul'][a][b]]] += 1
            if any(n%len(C) for n,C in zip(counts,classes)):
                raise ArithmeticError('nonintegral class product')
            plane.append([n//len(C) for n,C in zip(counts,classes)])
        constants.append(plane)
    return classes,labels,constants


def selected_subgroups():
    G = group()
    H18 = subgroup()
    def powers(g):
        row = [0]
        x = g
        while x:
            row.append(x)
            x = G['mul'][x][g]
        return row
    H9 = next(powers(g) for g in H18 if len(powers(g))==9)
    normalizer = {g for g in range(504) if all(
        G['mul'][G['mul'][g][h]][G['inv'][g]] in H9 for h in H9)}
    if normalizer!=set(H18):
        raise ArithmeticError('order-eighteen subgroup is not the full normalizer')
    H8 = [g for g,(a,b,c,d) in enumerate(G['matrices']) if (a,c,d)==(1,0,1)]
    return {'unipotent8':H8,'cyclic9':sorted(H9),'dihedral18':H18}


def verify_projection(H,coefficients,claimed_upper):
    G = group()
    if not H or len(set(H))!=len(H) or 0 not in H or any(type(h) is not int or not 0<=h<504 for h in H):
        raise ValueError('invalid subgroup elements')
    if any(G['mul'][a][b] not in H for a,b in product(H,repeat=2)):
        raise ValueError('not a subgroup')
    classes,labels,constants = class_data()
    if len(coefficients)!=len(classes):
        raise ValueError('wrong central-vector dimension')
    if any(type(v) not in [str,int] for v in coefficients) or type(claimed_upper) is not int:
        raise ValueError('exact rational coefficients and an integer rank required')
    z = list(map(Fraction,coefficients))
    denominator = lcm(*(v.denominator for v in z))
    numerators = [int(v*denominator) for v in z]
    for k in range(len(classes)):
        value = sum(numerators[i]*numerators[j]*constants[i][j][k]
                    for i,j in product(range(len(classes)),repeat=2))
        if value!=denominator*numerators[k]:
            raise ValueError('central projection is not idempotent')
    for g in range(504):
        value = sum(numerators[labels[G['mul'][g][G['inv'][h]]]] for h in H)
        if value!=denominator*int(g in H):
            raise ValueError('projection does not contain subgroup average')
    rank,remainder = divmod(504*numerators[0],denominator)
    if remainder or rank!=claimed_upper or not 0<=rank<=504:
        raise ValueError('incorrect regular projection rank')
    return {'subgroup_order':len(H),'central_class_dimension':len(classes),
            'coefficient_denominator':denominator,'coefficient_numerators':numerators,
            'ideal_dimension_upper_bound':rank,'idempotent_and_containment_verified':True}


def report():
    G = group()
    source = derive()
    classes,labels,constants = class_data()
    records = []
    for name,H in selected_subgroups().items():
        z = [Fraction(0)]*len(classes)
        retained = []
        for row in source['rational_central_blocks']:
            e = list(map(Fraction,row['central_idempotent']))
            nonzero = any(sum((e[labels[G['mul'][g][G['inv'][h]]]] for h in H),Fraction(0))
                          for g in range(504))
            if nonzero:
                z = [a+b for a,b in zip(z,e)]
                retained.append({'matrix_degree':row['complex_matrix_degree'],
                                 'complex_block_count':row['number_of_complex_blocks']})
        upper = 504*z[0]
        if upper.denominator!=1:
            raise ArithmeticError('nonintegral proposed projection rank')
        receipt = verify_projection(H,list(map(str,z)),int(upper))
        other_products = [18*25,18*25,18*18]
        records.append({'name':name,'subgroup':H,'central_projection':list(map(str,z)),
                        'retained_source_blocks':retained,'verification':receipt,
                        'selected_shape':[18,18,25],'other_pair_products':other_products,
                        'complete_coset_forbidden_on_legs':[v>int(upper) for v in other_products]})
    return {'group':'SL(2,F8)','group_order':504,'class_sizes':list(map(len,classes)),
            'records':records,
            'scope':'Complete subgroup cosets in injective-pair-map and strict-vertex-potential targets only. No general complex tensor-degeneration exclusion.',
            'imported_lemma':'Concurrent subgroup-ideal proof, pinned in import.json; written and unreviewed.',
            'improves_omega':False}


def verify_report(data):
    if data['group']!='SL(2,F8)' or data['group_order']!=504:
        raise ValueError('wrong group')
    classes,labels,constants = class_data()
    if data['class_sizes']!=list(map(len,classes)):
        raise ValueError('incorrect class ordering')
    expected = selected_subgroups()
    if {r['name'] for r in data['records']}!=set(expected) or len(data['records'])!=3:
        raise ValueError('incomplete subgroup cases')
    for row in data['records']:
        if row['subgroup']!=expected[row['name']]:
            raise ValueError('wrong selected subgroup')
        receipt = verify_projection(row['subgroup'],row['central_projection'],
                                    row['verification']['ideal_dimension_upper_bound'])
        if receipt!=row['verification']:
            raise ValueError('incorrect projection receipt')
        if row['selected_shape']!=[18,18,25] or row['other_pair_products']!=[450,450,324]:
            raise ValueError('incorrect target comparison')
        if row['complete_coset_forbidden_on_legs']!=[v>receipt['ideal_dimension_upper_bound'] for v in [450,450,324]]:
            raise ValueError('incorrect coset exclusions')
    return {'source':'SL(2,F8)','subgroup_projections_verified':3,'proof_status':'written, unreviewed',
            'improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    data = report()
    verify_report(data)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps([(r['name'],r['verification']['ideal_dimension_upper_bound'],
                       r['complete_coset_forbidden_on_legs']) for r in data['records']]))
