"""Independent integer coefficient replay for canonical moment-flag witnesses."""
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import argparse, hashlib, json, re

def integer_matrix(data, name, rows, columns):
    entries=data[name]
    assert len(entries)==rows and all(len(row)==columns for row in entries)
    parsed=[[Fraction(x) for x in row] for row in entries]
    assert all(x.denominator==1 for row in parsed for x in row)
    return [[x.numerator for x in row] for row in parsed]

def rank(matrix):
    work=[[Fraction(x) for x in row] for row in matrix]
    r=0
    for col in range(len(work[0])):
        pivot=next((i for i in range(r,len(work)) if work[i][col]),None)
        if pivot is None: continue
        work[r],work[pivot]=work[pivot],work[r]
        t=work[r][col]
        work[r]=[x/t for x in work[r]]
        for i in range(r+1,len(work)):
            t=work[i][col]
            work[i]=[a-t*b for a,b in zip(work[i],work[r])]
        r+=1
        if r==len(work): break
    return r

def verify(data):
    m=data.get("m",data.get("target_m"))
    source=data["source"]
    if isinstance(source,str):
        matched=re.fullmatch(r"C\((\d+),(\d+)\)",source)
        assert matched
        a,b=map(int,matched.groups())
        if m is None: m=int(data["target"].removeprefix("canonical T"))
    else: a,b=source
    assert isinstance(m,int) and m>=2
    n=m*(m+1)//2
    nodes=[(i,p-i) for p in range(m) for i in range(p+1)]
    A=integer_matrix(data,"a_map",m,a)
    Y=integer_matrix(data,"y",n,b)
    Z=integer_matrix(data,"z",n,a+b-1)
    tensor=[[[0]*n for _ in range(n)] for _ in range(m)]
    # Original source formula, independent of moment construction identities.
    for i in range(a):
        for j in range(b):
            for x in range(m):
                if not A[x][i]: continue
                for y in range(n):
                    value=A[x][i]*Y[y][j]
                    if not value: continue
                    for z in range(n):
                        tensor[x][y][z]+=value*Z[z][i+j]
    negative=constant=retained=positive=0
    remainder={str(e):0 for e in range(1,m)}
    for x,y,z in product(range(m),range(n),range(n)):
        i,j=nodes[y];k,l=nodes[z]
        e=i+j+k+l-(m-1)
        value=tensor[x][y][z]
        if e<0:
            assert value==0,("negative",x,y,z,value)
            negative+=1
        elif e==0:
            expected=int(x==i+k)
            assert value==expected,("constant",x,y,z,value,expected)
            constant+=1;retained+=expected
        elif value:
            positive+=1;remainder[str(e)]+=1
    assert negative==m*comb(m+2,4)
    assert constant==m*comb(m+2,3)
    assert retained==comb(m+2,3)
    ranks=[rank(M) for M in (A,Y,Z)]
    assert ranks==[m,n,n]
    return {
        "status":"exact integer full-source coefficient replay passed",
        "source":f"C({a},{b})","source_dimensions":[a,b,a+b-1],
        "target":f"canonical T{m}","target_dimensions":[m,n,n],
        "coefficient_ring":"integers; specializes to every field",
        "source_monomials":a*b,"target_coefficient_positions":m*n*n,
        "negative_coefficients_checked":negative,
        "constant_coefficients_checked":constant,"retained_target_monomials":retained,
        "nonzero_positive_remainder_coefficients":positive,
        "nonzero_remainder_coefficients_by_degree":remainder,
        "map_ranks_over_rationals":ranks,
        "maximum_absolute_map_entry":max(abs(x) for M in (A,Y,Z) for row in M for x in row),
        "verifier_uses_only_standard_library":True,
        "unbounded_family_constructed":False,"external_mathematical_review":False,
        "improves_omega":False}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("witness",type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    raw=args.witness.read_bytes()
    report=verify(json.loads(raw))
    report["witness_sha256"]=hashlib.sha256(raw).hexdigest()
    text=json.dumps(report,indent=2)+"\n"
    if args.output: args.output.write_text(text)
    print(text)
