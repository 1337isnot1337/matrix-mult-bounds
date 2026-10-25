"""Exact root-free descent controls; geometric exhaustion remains a written proof."""
import hashlib
import json
from pathlib import Path
import sympy as sp

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]
x,y,t,L,J,z,a=sp.symbols('x y t L J z a')
b,h,C,A,B,lam,mu,k,alpha,d,i=sp.symbols('b h C A B lam mu k alpha d i')


def require(condition,label):
    if not condition:raise ArithmeticError(label)


def mod2(expr):
    expr=sp.expand(expr)
    variables=sorted(expr.free_symbols,key=str)
    return sp.Poly(expr,*variables,modulus=2).as_expr() if variables else sp.Integer(expr)%2


def zero(expr,label):
    numerator,denominator=sp.fraction(sp.cancel(expr))
    require(mod2(denominator)!=0,'zero characteristic-two denominator: '+label)
    require(mod2(numerator)==0,label)


def equal(left,right,label):
    for entry in left-right:zero(entry,label)


def check_pins():
    sources=json.loads((PACKAGE/'sources.json').read_text())
    for item in sources['local_dependencies']:
        require(hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256'],
                'source pin: '+item['path'])
    return sources


def binary_action(g):
    a,b,c,d=list(g)
    return sp.Matrix([[a*a,a*c,c*c],[0,a*d+b*c,0],[b*b,b*d,d*d]])


def n_chart():
    return sp.Matrix([[t,b,d],[0,t,A*b+B*h+k*t],[C*t,h,i]])


def forced_root():return lam+C*mu


def n_controls():
    M=n_chart();D=mod2(M.det());ell=lam*b+mu*h+alpha*t
    Q=mod2(sp.cancel(D/t)+b*h+t*ell+ell**2)
    restriction=Q.subs(t,0)
    expected=(A*C+lam*lam)*b*b+(A+B*C+1)*b*h+(B+mu*mu)*h*h
    zero(restriction-expected,'N restricted coefficients')
    reduced=mod2(restriction.subs({A:1+C*mu*mu,B:mu*mu},simultaneous=True))
    zero(reduced-(forced_root()**2+C)*b*b,'N forced root')
    r=sp.symbols('r')
    equal(binary_action(sp.Matrix([[1,r],[0,1]]))*sp.Matrix([1,0,r*r]),
          sp.Matrix([1,0,0]),'N root normalizer')
    g0,g1,g2,g3,h0,h1,h3=sp.symbols('g0 g1 g2 g3 h0 h1 h3')
    G=binary_action(sp.Matrix([[g0,g1],[g2,g3]]));delta=g0*g3+g1*g2
    zero(G.extract([0,2],[0,2]).det()-delta**2,'N outer column rank')
    U=sp.Matrix([[0,b,d],[0,0,k],[0,h,i]])
    H=binary_action(sp.Matrix([[h0,h1],[0,h3]]))
    equal((U*H.T)[:,1],h0*h3*sp.Matrix([b,0,h]),'N middle column covariance')
    return {'restricted_Q':str(mod2(restriction)),
            'forced_B':'mu^2','forced_A':'1+C*mu^2','forced_root_C':str(forced_root()),
            'root_normalizer':True,'middle_column_covariance':True,
            'left_outer_determinant':'det(G)^2',
            'geometric_middle_column_rank_transfer_is_written_argument':True}


def section(x,y):return sp.Matrix([[x,0],[y,x],[0,y]])


def eta_family(L,J,x=x,y=y,t=t):
    return sp.Matrix([[x,J*J*t,J**3*t],[y,t,x+(L*J*J+J)*t],
                      [L**3*t,L*L*t,y+(L+L*L*J)*t]])


def section_normalizer(C):
    p,q,r,w=list(C);delta=p*w+q*r;adj=sp.Matrix([[w,q],[r,p]])
    return adj.T,delta*adj*sp.Matrix([x,y]),delta


def v_section_controls():
    aa,bb,l0,l2=sp.symbols('aa bb l0 l2')
    v=sp.Matrix([aa*l0*l0,bb*l0*l2,bb*bb*l2*l2/aa])
    xx=bb*l2/aa;yy=l0
    equal(v/aa,sp.Matrix([yy*yy,xx*yy,xx*xx]),'primitive conic parametrization')
    p,q,r,w=sp.symbols('p q r w');C=sp.Matrix([[p,q],[r,w]])
    G,zz,delta=section_normalizer(C)
    zero(G.det()-delta,'V left normalizer determinant')
    equal(binary_action(G)*section(x,y)*C,section(*zz),'V left section normalizer')
    zero(zz.jacobian([x,y]).det()-delta**3,'V section parameter determinant')
    # A concrete nonperfect-field example, as an identity over F2(s).
    ss=sp.symbols('s');CC=sp.diag(ss,1);GG=sp.diag(1,ss)
    equal(binary_action(GG)*section(x,y)*CC,section(ss*x,ss*ss*y),'F2(s) section normalization')
    return {'primitive_conic_parametrization':True,'left_normalizer':'adj(C)^transpose',
            'new_parameters':'det(C)*adj(C)*(x,y)^transpose',
            'parameter_determinant':'det(C)^3','F2(s)_example_verified':True,
            'no_square_roots_extracted':True}


def square_binary(T):return T.applyfunc(lambda entry:entry**2)


def generators():
    return [
        ('diagonal',sp.diag(a,1),sp.diag(1/a,1),L/a,a*J,(a*t,a*a*x,y)),
        ('lower',sp.Matrix([[1,0],[z,1]]),sp.Matrix([[1,z],[0,1]]),L,J+z+L*z*z,
         (t,x+z*z*y+L**3*z**4*t,y)),
        ('upper',sp.Matrix([[1,z],[0,1]]),sp.Matrix([[1,0],[z,1]]),L+z+J*z*z,J,
         (t,x+(J**3*z*z+J*J*z)*t,y+z*z*x+(J*J*L*z*z+J*z*z+z)*t))]


def v_stabilizer_controls():
    rows=[]
    for label,T,H,LL,JJ,coords in generators():
        G=square_binary(T);tt,xx,yy=coords
        equal(G.T*square_binary(H),sp.eye(2),'V paired stabilizer relation: '+label)
        image=binary_action(G)*eta_family(L,J)*binary_action(H).T
        equal(image,eta_family(LL,JJ,xx,yy,tt),'V whole-family stabilizer: '+label)
        zero(sp.Matrix(coords).jacobian([t,x,y]).det()-T.det()**3,'V parameter determinant: '+label)
        rows.append({'generator':label,'L_new':str(LL),'J_new':str(JJ),
                     'parameters_t_x_y':[str(v) for v in coords],
                     'parameter_determinant':str(T.det()**3)})
    # Necessity of the AS class is a scalar coefficient identity over every K.
    aa,bb,cc,dd,U,V=sp.symbols('aa bb cc dd U V');delta=aa*dd+bb*cc
    Un=dd*bb+U*dd*dd+V*bb*bb;Vn=cc*aa+U*cc*cc+V*aa*aa
    Rn=U*cc*dd+V*aa*bb+bb*cc
    zero(Un*Vn+U*V*delta**2+Rn**2+Rn*delta,'arbitrary-field AS invariant')
    return {'generators':rows,'diagonal_requires_a_nonzero':True,
            'arbitrary_field_AS_scalar_identity':True,'no_square_roots_extracted':True}


def report():
    sources=check_pins()
    return {'source_pins_checked':len(sources['local_dependencies']),
            'N':n_controls(),'V_section':v_section_controls(),'V_stabilizers':v_stabilizer_controls(),
            'written_classification_field':'every characteristic-two field',
            'written_classes':'(K/AS(K))_P disjoint-union {N} disjoint-union (K/AS(K))_V',
            'V_class_representative':'M_(1,c)',
            'new_finite_census':False,'computer_certifies_field_descent':False,
            'computer_certifies_geometric_exhaustion':False,'independent_review':False,
            'lean_formalized':False,'compatible_tensor_map':False,'improves_omega':False}


if __name__=='__main__':print(json.dumps(report(),indent=2,sort_keys=True))
