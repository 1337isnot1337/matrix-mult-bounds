"""Exact sparse coefficient replay for alternating-degree packing.

No floating arithmetic, symbolic algebra package, or optimizer is used.
All generated coefficients and powers are integers.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import comb
from pathlib import Path


def blocks(m: int) -> list[dict]:
    if m < 1:
        raise ValueError("m must be positive")
    d = m-1
    result = []
    for i in range(d//2+1):
        result.append(dict(degree=i, start=i*m+i*i, high=0))
        if i < d-i:
            result.append(dict(degree=d-i, start=i*m+(i+1)**2, high=1))
    assert sorted(b['degree'] for b in result) == list(range(m))
    return result


def witness(m: int, k: int = 1) -> dict:
    if k < 1:
        raise ValueError("k must be positive")
    d = m-1
    n = m*(m+1)//2
    period = n+d*d//4
    shortfall = d//2
    length = k*period-shortfall
    y, z = [], []
    for r in range(k):
        for block in blocks(m):
            p, start, high = block['degree'], block['start'], block['high']
            weight = high-2*r
            for a in range(p+1):
                y.append(dict(source=r*period+start+p-a,
                              target=[r,a,p-a], weight=weight))
            for c in range(d-p+1):
                z.append(dict(source=r*period+start+p+c,
                              target=[r,c,d-p-c], weight=-weight))
    return dict(m=m,k=k,D=d,N=n,period=period,B=length,
                source_format=[m,length,length+d],target_format=[m,k*n,k*n],
                shared_map='identity',y=y,z=z)


def target_coefficients(m: int, k: int) -> Counter:
    target = Counter()
    d = m-1
    for r in range(k):
        for a in range(m):
            for b in range(m-a):
                for c in range(m-a-b):
                    e = d-a-b-c
                    target[(a+c,(r,a,b),(r,c,e))] += 1
    return target


def verify(data: dict) -> dict:
    m,k,length = data['m'],data['k'],data['B']
    n,d = data['N'],m-1
    y = {entry['source']:entry for entry in data['y']}
    z = {entry['source']:entry for entry in data['z']}
    assert len(y) == len(data['y']) == k*n, 'Y coordinates must be distinct'
    assert len(z) == len(data['z']) == k*n, 'Z coordinates must be distinct'
    assert all(0 <= j < length for j in y), 'Y index outside source'
    assert all(0 <= j < length+d for j in z), 'Z index outside source'
    assert len({tuple(x['target']) for x in y.values()}) == k*n
    assert len({tuple(x['target']) for x in z.values()}) == k*n
    actual = Counter()
    source_terms = 0
    for shared in range(m):
        for j in range(length):
            source_terms += 1
            if j in y and j+shared in z:
                yy,zz = y[j],z[j+shared]
                power = yy['weight']+zz['weight']
                actual[(power,shared,tuple(yy['target']),tuple(zz['target']))] += 1
    assert all(power >= 0 for power,_,_,_ in actual), 'negative Laurent coefficient'
    constant = Counter({(i,yy,zz):coefficient
                        for (power,i,yy,zz),coefficient in actual.items() if power == 0})
    wanted = target_coefficients(m,k)
    assert constant == wanted, 'constant tensor differs from target'
    assert sum(constant.values()) == k*comb(m+2,3)
    counts = Counter()
    for (power,_,_,_),coefficient in actual.items():
        counts[power] += coefficient
    encoded = json.dumps(sorted((power,i,list(yy),list(zz),coefficient)
                                for (power,i,yy,zz),coefficient in actual.items()),
                         separators=(',',':')).encode()
    expected_length = k*((3*m*m+3)//4)-(m-1)//2
    assert length == expected_length
    return dict(m=m,k=k,N=n,B=length,
                matching_prior_lower_bound=expected_length,
                source_terms_enumerated=source_terms,
                target_coefficient_space=m*(k*n)**2,
                retained_terms=sum(constant.values()),
                coefficient_count_by_power={str(p):counts[p] for p in sorted(counts)},
                full_laurent_tensor_sha256=sha256(encoded).hexdigest(),
                verified=True)


def report(max_m: int = 40, max_k: int = 3) -> dict:
    cases = [verify(witness(m,k)) for m in range(1,max_m+1)
             for k in range(1,max_k+1)]
    return dict(status='exact construction; no smaller matrix multiplication exponent',
                statement='C(m, k*ceil(3*m^2/4)-floor((m-1)/2)) degenerates to T_(m,k) with identity shared map',
                all_size_proof='research/ai/2026-10-20-alternating-degree-packing/README.md',
                prior_finite_control='research/ai/2026-10-20-mixed-restrictions/README.md',
                prior_matching_lower_bound='research/ai/2026-10-20-koszul/arbitrary_shared_basis.md',
                max_m=max_m,max_k=max_k,case_count=len(cases),
                source_terms_enumerated=sum(x['source_terms_enumerated'] for x in cases),
                target_coefficients_verified=sum(x['target_coefficient_space'] for x in cases),
                new_exponent_established=False,independent_external_review=False,
                m4_k1_witness=witness(4,1),cases=cases)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-m',type=int,default=40)
    parser.add_argument('--max-k',type=int,default=3)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    result = report(args.max_m,args.max_k)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items()
                      if key not in ('cases','m4_k1_witness')},indent=2))


if __name__ == '__main__':
    main()
