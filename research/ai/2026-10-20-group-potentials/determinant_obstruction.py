"""Necessary determinant-divisor condition for C[G] -> M(n,n,p).

The written all-size argument is in research_note.md. A passing screen is not
a construction. Character degrees must be certified separately.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def obstruction(order: int, degrees: list[int], n: int, p: int) -> dict:
    if n<1 or p<1 or order<1 or not degrees or any(d<1 for d in degrees):
        raise ValueError('positive dimensions and degrees required')
    if sum(d*d for d in degrees)!=order:
        raise ValueError('source dimension does not equal the degree-square sum')
    M=n*p
    if M>order or n*n>order:
        return {'excluded':True,'reason':'ordinary flattening dimension',
                'order':order,'target':[n,n,p]}
    c=order-M
    bad=sorted({d for d in degrees if d>c and d%n})
    return {'order':order,'target':[n,n,p],'square_slice_size':M,
            'codimension':c,'excluded':bool(bad),
            'obstructing_irrep_degrees':bad,
            'reason':'A source degree d>codimension forces a homogeneous '
                     'determinant divisor of degree d; target divisors have '
                     'degrees divisible by n.' if bad else
                     'This necessary determinant screen does not exclude the target.',
            'proof_status':'written proof, unreviewed; see research_note.md',
            'improves_omega':False}


def frobenius_degrees(p: int,r: int) -> list[int]:
    if p<2 or any(p%d==0 for d in range(2,int(p**0.5)+1)) or r<1 or (p-1)%r:
        raise ValueError('prime p and positive index dividing p-1 required')
    return [1]*r+[r]*((p-1)//r)


def abelian_coset_bounds(subgroup_order: int,index: int,shape: list[int]) -> dict:
    if subgroup_order<1 or index<1 or len(shape)!=3 or min(shape)<1:
        raise ValueError('positive subgroup order, index and three dimensions required')
    lower=[(n+index-1)//index for n in shape]
    product=lower[0]*lower[1]*lower[2]
    upper=[subgroup_order//(lower[(f+1)%3]*lower[(f+2)%3]) for f in range(3)]
    return {'subgroup_order':subgroup_order,'subgroup_index':index,'shape':shape,
            'max_coset_size_lower':lower,'max_coset_size_upper':upper,
            'ceiling_product':product,'excluded':product>subgroup_order,
            'scope':'Necessary for the coordinate-potential group construction; '
                    'not asserted for arbitrary non-coordinate degenerations.'}


def report():
    return {'examples':[
        {'source':f'C{p}:C{r}','degrees':frobenius_degrees(p,r),
         'screen':obstruction(p*r,frobenius_degrees(p,r),n,k)}
        for p,r,n,k in [(5,4,4,5),(7,3,4,5),(13,4,7,7),
                        (13,3,6,6),(17,4,8,8),(19,3,7,7)]],
        'scope':'All-size necessary theorem; examples do not exhaust groups or targets.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
