"""Exact controls for a characteristic-zero Hankel-space Wronskian proof."""
import argparse
from itertools import combinations
import json
from math import comb,prod
from pathlib import Path
import sympy as sp


def linear_space_cap(a,b,r):
    if not (0<=r<min(a,b)):return None
    return r


def tail_minor(a,b,r,k):
    if not (1<=r<min(a,b) and r<=k<=a+b-2-r):raise ValueError('Outside the antidiagonal minor range')
    i0=max(0,k-b+1);j0=k-r-i0
    assert 0<=i0<=a-r-1 and 0<=j0<=b-r-1
    for i in range(r+1):
        for j in range(r+1):
            degree=i0+j0+i+j
            if i+j<r:assert degree<k
            elif i+j==r:assert degree==k
    return [a,b,r,k,i0,j0]


def tail_controls():
    cases=[]
    for a in range(2,13):
        for b in range(2,13):
            for r in range(1,min(a,b)):
                for k in range(r,a+b-1-r):cases.append(tail_minor(a,b,r,k))
    return {'format_range':[2,12],'cases':cases,'complete_case_count':len(cases)}


def shear_controls():
    coefficients=0;translations=0
    for a in range(2,13):
        for b in range(2,13):
            d=a+b-2
            for p in range(a):
                for q in range(b):
                    for ell in range(p+q,d+1):
                        value=sum(comb(a-1-p,i-p)*comb(b-1-q,ell-i-q)
                                  for i in range(p,a) if q<=ell-i<b)
                        assert value==comb(d-p-q,ell-p-q);coefficients+=1
            for k in range(d+1):
                for j in range(k,d+1):
                    assert comb(d,k)*comb(d-k,j-k)==comb(d,j)*comb(j,k);translations+=1
    return {'formats':121,'hankel_shear_coefficients_checked':coefficients,
            'polynomial_translation_coefficients_checked':translations,
            'triangular_diagonal_entries':1,'shear_determinants':1}


def falling(n,j):
    return prod(n-i for i in range(j))


def monomial_wronskian(degrees):
    r=len(degrees)-1
    matrix=sp.Matrix([[falling(n,j) for n in degrees] for j in range(r+1)])
    determinant=int(matrix.to_DM().det())
    expected=prod(degrees[j]-degrees[i] for i in range(r+1) for j in range(i+1,r+1))
    assert determinant==expected and determinant!=0
    exponent=sum(degrees)-r*(r+1)//2;assert exponent>=0
    return {'degrees':list(degrees),'leading_coefficient':determinant,'wronskian_degree':exponent}


def polynomial_control(degrees):
    t=sp.symbols('t');polynomials=[]
    for i,n in enumerate(degrees):
        polynomials.append((i+2)*t**n+sum(((i+3)*(j+1)%7-3)*t**j for j in range(n)))
    matrix=sp.Matrix([[sp.diff(f,t,j) for f in polynomials] for j in range(len(degrees))])
    W=sp.Poly(matrix.det(method='domain-ge'),t)
    expected=prod(i+2 for i in range(len(degrees)))*monomial_wronskian(degrees)['leading_coefficient']
    exponent=sum(degrees)-len(degrees)*(len(degrees)-1)//2
    assert W.degree()==exponent and W.LC()==expected
    return {'degrees':list(degrees),'polynomials_low_to_high':[[int(c) for c in reversed(sp.Poly(f,t).all_coeffs())] for f in polynomials],
            'wronskian_low_to_high':[int(c) for c in reversed(W.all_coeffs())],
            'leading_coefficient':int(W.LC()),'wronskian_degree':int(W.degree())}


def witness(a,b,r,basis):
    """Find an integer rank>r witness in any rational(r+1)-space."""
    if not (1<=r<min(a,b)):raise ValueError('Need1<=r<min(a,b)')
    d=a+b-2
    if len(basis)!=r+1 or any(len(row)!=d+1 for row in basis):raise ValueError('Wrong basis shape')
    rows=sp.Matrix([[sp.Rational(x) for x in row] for row in basis])
    if rows.to_DM().rank()!=r+1:raise ValueError('Basis is dependent')
    degree_bound=(r+1)*(d-r)
    for lam in range(degree_bound+1):
        C=sp.Matrix(r+1,r+1,lambda k,i:sum(comb(d-k,j-k)*lam**(j-k)*rows[i,j] for j in range(k,d+1)))
        if C.to_DM().det()==0:continue
        target=sp.zeros(r+1,1);target[r,0]=1
        coefficients=C.inv()*target
        h=coefficients.T*rows
        scale=sp.ilcm(*[sp.denom(x) for x in h]);h=[int(scale*x) for x in h]
        coefficients=[str(scale*x) for x in coefficients]
        transformed=[sum(comb(d-k,j-k)*lam**(j-k)*h[j] for j in range(k,d+1)) for k in range(d+1)]
        assert transformed[:r]==[0]*r and transformed[r]==scale
        H=sp.Matrix(a,b,lambda i,j:h[i+j])
        columns=list(H.to_DM().rref()[1][:r+1])
        minor_rows=list(H[:,columns].T.to_DM().rref()[1][:r+1])
        determinant=int(H.extract(minor_rows,columns).to_DM().det());assert determinant
        return {'a':a,'b':b,'r':r,'input_basis':[[str(x) for x in row] for row in rows.tolist()],
                'linear_combination_coefficients':coefficients,'integer_moments':h,
                'shear_lambda':lam,'shear_search_upper':degree_bound,
                'sheared_pivot':int(scale),'original_minor':{'rows':minor_rows,'columns':columns,'determinant':determinant},
                'rank_exceeds_r':True}
    raise ArithmeticError('Wronskian root bound violated')


def witness_controls():
    cases=[]
    for a,b,r,indices in [(3,4,2,[0,3,5]),(5,5,3,[0,2,6,8]),(8,8,6,[0,1,2,3,12,13,14])]:
        basis=[[int(i==j) for j in range(a+b-1)] for i in indices]
        cases.append(witness(a,b,r,basis))
    t=sp.symbols('t');a=b=4;r=3;d=a+b-2
    # Its Wronskian vanishes at0 and-1, exercising more than one trial shear.
    polynomials=[sp.Poly(t*(t+1)*t**j,t) for j in range(r+1)]
    basis=[[(-1)**k*f.nth(k)/comb(d,k) for k in range(d+1)] for f in polynomials]
    mixed=witness(a,b,r,basis);assert mixed['shear_lambda']==2;cases.append(mixed)
    return cases


def report():
    cases=[]
    for dimension in range(2,5):
        for degrees in combinations(range(10),dimension):cases.append(monomial_wronskian(degrees))
    polynomial=[polynomial_control(x) for x in [(0,1,2),(0,3,6),(1,4,8),(0,2,5,9),(0,1,3,6,10)]]
    return {'scope':'Exact identity controls for a written all-size proof, not an exhaustive proof by finite testing.',
            'tail_minors':tail_controls(),'binomial_shears':shear_controls(),
            'monomial_wronskians':{'maximum_polynomial_degree':9,'cases':cases,'case_count':len(cases)},
            'polynomial_wronskians':polynomial,'generated_witnesses':witness_controls(),
            'sharp_space':'Sequences supported on h_0,...,h_(r-1), of dimension r.',
            'outside_rank_hypothesis':{'a':2,'b':3,'r':2,'full_space_dimension':4,'all_matrices_have_rank_at_most':2},
            'positive_characteristic_method_control':{'prime':5,'independent_polynomials':['1','t^5'],'wronskian_over_Z':'5*t^4','wronskian_mod_prime':0,'does_not_disprove_finite_field_cap':True},
            'full_segre_image_cap_r_claimed':False,'independent_review':False,'improves_omega':False}


def write_json(path,data):
    def render(value,level=0,key=None):
        pad='  '*level
        if isinstance(value,dict):return '{\n'+',\n'.join(pad+'  '+json.dumps(k)+': '+render(v,level+1,k) for k,v in value.items())+'\n'+pad+'}'
        if isinstance(value,list):
            if key in {'cases','records','dimension_frontier'}:return '[\n'+',\n'.join(pad+'  '+json.dumps(v,separators=(',',':')) for v in value)+'\n'+pad+']'
            if all(not isinstance(v,(dict,list)) for v in value):return json.dumps(value)
            return '[\n'+',\n'.join(pad+'  '+render(v,level+1) for v in value)+'\n'+pad+']'
        return json.dumps(value)
    path.write_text(render(data)+'\n')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);p.add_argument('--basis-input',type=Path)
    args=p.parse_args();args.output.parent.mkdir(parents=True,exist_ok=True)
    if args.basis_input:
        data=json.loads(args.basis_input.read_text());x=witness(data['a'],data['b'],data['r'],data['basis'])
        write_json(args.output,x);print('Exact integer rank witness exported.')
    else:
        x=report();write_json(args.output,x)
        print(x['tail_minors']['complete_case_count'],'tail minors and',x['monomial_wronskians']['case_count'],'Wronskian determinants checked.')
