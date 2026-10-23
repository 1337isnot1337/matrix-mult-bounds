"""Exact controls for the written all-degree Hankel sharpness family."""
import argparse
import json
from pathlib import Path

import sympy as sp


def pencil(epsilon, p, q):
    s=p+q; r=epsilon*s; a=r+p; b=r+q
    u,v=sp.symbols('u v')
    h=[sp.Integer(0)]*(a+b-1)
    h[r-1]=u; h[r+s-1]=v
    coefficients=[sp.Integer(0)]*(r+1)
    for j in range(epsilon+1):
        coefficients[s*j]=(-v)**(epsilon-j)*u**j
    H=sp.Matrix(a,b,lambda i,j:h[i+j])
    return H,coefficients,(u,v)


def check(epsilon, p, q):
    H,P,(u,v)=pencil(epsilon,p,q)
    a,b=H.shape; r=epsilon*(p+q)
    right=sp.Matrix(b,q,lambda i,j:P[i-j] if j<=i<=j+r else 0)
    left=sp.Matrix(a,p,lambda i,j:P[i-j] if j<=i<=j+r else 0)
    for product in (H*right,H.T*left):
        if any(sp.expand(x) for x in product):
            raise ArithmeticError('polynomial kernel identity failed')
    sign=(-1)**(r*(r-1)//2)
    top=sp.expand(H[:r,:r].det(method='domain-ge'))
    bottom=sp.expand(H[a-r:,b-r:].det(method='domain-ge'))
    if top!=sign*u**r or bottom!=sign*v**r:
        raise ArithmeticError('projective rank minor failed')
    if (a+b-2*r)*epsilon!=r:
        raise ArithmeticError('index budget failed')
    return {'epsilon':epsilon,'left_nullity':p,'right_nullity':q,
            'shape':[a,b],'rank':r,'moment_indices':[r-1,r+p+q-1],
            'homogeneous_annihilator':{str(i):str(x) for i,x in enumerate(P) if x},
            'left_minimal_indices':[epsilon]*p,
            'right_minimal_indices':[epsilon]*q,
            'top_minor':str(top),'bottom_minor':str(bottom),
            'kernel_coefficient_identities':a*q+b*p,
            'index_sum':(p+q)*epsilon}


def report():
    records=[check(e,p,q) for e in range(1,5) for p in range(1,4) for q in range(1,4)]
    boundary=next(x for x in records if (x['epsilon'],x['left_nullity'],x['right_nullity'])==(2,2,2))
    return {'scope':'Finite exact controls for a written all-size family; no matrix target or exponent improvement.',
            'epsilon_range':[1,4],'left_and_right_nullity_range':[1,3],
            'pencils_checked':len(records),'records':records,'a10_boundary':boundary,
            'independent_review':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=report(); args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f"Verified {result['pencils_checked']} homogeneous pencils and both endpoint minors.")
