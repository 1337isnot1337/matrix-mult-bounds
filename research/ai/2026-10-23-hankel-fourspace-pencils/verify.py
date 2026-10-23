"""Exact identities for quadratic pencils inside the prescribed A10 four-space."""
import argparse
import json
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


def matrices(line):
    u,v=sp.symbols('u v')
    A,B,C,D=[a*u+b*v for a,b in line]
    Q=[B*D-C*C,B*C-A*D,A*C-B*B]
    M=sp.Matrix([[sp.expand(x).coeff(u,2-j).coeff(v,j) for j in range(3)] for x in Q])
    square=[Q[0]**2,2*Q[0]*Q[1],Q[1]**2+2*Q[0]*Q[2],2*Q[1]*Q[2],Q[2]**2]
    N=sp.Matrix([[sp.expand(x).coeff(u,4-j).coeff(v,j) for j in range(5)] for x in square])
    (a0,a1),(b0,b1),(c0,c1),(d0,d1)=line
    delta=3*(b0*c1-b1*c0)-(a0*d1-a1*d0)
    return M,N,delta


def exact_rank(matrix):
    return DomainMatrix.from_Matrix(matrix).convert_to(sp.QQ).rank()


def chart_identity():
    a,b,c,d=sp.symbols('a b c d')
    M,N,delta=matrices([(1,0),(a,b),(c,d),(0,1)])
    chi=sp.expand(M.det()); determinant=sp.expand(N.det(method='domain-ge'))
    residual=sp.Poly(determinant+4*delta*chi**3,a,b,c,d)
    if not residual.is_zero:
        raise ArithmeticError('universal chart determinant identity failed')
    return {'chart':'A=u,D=v,B=a*u+b*v,C=c*u+d*v',
            'delta':str(delta),'chi':str(chi),
            'identity':'det(N) = -4*Delta*det(M)^3',
            'nonzero_residual_coefficients':0,
            'global_extension':'Polynomial density and parameter GL2 weights 10=1+3*3; see proof.'}


def line_certificate(line):
    M,N,delta=matrices(line); chi=M.det()
    if not chi:
        raise ArithmeticError('line does not meet the stated nonzero-chi guard')
    if sp.expand(N.det()+4*delta*chi**3):
        raise ArithmeticError('line determinant identity failed')
    rank=exact_rank(N)
    operator=sp.zeros(15,19)
    for shift in range(3):
        for degree in range(5):
            for k in range(5):operator[5*shift+degree,shift+4*k]=N[k,degree]
    tangent_dimension=19-exact_rank(operator)
    if rank!=(5 if delta else 4) or tangent_dimension!=(4 if delta else 7):
        raise ArithmeticError('tangent jump failed')
    return {'line':[[str(a),str(b)] for a,b in line],
            'chi':str(chi),'delta':str(delta),'square_coefficient_rank':rank,
            'common_tangent_dimension':tangent_dimension,
            'unique_four_space_proved_by_first_order':bool(delta)}


def hankel(moments):
    return sp.Matrix(10,10,lambda i,j:moments[i+j])


def exceptional_certificate():
    A,B,C,D,x,y,z=sp.symbols('A B C D x y z'); E=A-D
    w=[0]*19
    for i,value in {3:A,7:B,11:C,15:D,4:x,5:y,6:z,16:-2*x,17:-2*y,18:-2*z}.items():w[i]=value
    J=hankel(w)
    generators=[B*x+y*z,2*B*y+z*z,B*z,E*x,2*E*y+3*x*x,E*z+3*x*y]
    g1,g2,g3,g4,g5,g6=generators
    expected=[sp.Matrix([[-2*g1,-g2],[-g2,-2*g3]]),
              sp.Matrix([[-2*g4-4*g1,-g5-2*g2],[-g5-2*g2,-2*g6-4*g3]])]
    obstructions=[]
    for t,advertised in zip([0,1],expected):
        h=[0]*19; h[3]=t;h[11]=1;h[15]=t;H=hankel(h)
        columns=list(H.rref()[1]); rows=list(H[:,columns].T.rref()[1])
        pivot=H.extract(rows,columns)
        left=sp.Matrix.hstack(*H.T.nullspace());right=sp.Matrix.hstack(*H.nullspace())
        quadratic=(-left.T*J[:,columns]*pivot.inv()*J[rows,:]*right).applyfunc(sp.expand)
        if (quadratic-advertised).applyfunc(sp.expand)!=sp.zeros(2,2):
            raise ArithmeticError('exceptional Schur quadratic failed')
        obstructions.append({'t':t,'pivot_rows':rows,'pivot_columns':columns,
                             'second_schur_coefficient':[str(v) for v in quadratic]})
    if sp.expand(x*g5-2*y*g4)!=3*x**3 or sp.expand(z*g2-2*y*g3)!=z**3:
        raise ArithmeticError('nilpotent elimination identity failed')
    reduced_moments=[0,A,y,0,0,C,0,A,-2*y]
    T=sp.Matrix(5,5,lambda i,j:reduced_moments[i+j])
    if sp.expand(T.det(method='domain-ge'))!=A*A*y**3:
        raise ArithmeticError('higher determinant failed')
    extra=J.subs({A:0,B:0,C:0,D:0,x:0,y:1,z:0})
    endpoint=[0]*19;endpoint[3]=endpoint[15]=1
    if exact_rank(extra)!=8 or (extra+hankel(endpoint)).det()!=-1:
        raise ArithmeticError('transverse nonintegration control failed')
    return {'line':[[0,1],[0,0],[1,0],[0,1]],
            'common_tangent_dimension':7,'maximal_linear_extension_dimension':4,
            'free_transverse_moments':[4,5,6],
            'paired_moments':{'16':'-2*x','17':'-2*y','18':'-2*z'},
            'necessary_quadratics':[str(g) for g in generators],
            'quadratic_witnesses':obstructions,
            'nilpotent_identities':['x*g5-2*y*g4 = 3*x^3','z*g2-2*y*g3 = z^3'],
            'half_block_determinant':'A^2*y^3','full_determinant':'-A^4*y^6',
            'transverse_direction_rank':8,'direction_plus_seed_endpoint_determinant':-1}


def report():
    lines=[[(0,0),(1,0),(0,1),(0,0)],
           [(0,1),(0,0),(1,0),(0,1)],
           [(1,0),(sp.Rational(1,3),0),(0,1),(0,1)],
           [(1,0),(1,1),(2,3),(0,1)],
           [(1,0),(2,-1),(1,2),(0,1)],
           [(2,1),(1,3),(-1,2),(3,-1)]]
    return {'scope':'Universal polynomial determinant identity and exact line/exceptional-seed controls; written unreviewed proofs over C.',
            'chart_identity':chart_identity(),
            'lines':[line_certificate(line) for line in lines],
            'exceptional_seed':exceptional_certificate(),
            'other_exceptional_extensions_classified':False,
            'arbitrary_quadratic_hankel_pencils_classified':False,
            'independent_review':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('Universal chart identity, tangent jumps and exceptional higher obstruction verified.')
