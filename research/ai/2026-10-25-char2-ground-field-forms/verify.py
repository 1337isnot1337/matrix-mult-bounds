"""Exact ground-field controls; the perfect-field classification is a written proof."""
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]
x,y,t,c,lam=sp.symbols('x y t c lam')


def require(condition,label):
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


class Field:
    def __init__(self,degree,modulus):
        self.m=degree;self.q=1<<degree;self.modulus=modulus
        self.product=[[self.rawmul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inverse=[0]+[next(b for b in range(1,self.q) if self.mul(a,b)==1) for a in range(1,self.q)]
    def rawmul(self,a,b):
        out=0
        while b:
            if b&1:out^=a
            b>>=1;a<<=1
            if a&self.q:a^=self.modulus
        return out
    def mul(self,a,b):return self.product[a][b]
    def sq(self,a):return self.mul(a,a)
    def trace(self,a):
        out=0
        for _ in range(self.m):out^=a;a=self.sq(a)
        assert out in (0,1)
        return out
    def prod(self,*args):
        out=1
        for a in args:out=self.mul(out,a)
        return out
    def det(self,M):
        a,b,c,d,e,f,g,h,i=M
        return self.prod(a,e,i)^self.prod(b,f,g)^self.prod(c,d,h)^self.prod(c,e,g)^self.prod(b,d,i)^self.prod(a,f,h)
    def transform(self,A,B,G):
        a,b,c,d=G;delta=self.mul(a,d)^self.mul(b,c)
        assert delta
        AA=self.mul(self.mul(d,b)^self.mul(A,self.sq(d))^self.mul(B,self.sq(b)),self.inverse[delta])
        BB=self.mul(self.mul(c,a)^self.mul(A,self.sq(c))^self.mul(B,self.sq(a)),self.inverse[delta])
        return AA,BB
    def family(self,L,J,x,y,t):
        L2=self.sq(L);J2=self.sq(J)
        return [x,self.mul(J2,t),self.prod(J2,J,t),
                y,t,x^self.mul(self.mul(L,J2)^J,t),
                self.prod(L2,L,t),self.mul(L2,t),y^self.mul(L^self.mul(L2,J),t)]

def finite_controls(m,modulus):
    F=Field(m,modulus);q=F.q;elements=range(q)
    for a,b,c in itertools.product(elements,repeat=3):
        assert F.mul(a,b^c)==F.mul(a,b)^F.mul(a,c)
        assert F.mul(F.mul(a,b),c)==F.mul(a,F.mul(b,c))
    AS={F.sq(z)^z for z in elements}
    assert len(AS)==q//2 and AS=={z for z in elements if F.trace(z)==0}
    gl=[G for G in itertools.product(elements,repeat=4) if F.mul(G[0],G[3])^F.mul(G[1],G[2])]
    assert len(gl)==(q*q-1)*(q*q-q)
    c=next(z for z in elements if F.trace(z)==1)
    orbits=[{F.transform(*pair,G) for G in gl} for pair in [(0,0),(1,c)]]
    expected=[{(A,B) for A,B in itertools.product(elements,repeat=2) if F.trace(F.mul(A,B))==i} for i in (0,1)]
    assert orbits==expected and not (orbits[0]&orbits[1])
    action_checks=0
    for A,B in itertools.product(elements,repeat=2):
        for G in gl:
            AA,BB=F.transform(A,B,G)
            assert (F.mul(AA,BB)^F.mul(A,B)) in AS
            action_checks+=1
    counts={0:set(),1:set()}
    for L,J in itertools.product(elements,repeat=2):
        actual=sum(F.det(F.family(L,J,x,y,t))!=0 for x,y,t in itertools.product(elements,repeat=3))
        cls=F.trace(F.mul(L,J));counts[cls].add(actual)
        assert actual==((q-1)**3 if cls==0 else (q-1)**2*(q+1))
    return {'q':q,'modulus_bits':modulus,'GL2_order':len(gl),
            'all_quadratics':q*q,'weighted_orbit_sizes':[len(x) for x in orbits],
            'all_action_invariance_checks':action_checks,
            'nonsplit_c':c,'invertible_counts_by_trace':{str(k):sorted(v) for k,v in counts.items()},
            'all_family_matrix_determinants':q**5}


def binary_action(a,b,c,d):
    return sp.Matrix([[a*a,a*c,c*c],[0,a*d+b*c,0],[b*b,b*d,d*d]])


def p_twist(cc):
    return sp.Matrix([[cc*t+x+y,t+y,t],[cc*t,t,t],
                      [cc*cc*t+(cc+1)*x+y,cc*t+(cc+1)*y+x,cc*t]])


def eta_family(L,J):
    return sp.Matrix([[x,J*J*t,J**3*t],[y,t,x+(L*J*J+J)*t],
                      [L**3*t,L*L*t,y+(L+L*L*J)*t]])


def quartic(entries):
    a,b,c,d,e,f,g,h,i=entries
    return (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
            +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
            -c*d*e*h-c*d*f*g+c*e*e*g)


def arf_numerators(A,B,a,b,c,d):
    return d*b+A*d*d+B*b*b, c*a+A*c*c+B*a*a, A*c*d+B*a*b+b*c


def symbolic_controls():
    A,B,a,b,cc,d=sp.symbols('A B a b cc d');Delta=a*d+b*cc
    An,Bn,Rn=arf_numerators(A,B,a,b,cc,d)
    require(mod2(An*Bn+A*B*Delta**2+Rn**2+Rn*Delta)==0,'cleared AS identity')
    numerator=(d*x+cc*y)*(b*x+a*y)+A*(d*x+cc*y)**2+B*(b*x+a*y)**2
    require(mod2(numerator-(An*x*x+Delta*x*y+Bn*y*y))==0,'weighted quadratic coefficients')
    M=p_twist(c);D=mod2(M.det());ell=t+x+y;A2=M[0,1]*M[2,1]+M[1,0]*M[1,2]
    require(mod2(D-t*(x*x+x*y+c*y*y))==0,'P twist determinant')
    require(mod2(quartic(list(M))+D*ell)==0 and mod2(D+t*(A2+t*ell+ell**2))==0,
            'P twist integral identities')
    def reduce_root(expr):
        return mod2(sp.rem(sp.Poly(mod2(expr),lam),sp.Poly(lam*lam+lam+c,lam)).as_expr())
    bb=x+lam*y;hh=x+(lam+1)*y
    M0=sp.Matrix([[0,bb,0],[t,t,0],[0,hh,hh]])
    image=binary_action(1,lam,1,lam+1)*M0*binary_action(lam,1,1,0).T
    require(all(reduce_root(z)==0 for z in image-M),'separable P twist action')
    require(mod2(sp.Matrix([[1,lam],[1,lam+1]]).det()-1)==0 and
            mod2(sp.Matrix([[lam,1],[1,0]]).det()-1)==0,'P twist binary determinants')
    L,J=sp.symbols('L J');E=eta_family(L,J);q=sp.cancel(E.det()/t)
    require(mod2(q.subs({x:x+L*J*J*t,y:y+L*t},simultaneous=True)
                 -(x*y+L*L*x*x+J*J*y*y))==0,'eta determinant translation')
    return {'cleared_AS_identity':True,'weighted_polar_numerator':'a*d+b*cc',
            'AS_r_numerator':str(Rn),'P_twist':[[str(z) for z in row] for row in M.tolist()],
            'P_twist_D':str(D),'P_twist_ell':str(ell),'separable_P_action_verified':True,
            'eta_determinant_translation_verified':True}


def rank_bits(rows):
    basis={}
    for bits in rows:
        while bits:
            pivot=bits.bit_length()-1
            if pivot in basis:bits^=basis[pivot]
            else:basis[pivot]=bits;break
    return len(basis)


def source_rows(M):
    # Complete literal rows (j,L), columns (H,r), including endpoints.
    rows=[]
    for j in range(3):
        for L in range(5):
            row=0
            for H in range(5):
                for r in range(3):
                    if 0<=H-j<3 and 0<=L-r<3:row|=(int(M[H-j,L-r])%2)<<(3*H+r)
            rows.append(row)
    return rows


def five_GF2_forms():
    P=sp.Matrix([[x,x,0],[0,t,0],[0,y,y]])
    N=sp.Matrix([[t,x,0],[0,t,x],[0,y,0]])
    forms={'P_split':P,'P_nonsplit':p_twist(1),'N':N,
           'V_split':eta_family(0,0),'V_nonsplit':eta_family(1,1)}
    expected={'P_split':(1,[1,1]),'P_nonsplit':(3,[1,1]),'N':(1,[1,0]),
              'V_split':(1,[1,0]),'V_nonsplit':(3,[1,0])}
    output={}
    for name,M in forms.items():
        spectra={};invertible=0
        for xx,yy,tt in itertools.product((0,1),repeat=3):
            C=M.subs({x:xx,y:yy,t:tt});rows=source_rows(C)
            require(len(rows)==15 and all(z<2**15 for z in rows),'complete source dimensions')
            rank=rank_bits(rows);spectra[str(rank)]=spectra.get(str(rank),0)+1
            require(rank<=14,'literal source rank ceiling')
            if int(C.det())%2:
                invertible+=1
                require(rank==14,'invertible coefficient source rank')
        section=[M.diff(x),M.diff(y)]
        vectors=[sp.Matrix(v) for v in itertools.product((0,1),repeat=3) if any(v)]
        kr=[v for v in vectors if all(int(z)%2==0 for C in section for z in C*v)]
        kl=[v for v in vectors if all(int(z)%2==0 for C in section for z in v.T*C)]
        # Here every nonzero common kernel list has size one, hence dimension one.
        require((invertible,[len(kr),len(kl)])==expected[name],'five forms invariants')
        output[name]={'invertible_matrices':invertible,'source_rank_counts':spectra,
                      'common_right_nonzero_vectors':[list(map(int,v)) for v in kr],
                      'common_left_nonzero_vectors':[list(map(int,v)) for v in kl]}
    require(output['N']['common_right_nonzero_vectors']==[[1,0,0]] and
            output['V_split']['common_right_nonzero_vectors']==[[0,1,0]],'evaluation versus eta kernel')
    return {'forms':output,'literal_GF2_source_rank_checks':40,'pairwise_inequivalent_GF2_forms_lower_bound':5}


def report():
    check_pins()
    return {'claims':['AI-CHAR2-PERFECT-ETA-FORMS-001','AI-CHAR2-NONSPLIT-P-FORMS-001'],
            'eta_proof_scope':'perfect characteristic-two fields; common right eta kernel and no common left kernel',
            'P_twist_proof_scope':'all characteristic-two fields; explicit construction, not exhaustion',
            'symbolic':symbolic_controls(),
            'finite_fields':[finite_controls(1,0b11),finite_controls(2,0b111),finite_controls(3,0b1011)],
            **five_GF2_forms(),
            'computer_certifies_perfect_field_classification':False,
            'all_P_forms_classified':False,'complete_GF2_attainer_classification':False,
            'nonperfect_field_forms_classified':False,'independent_review':False,
            'lean_formalized':False,'improves_omega':False}


if __name__=='__main__':
    print(json.dumps(report(),indent=2))
