"""Exact chart controls; field descent and exhaustion remain written proofs."""
import hashlib
import json
from pathlib import Path
import sympy as sp

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]
b,h,t,c,F,r,k,u,v,z,s=sp.symbols('b h t c F r k u v z s')


def require(condition,label):
    if not condition:raise ArithmeticError(label)


def mod2(expr):
    expr=sp.expand(expr)
    variables=sorted(expr.free_symbols,key=str)
    return sp.Poly(expr,*variables,modulus=2).as_expr() if variables else sp.Integer(expr)%2


def zero(expr,label):
    require(mod2(sp.cancel(expr))==0,label)


def equal_matrix(left,right,label):
    for entry in left-right:zero(entry,label)


def check_pins():
    sources=json.loads((PACKAGE/'sources.json').read_text())
    for item in sources['local_dependencies']:
        require(hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256'],
                'source pin: '+item['path'])
    return sources


def binary_action(a,b,c,d):
    return sp.Matrix([[a*a,a*c,c*c],[0,a*d+b*c,0],[b*b,b*d,d*d]])


def quartic(M):
    a,b,c,d,e,f,g,h,i=list(M)
    return (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
            +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
            -c*d*e*h-c*d*f*g+c*e*e*g)


def chart():
    return sp.Matrix([[t,b,r*b+h+k*t],[t,t,F*t],
                      [c*t,h,c*c*b+(r+1)*h+u*t]])


def normal(cc=c,rr=r,hh=h):
    return sp.Matrix([[t,b,rr*b+hh+(cc**2+cc+rr**2)*t],
                      [t,t,(cc**2+rr**2+rr)*t],
                      [cc*t,hh,cc**2*b+(rr+1)*hh+(cc**3+cc**2+cc*rr**2+cc)*t]])


def initial_solution():
    return {u:c*c+c*F+c*r+c,k:F+c+r}


def shifted_parameters():
    return c+z*z+z,r+z*z,h+z*z*b+z*t


def chart_controls():
    d0,i0=sp.symbols('d0 i0')
    raw=sp.Matrix([[t,b,d0],[t,t,F*t],[c*t,h,i0]])
    delta=b*i0+d0*h
    zero(sp.cancel(mod2(raw.det())/t).subs(t,0)-delta,'raw determinant restriction')
    zero(sp.cancel(mod2(quartic(raw))/t).subs(t,0)-(h+c*b)*delta,'raw quartic restriction')
    M=chart();D=mod2(M.det());ell=c*b+h+v*t
    Q=mod2(sp.cancel(D/t)+b*h+F*t*t+t*ell+ell**2)
    C=mod2(sp.cancel(mod2(quartic(M))/t)+sp.cancel(D/t)*ell)
    expected=(F*c+c*c+c*r+c+u)*b*t+(F+c+k+r)*h*t+(F+c*k+u+v*v+v)*t*t
    zero(Q-expected,'full chart Q coefficients')
    sol=initial_solution()
    Q1=mod2(Q.subs(sol,simultaneous=True))
    C1=mod2(C.subs(sol,simultaneous=True))
    zero(Q1-(F+c+v*v+v)*t*t,'initial coefficient solution')
    Q2=mod2(Q1.subs(F,c+v*v+v));C2=mod2(C1.subs(F,c+v*v+v))
    zero(Q2,'Q after F substitution')
    zero(sp.Poly(C2,b,h,t).coeff_monomial(b*h*t)-(c+r+v)**2,'forced v coefficient')
    zero(C2.subs(v,c+r),'all remaining C coefficients')
    params={F:c*c+r*r+r,k:c*c+c+r*r,u:c**3+c*c+c*r*r+c,v:c+r}
    equal_matrix(M.subs(params,simultaneous=True),normal(),'forced normal family')
    B=normal();BE=c*b+h+(c+r)*t;BD=mod2(B.det())
    zero(quartic(B)+BD*BE,'normal full quartic identity')
    zero(BD+t*(B[0,1]*B[2,1]+B[1,0]*B[1,2]+t*BE+BE**2),'normal full determinant identity')
    zero(sp.cancel(BD/t).subs(t,0)-(c*c*b*b+b*h+h*h),'intrinsic section quadratic')
    equal_matrix(B*binary_action(1,s,0,1).T,normal(rr=r+s),'right shear')
    xx=h+(c+1)*b+t;yy=b+t
    Pc=sp.Matrix([[c*t+xx+yy,t+yy,t],[c*t,t,t],
                  [c*c*t+(c+1)*xx+yy,c*t+(c+1)*yy+xx,c*t]])
    equal_matrix(normal(rr=c),Pc*binary_action(0,1,1,0).T,'canonical P match')
    zero(sp.Matrix([t,xx,yy]).jacobian([t,b,h]).det()-1,'canonical parameter determinant')
    cc,rr,hh=shifted_parameters()
    equal_matrix(binary_action(1,z,0,1)*B,normal(cc,rr,hh),'AS shift')
    return {'raw_restrictions':True,'full_Q_coefficient_comparison':True,
            'initial_solution':{'u':str(sol[u]),'k':str(sol[k])},
            'forced_v_coefficient':'(c+r+v)^2','complete_residuals':True,
            'normal_family':[[str(e) for e in row] for row in B.tolist()],
            'section_quadratic':'c^2*b^2+b*h+h^2','right_shear':True,
            'canonical_P_match':True,'AS_shift':True}


def normalization_controls():
    a,d,g0,g1,g2,g3,h0,h1,h3=sp.symbols('a d g0 g1 g2 g3 h0 h1 h3')
    eta=sp.Matrix([0,1,0]);e0=sp.Matrix([1,0,0])
    equal_matrix(binary_action(1,0,r,1).T*e0,sp.Matrix([1,r,r*r]),'evaluation normalizer')
    G=binary_action(g0,g1,g2,g3);detg=g0*g3+g1*g2
    equal_matrix(G.T*eta,detg*eta,'eta fixed dually')
    zero(G.extract([0,2],[0,2]).det()-detg**2,'left outer block determinant')
    U=sp.Matrix([[0,b,r*b+h],[0,0,0],[0,h,a*b+d*h]])
    equal_matrix((U*binary_action(h0,h1,0,h3).T)[:,1],h0*h3*sp.Matrix([b,0,h]),'middle column rank covariance')
    equal_matrix(binary_action(1/a,0,0,1)*sp.Matrix([a,1,d])*a,
                 sp.Matrix([1,1,a*d]),'root-free first column')
    equal_matrix(binary_action(1,0,1,1)*eta,sp.Matrix([1,1,0]),'eta first column')
    # Reconstruct the pinned square-chart N shear, including the coordinate shift.
    lam,alpha,x,y=sp.symbols('lam alpha x y')
    N=sp.Matrix([[t,x,0],[0,t,x],[0,y,0]])
    bb=x+lam*t+lam*lam*y
    S=sp.Matrix([[t,bb,(alpha+lam)*bb+lam**3*y+(alpha**2+lam**2)*t],
                 [0,t,bb+lam**2*y+(alpha+lam)*t],[0,y,alpha*y]])
    equal_matrix(binary_action(1,0,lam,1)*N*binary_action(1,alpha,0,1).T,S,'square chart N shear')
    # Scalar AS necessity is valid without perfection; clear the denominator.
    A,B=sp.symbols('A B');delta=g0*g3+g1*g2
    An=g3*g1+A*g3*g3+B*g1*g1;Bn=g2*g0+A*g2*g2+B*g0*g0
    Rn=A*g2*g3+B*g0*g1+g1*g2
    zero(An*Bn+A*B*delta**2+Rn**2+Rn*delta,'AS scalar invariant')
    return {'evaluation_normalizer':True,'eta_fixed_dually':True,
            'left_outer_determinant':'det(G)^2','middle_column_rank_covariance':True,
            'root_free_P_normalizers':True,'square_chart_N_shear':True,
            'arbitrary_field_AS_scalar_identity':True}


def report():
    sources=check_pins()
    return {'source_pins_checked':len(sources['local_dependencies']),
            'chart':chart_controls(),'normalization':normalization_controls(),
            'written_P_classification_field':'every characteristic-two field',
            'written_full_classification_field':'perfect characteristic-two fields',
            'finite_field_class_count_written_corollary':5,
            'new_finite_attainer_census':False,'computer_certifies_field_descent':False,
            'computer_certifies_geometric_exhaustion':False,
            'nonperfect_N_and_V_classified':False,'independent_review':False,
            'lean_formalized':False,'compatible_tensor_map':False,'improves_omega':False}


if __name__=='__main__':
    print(json.dumps(report(),indent=2,sort_keys=True))
