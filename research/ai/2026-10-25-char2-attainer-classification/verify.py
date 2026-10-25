"""Exact algebra for a written geometric classification, not a formal proof."""
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
x,y,t,L,J,B = sp.symbols('x y t L J B')


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def mod2(expr):
    expr=sp.expand(expr)
    variables=sorted(expr.free_symbols,key=str)
    return sp.Poly(expr,*variables,modulus=2).as_expr() if variables else sp.Integer(expr)%2


def check_pins():
    sources=json.loads((PACKAGE/'sources.json').read_text())
    for item in sources['local_dependencies']:
        require(hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256'],
                'source pin: '+item['path'])
    return sources


def quartic(entries):
    # Literal integer invariant from the pinned determinant package.
    a,b,c,d,e,f,g,h,i=entries
    return (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
            +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
            -c*d*e*h-c*d*f*g+c*e*e*g)


def binary_action(a,b,c,d):
    return sp.Matrix([[a*a,a*c,c*c],[0,a*d+b*c,0],[b*b,b*d,d*d]])


def pencil(xx,yy):
    return sp.Matrix([[xx,0],[yy,xx],[0,yy]])


def family(LL,JJ):
    return sp.Matrix([[x,JJ**2*t,JJ**3*t],
                      [y,t,x+(LL*JJ**2+JJ)*t],
                      [LL**3*t,LL**2*t,y+(LL+LL**2*JJ)*t]])


def coefficient(expr,monomial):
    return mod2(sp.Poly(sp.expand(expr),x,y,t).coeff_monomial(monomial))


def syzygy_controls():
    a0,b0,a1,b1,a2,b2=sp.symbols('a0 b0 a1 b1 a2 b2')
    v=sp.Matrix([y*y,x*y,x*x])
    col=sp.Matrix([a0*x+b0*y,a1*x+b1*y,a2*x+b2*y])
    expected=a2*x**3+(a1+b2)*x*x*y+(a0+b1)*x*y*y+b0*y**3
    require(mod2((v.T*col)[0]-expected)==0,'complete linear syzygy coefficients')
    require(all(mod2(z)==0 for z in v.T*pencil(x,y)),'moving pencil syzygies')
    return {'linear_syzygy_equations':['a2=0','b0=0','a1=b2','a0=b1']}


def extension_controls():
    b,c,f,g,h,i=sp.symbols('b c f g h i')
    M=sp.Matrix([[x,b*t,c*t],[y,t,x+f*t],[g*t,h*t,y+i*t]])
    D=M.det();ell=L*x+J*y+B*t;A2=b*h*t*t+y*(x+f*t)
    Q=mod2(sp.cancel(D/t)+A2+t*ell+ell**2)
    C=mod2(quartic(list(M))+D*ell)
    expected={x*x:h+L*L,y*y:b+J*J,x*t:i+b*g+f*h+L,
              y*t:b*i+c*h+f+J,t*t:B*B+B+b*f*g+b*h+c*g}
    for monomial,value in expected.items():
        require(mod2(coefficient(Q,monomial)-value)==0,'quadratic extension coefficient')
    require(coefficient(Q,x*y)==0,'quadratic cross coefficient')
    first={h:L*L,b:J*J,i:L+J*J*g+f*L*L}
    Q1=mod2(Q.subs(first,simultaneous=True));C1=mod2(C.subs(first,simultaneous=True))
    for monomial,value in {x**3*t:g+L**3,y**3*t:c+J**3,x*y*y*t:f+L*J*J+J}.items():
        require(mod2(coefficient(C1,monomial)-value)==0,'quartic extension coefficient')
    second={g:L**3,c:J**3,f:L*J*J+J}
    Q2=mod2(Q1.subs(second,simultaneous=True));C2=mod2(C1.subs(second,simultaneous=True))
    require(mod2(coefficient(C2,x*y*t*t)-(B+L*L*J*J))==0,'extension linear form coefficient')
    require(mod2(Q2.subs(B,L*L*J*J))==0 and mod2(C2.subs(B,L*L*J*J))==0,
            'remaining extension coefficients')
    F=family(L,J);ellF=L*x+J*y+L*L*J*J*t;DF=mod2(F.det())
    AF=F[0,1]*F[2,1]+F[1,0]*F[1,2]
    require(mod2(quartic(list(F))+DF*ellF)==0 and
            mod2(DF+t*(AF+t*ellF+ellF**2))==0,'normalized family invariant identities')
    q=mod2(sp.cancel(DF/t));qU=x*y+L*L*x*x+J*J*y*y
    require(mod2(q.subs(t,0)-qU)==0,'section quadratic')
    require(mod2(q.subs({x:x+L*J*J*t,y:y+L*t},simultaneous=True)-qU)==0,'shifted quadratic')
    return {'quadratic_coefficients':{str(m):str(mod2(v)) for m,v in expected.items()},
            'forced_parameters':{'b':'J**2','h':'L**2','g':'L**3','c':'J**3',
                                 'f':'J+L*J**2','i':'L+L**2*J','B':'L**2*J**2'},
            'family':[[str(z) for z in row] for row in F.tolist()],
            'ell':str(ellF),'D':str(DF),'q_U':str(qU),'shifted_q_equals_q_U':True}


def stabilizer_controls():
    a,b,c,d=sp.symbols('a b c d');delta=a*d+b*c
    A=binary_action(a,b,c,d);G=sp.Matrix([[a,b],[c,d]])
    require(all(mod2(z)==0 for z in A*pencil(x,y)-pencil(a*x+c*y,b*x+d*y)*G.T),
            'permitted pencil stabilizer orientation')
    require(mod2(A.det()-delta**3)==0,'binary action determinant')
    # Clearing the one remaining denominator in det(G)*q((G^T)^-1 z).
    xx=d*x+c*y;yy=b*x+a*y
    numerator=xx*yy+L*L*xx*xx+J*J*yy*yy
    require(mod2(coefficient(numerator,x*y)-delta)==0,'polar scalar cancellation')
    return {'stabilizer_identity':True,'right_outer_action':'(G.T)^-1',
            'delta_squared':'det(G)','q_transform':'det(G)*q_U((G.T)^-1*z)',
            'transformed_polar_coefficient':1}


def rank_mod2(matrix):
    basis={}
    for row in matrix.tolist():
        bits=sum((int(z)%2)<<j for j,z in enumerate(row))
        while bits:
            pivot=bits.bit_length()-1
            if pivot in basis:bits^=basis[pivot]
            else:basis[pivot]=bits;break
    return len(basis)


def kernel_dimensions(M):
    coeffs=[M.diff(z).subs(t,0) for z in (x,y)]
    return [3-rank_mod2(sp.Matrix.vstack(*coeffs)),
            3-rank_mod2(sp.Matrix.vstack(*(A.T for A in coeffs)))]


def branch_and_field_controls():
    a,c,f,g,i=sp.symbols('a c f g i')
    mixed=sp.Matrix([[a,a,c],[0,0,f],[g,g,i]])
    require(mod2(quartic(list(mixed))-(a*i+c*g)**2-a*g*f*f)==0,'mixed-kernel quartic')
    P=sp.Matrix([[x,x,0],[0,t,0],[0,y,y]])
    N=sp.Matrix([[t,x,0],[0,t,x],[0,y,0]])
    V=family(0,0)
    fixed=sp.Matrix([[x,0,0],[y,t,t+x+y],[t+x+y,0,t+x+y]])
    shear=P.T.subs({y:t+x+y},simultaneous=True)*binary_action(1,0,1,1).T
    require(all(mod2(z)==0 for z in shear-fixed),'fixed eta branch is P transpose')
    require(kernel_dimensions(fixed)==[1,1],'fixed eta branch has both kernels')
    dims={name:kernel_dimensions(M) for name,M in [('P',P),('N',N),('V',V)]}
    require(dims=={'P':[1,1],'N':[1,0],'V':[1,0]},'representative kernel dimensions')
    kernels={'P':(sp.Matrix([1,1,1]),sp.Matrix([0,1,0])),
             'N':(sp.Matrix([1,0,0]),None),'V':(sp.Matrix([0,1,0]),None)}
    for name,M in [('P',P),('N',N),('V',V)]:
        right,left=kernels[name]
        require(all(mod2(z)==0 for z in M.subs(t,0)*right),'representative right kernel')
        if left is not None:
            require(all(mod2(z)==0 for z in left.T*M.subs(t,0)),'representative left kernel')
    counts={}
    for LL,JJ in [(0,0),(1,1)]:
        F=family(LL,JJ)
        counts[f'{LL},{JJ}']=sum(int(F.subs({x:xx,y:yy,t:tt}).det())%2
                                 for xx,yy,tt in itertools.product((0,1),repeat=3))
    require(counts=={'0,0':1,'1,1':3},'GF2 form distinction')
    require(all((xx*xx+xx*yy+yy*yy)%2==1 for xx,yy in [(1,0),(0,1),(1,1)]),
            'GF2 nonsplit section quadratic')
    return {'mixed_quartic':'(a*i+c*g)**2+a*g*f**2','fixed_eta_witness_is_P_transpose':True,
            'section_kernel_dimensions_right_left':dims,'GF2_invertible_matrix_counts':counts,
            'GF2_x2_xy_y2_has_no_projective_root':True}


def report():
    check_pins()
    return {'claim':'AI-CHAR2-QUADRATIC-ATTAINERS-001',
            'proof_scope':'algebraically closed characteristic two; dim W=3; D not identically zero; geometric full-source rank <=14',
            'written_geometric_representatives':['P','N','V'],
            **syzygy_controls(),'extension':extension_controls(),
            'stabilizer':stabilizer_controls(),**branch_and_field_controls(),
            'computer_certifies_geometric_exhaustion':False,
            'arbitrary_ground_field_forms_classified':False,'independent_review':False,
            'lean_formalized':False,'improves_omega':False}


if __name__=='__main__':
    print(json.dumps(report(),indent=2))
