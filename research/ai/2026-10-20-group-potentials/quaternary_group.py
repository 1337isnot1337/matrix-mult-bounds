"""Exact F4^3 semidirect F4* group; field labels, complex group algebra.

F4 is F2[t]/(t^2+t+1). These finite-field operations define the finite group;
the matrix-multiplication target remains over C.
"""


def fm(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return out


def scale(a,v):return sum(fm(a,(v>>(2*j))&3)<<(2*j) for j in range(3))


def group():
    elements=[(a,v) for a in [1,2,3] for v in range(64)]
    index={x:i for i,x in enumerate(elements)}
    table=[[index[(fm(a,b),v^scale(a,w))] for b,w in elements] for a,v in elements]
    inverses=[index[(fm(a,a),scale(fm(a,a),v))] for a,v in elements]
    return {'name':'F4^3:C3','matrices':elements,'mul':table,'inv':inverses,
            'normal_order':64,'index':3,'identity':0}


def planes():
    # A is the graph of Frobenius in two coordinates; B,C are F4 lines.
    return [tuple(x|(fm(x,x)<<4) for x in range(4)),
            tuple(y<<2 for y in range(4)),tuple(z<<4 for z in range(4))]


def plane_family(pattern='covariant'):
    if pattern=='covariant':
        return [{a:P for a in [1,2,3]} for P in planes()]
    if pattern=='one-shear':
        axis=tuple(range(4))
        shear=tuple(x|((x&1)<<4) for x in range(4))
        return [{1:axis,2:axis,3:shear},
                {a:tuple(y<<2 for y in range(4)) for a in [1,2,3]},
                {a:tuple(z<<4 for z in range(4)) for a in [1,2,3]}]
    raise ValueError('unknown plane pattern')


def coset_representatives(subspace):
    remaining=set(range(64));reps=[]
    while remaining:
        v=min(remaining);reps.append(v)
        remaining.difference_update(v^x for x in subspace)
    return reps
