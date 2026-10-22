"""Exact characteristic-two SL2 F8 modules and radical powers."""
from functools import lru_cache
from pathlib import Path
from itertools import product
import json
import sys
import time

PACKAGE=Path(__file__).resolve().parent
HERE=PACKAGE.parents[2]/'results/sl2-f8-modular-2026-10-21'
sys.path.insert(0,str(PACKAGE.parent/'2026-10-21-semisimple-koszul'))
sys.path.insert(0,str(PACKAGE.parent/'2026-10-21-s5-split'))
from sl2_f8_source import group, fm
from radical import kernel,insert

M=[[fm(a,b) for b in range(8)] for a in range(8)]

def bits(x):
    while x:
        b=x&-x
        yield b.bit_length()-1
        x^=b


def xor(xs):
    out=0
    for x in xs:
        out^=x
    return out


def field_power(a,n):
    v=1
    for _ in range(n):
        v=M[v][a]
    return v


def modules(G):
    natural=[];second=[];steinberg=[];perms=[]
    for a,b,c,d in G['matrices']:
        natural.append((a,c,b,d)) # column-major
        N=[[a,b],[c,d]]
        second.append(tuple(M[N[i//2][j//2]][M[N[i%2][j%2]][N[i%2][j%2]]]
                            for j in range(4) for i in range(4)))
        p=[]
        for x in range(9):
            numerator=a if x==8 else M[a][x]^b
            denominator=c if x==8 else M[c][x]^d
            p.append(8 if denominator==0 else M[numerator][field_power(denominator,6)])
        assert sorted(p)==list(range(9))
        perms.append(p)
        columns=[((1<<p[i])^(1<<p[8]))&255 for i in range(8)]
        steinberg.append(sum(col<<(8*i) for i,col in enumerate(columns)))
    def check_field(rep,n):
        # Precompute each output column times each scalar of F8.
        ops=[[[sum(M[v][A[n*j+i]]<<(3*i) for i in range(n)) for v in range(8)]
              for j in range(n)] for A in rep]
        for g in range(504):
            op=ops[g]
            for h in range(504):
                B=rep[h]
                actual=tuple((xor(op[i][B[n*j+i]] for i in range(n))>>(3*r))&7
                             for j in range(n) for r in range(n))
                if actual!=rep[G['mul'][g][h]]:
                    raise ArithmeticError('F8 representation failed')
        return 504**2
    counts=[check_field(natural,2),check_field(second,4)]
    actions=[[xor((A>>(8*j))&255 for j in bits(v)) for v in range(256)] for A in steinberg]
    for g in range(504):
        for h in range(504):
            B=steinberg[h]
            actual=sum(actions[g][(B>>(8*j))&255]<<(8*j) for j in range(8))
            if actual!=steinberg[G['mul'][g][h]]:
                raise ArithmeticError('F2 representation failed')
    images=[1 | (sum(v<<(3*i) for i,v in enumerate(N))<<1)
             | (sum(v<<(3*i) for i,v in enumerate(T))<<13) | (S<<61)
             for N,T,S in zip(natural,second,steinberg)]
    return images,{'field_representation_products_checked':sum(counts),
                   'binary_representation_products_checked':504**2,
                   'natural':natural,'tensor':second,'steinberg':steinberg}


def explore():
    start=time.monotonic();G=group();images,receipt=modules(G)
    print('modules checked',time.monotonic()-start,flush=True)
    rows=[sum(1<<g for g in range(504) if images[g]>>i&1) for i in range(125)]
    J=kernel(rows,504)
    print('kernel',len(J),flush=True)
    translates=[[xor(1<<G['mul'][g][h] for h in bits(v)) for v in J] for g in range(504)]
    previous=J;dims=[504,len(J)];powers=[J]
    print('translation table ready',time.monotonic()-start,flush=True)
    for k in range(2,30):
        span={}
        for a in previous:
            supp=list(bits(a))
            for j in range(len(J)):
                insert(xor(translates[g][j] for g in supp),span)
        previous=list(span.values());dims.append(len(previous));powers.append(previous)
        print('power',k,'dim',len(previous),'seconds',time.monotonic()-start,flush=True)
        if not previous or len(previous)==dims[-2]:break
    value={'group':'SL(2,F8)','image_dimension':504-len(J),'power_dimensions':dims,
           'powers':[[hex(v) for v in row] for row in powers],**receipt}
    (HERE/'modules-powers.json').write_text(json.dumps(value,indent=2)+'\n')

if __name__=='__main__':explore()
