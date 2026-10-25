"""Exact identities and a complete GF2 pencil census; not a proof formalization."""
import hashlib
import itertools
import json
from pathlib import Path
import sympy as sp

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]


def check_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for item in sources['local_dependencies']:
        if hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ArithmeticError('source pin: ' + item['path'])
    return sources


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def adjugate_form(N):
    return N[1, 1]**2+N[1, 0]*N[1, 2]+N[0, 1]*N[2, 1]+N[0, 0]*N[2, 2]


def conic(u):
    return u[1]**2+u[0]*u[2]


def integer_quartic(entries):
    a,b,c,d,e,f,g,h,i=entries
    return (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
            +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
            -c*d*e*h-c*d*f*g+c*e*e*g)


def adjugate_controls():
    entries=sp.symbols('a b c d e f g h i')
    M=sp.Matrix(3,3,entries)
    require(mod2zero(adjugate_form(M.adjugate())-integer_quartic(entries)-M[1,1]*M.det(),entries),
            'literal adjugate identity')
    u=sp.Matrix(sp.symbols('u0:3'));v=sp.Matrix(sp.symbols('v0:3'))
    require(mod2zero(adjugate_form(u*v.T)-conic(u)*conic(v),tuple(u)+tuple(v)),
            'rank-one conic factorization')
    return {'adjugate_identities': 2}


def pointwise_zero(poly, degree):
    # Homogeneous evaluation at (s,t)=(1,0),(0,1),(1,1).
    return poly&1 == 0 and (poly>>degree)&1 == 0 and bin(poly).count('1')%2 == 0


def pointwise_trap():
    a,b=10,162
    entries=[((a>>j)&1)+2*((b>>j)&1) for j in range(9)]
    D,T=inv(entries)
    dimensions=[3-rank(rowbits(a)+rowbits(b)),3-rank(colbits(a)+colbits(b))]
    require(D==0 and T==12 and pointwise_zero(D,3) and pointwise_zero(T,4), 'pointwise polynomial distinction')
    require(dimensions==[0,0], 'pointwise trap has no common kernel')
    s,t=sp.symbols('s t')
    M=sp.Matrix([[0,s+t,0],[s,0,t],[0,t,0]])
    u=sp.Matrix([t,0,s]);v=sp.Matrix([t,0,s+t])
    require(all(mod2zero(entry,(s,t)) for entry in M.adjugate()-u*v.T), 'trap adjugate factors')
    require(mod2zero(integer_quartic(list(M))-s*t*t*(s+t),(s,t)), 'trap quartic')
    return {'basis_bits':[a,b],'D_polynomial_bits':D,'T4_polynomial_bits':T,
            'T4_homogeneous':'s*t**2*(s+t)','common_kernel_dimensions':dimensions,
            'vanishes_at_all_GF2_projective_points':True,'polynomial_T4_zero':False}


def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        a<<=1;b>>=1
    return out

def prod(*args):
    out=1
    for a in args:out=mul(out,a)
    return out

def inv(entries):
    a,b,c,d,e,f,g,h,i=entries
    D=prod(a,e,i)^prod(b,f,g)^prod(c,d,h)^prod(c,e,g)^prod(b,d,i)^prod(a,f,h)
    T=(prod(a,a,i,i)^prod(a,b,h,i)^prod(a,c,h,h)^prod(a,d,f,i)^prod(a,f,f,g)
       ^prod(b,b,g,i)^prod(b,c,g,h)^prod(b,d,f,h)^prod(b,e,f,g)^prod(c,c,g,g)
       ^prod(c,d,d,i)^prod(c,d,e,h)^prod(c,d,f,g)^prod(c,e,e,g))
    return D,T

def rank(rows):
    basis={}
    for row in rows:
        while row:
            j=row.bit_length()-1
            if j in basis:row^=basis[j]
            else:basis[j]=row;break
    return len(basis)

def rowbits(n):return [(n>>(3*j))&7 for j in range(3)]
def colbits(n):return [sum(((n>>(3*r+c))&1)<<r for r in range(3)) for c in range(3)]

def generic_rank_one(entries):
    return all(mul(entries[3*r+c],entries[3*s+d])^mul(entries[3*r+d],entries[3*s+c])==0
               for r,s in itertools.combinations(range(3),2) for c,d in itertools.combinations(range(3),2))

def mod2zero(expr,vars):return sp.Poly(sp.expand(expr),*vars,modulus=2).is_zero

def symbolic_controls():
    a=sp.symbols('a0:3');b=sp.symbols('b0:3');vars=a+b
    qa=a[1]**2+a[0]*a[2];qb=b[1]**2+b[0]*b[2]
    B=a[0]*b[2]+a[2]*b[0]
    p01=a[0]*b[1]+a[1]*b[0];p12=a[1]*b[2]+a[2]*b[1]
    require(mod2zero(p01**2+a[0]*b[0]*B+a[0]**2*qb+b[0]**2*qa,vars), "first Plucker identity")
    require(mod2zero(p12**2+a[2]*b[2]*B+a[2]**2*qb+b[2]**2*qa,vars), "second Plucker identity")
    # Differential-check the bit-polynomial implementation against literal symbolic formulas.
    z=sp.symbols('z')
    pairs=[(1,2),(17,257),(273,84),(511,254),(60,399),(128,271),(3,256),(73,146)]
    for aa,bb in pairs:
        bits=[((aa>>j)&1)+2*((bb>>j)&1) for j in range(9)]
        entries=[((aa>>j)&1)+z*((bb>>j)&1) for j in range(9)]
        M=sp.Matrix(3,3,entries)
        T=integer_quartic(entries)
        for expression,encoded in zip((M.det(),T),inv(bits)):
            actual=sum((int(sp.expand(expression).coeff(z,j))%2)<<j for j in range(5))
            require(encoded==actual, "literal polynomial encoding")
    return {'conic_line_plucker_identities':2,'literal_polynomial_comparisons':16}

def census():
    count=singular=eligible=one=0;dimensions={};violations=[]
    for a in range(1,512):
        for b in range(a+1,512):
            if (a^b)<=b:continue
            count+=1
            entries=[((a>>j)&1)+2*((b>>j)&1) for j in range(9)]
            D,T=inv(entries)
            if D:continue
            singular+=1
            if T:continue
            eligible+=1;one+=generic_rank_one(entries)
            kr=3-rank(rowbits(a)+rowbits(b));kl=3-rank(colbits(a)+colbits(b))
            key=f'{kr},{kl}';dimensions[key]=dimensions.get(key,0)+1
            if kr==kl==0:violations.append([a,b])
    require(count==43435 and not violations, "complete pencil census")
    return {'scope':'all GF2 2D coefficient spaces, polynomial D=T4=0',
        'all_two_spaces':count,'singular_two_spaces':singular,'singular_T4_zero':eligible,
        'eligible_generic_rank_at_most_one':one,'common_kernel_dimensions':dimensions,
        'violations':violations}


def report():
    check_pins()
    return {'claim':'AI-CHAR2-SINGULAR-PENCIL-KERNEL-001',
            'proof_scope':'every field of characteristic two, polynomial hypotheses',
            **adjugate_controls(), **symbolic_controls(), 'census':census(),
            'pointwise_trap':pointwise_trap(),
            'finite_census_is_arbitrary_field_proof':False,
            'computer_certifies_UFD_factorization_or_degree_argument':False,
            'complete_char2_attainer_classification':False,
            'independent_review':False,'lean_formalized':False,'improves_omega':False}


if __name__=='__main__':
    print(json.dumps(report(),indent=2))
