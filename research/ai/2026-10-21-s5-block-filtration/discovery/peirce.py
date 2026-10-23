"""Exploration only: modular S5 idempotents and corner/radical dimensions."""
import json
from pathlib import Path
import sys
from functools import lru_cache

PACKAGE=Path(__file__).resolve().parents[1]
ROOT=PACKAGE.parents[2]
sys.path.insert(0,str(PACKAGE.parent/'2026-10-21-s5-split'))
import radical


def indices(x):
    while x:
        b=x & -x
        yield b.bit_length()-1
        x^=b


def solver(vectors):
    basis={}
    for i,x in enumerate(vectors):
        label=1<<i
        while x:
            p=x.bit_length()-1
            if p not in basis:
                basis[p]=(x,label)
                break
            r,l=basis[p]
            x^=r
            label^=l
    def solve(x):
        label=0
        while x:
            p=x.bit_length()-1
            if p not in basis:
                raise ValueError('not in image')
            r,l=basis[p]
            x^=r
            label^=l
        return label
    return solve


def xor(values):
    out=0
    for x in values:
        out^=x
    return out


def run():
    G=radical.group()
    reps=radical.representations(G)[:2]
    images=[1|(reps[0][g]<<1)|(reps[1][g]<<17) for g in range(120)]
    preimage=solver(images)
    @lru_cache(maxsize=25000)
    def translate(g,b):
        return xor(1<<G['mul'][g][h] for h in indices(b))
    def mul(a,b):
        return xor(translate(g,b) for g in indices(a))
    def image(a):
        return xor(images[g] for g in indices(a))
    idempotents=[]
    remaining=1
    for slot in [0]+list(range(1,17,5))+list(range(17,33,5)):
        a=preimage(1<<slot)
        a=mul(mul(remaining,a),remaining)
        for _ in range(3):
            a=mul(a,a)
        assert mul(a,a)==a and image(a)==1<<slot
        for e in idempotents:
            assert mul(e,a)==mul(a,e)==0
        idempotents.append(a)
        remaining^=a
    assert remaining==0
    powers=json.loads((ROOT/'results/s5-split-2026-10-21/radical-pilot.json').read_text())['power_bases']
    powers=[[1<<g for g in range(120)]]+[[int(v,16) for v in row] for row in powers]
    corners=[]
    for i,e in enumerate(idempotents):
        for j,f in enumerate(idempotents):
            corner=[]
            for power in powers:
                b={}
                for v in power:
                    radical.insert(mul(mul(e,v),f),b)
                corner.append(list(b.values()))
            if corner[0]:
                corners.append({'i':i,'j':j,'power_dimensions':[len(p) for p in corner],
                                'bases':[[hex(v) for v in p] for p in corner]})
    report={'idempotents':[hex(v) for v in idempotents],'corners':corners}
    (PACKAGE/'discovery/peirce.json').write_text(json.dumps(report,indent=2)+'\n')
    print('idempotents', [hex(v) for v in idempotents],flush=True)
    for c in corners:
        print(c['i'],c['j'],c['power_dimensions'],flush=True)

if __name__=='__main__':
    run()
