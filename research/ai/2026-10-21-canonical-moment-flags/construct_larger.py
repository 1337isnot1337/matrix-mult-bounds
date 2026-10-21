"""Reconstruct integer canonical T5, T6, and T7 maps from literal moments."""
from fractions import Fraction
from pathlib import Path
import argparse,json

SPEC=json.loads(r'''{"5":{"b":16,"g":[[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,-1,0,0,0,0,0,1,0,1,1,1,1,1,1],[1,0,0,0,0,0,-1,1,-1,-1,-1,-1,-1,-1],[0,0,-1,1,0,0,0,0,0,0,1,0,0],[0,0,-1,1,0,0,0,0,0,0,0,1]],"moments":[[0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0],[-1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,-1],[-1,0,0,0,-1,1,-1,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0]]},"6":{"b":24,"g":[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0,0,0,0,-1,1,0,0,1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,1,0,0,0,-1,-1,-1,-1,1,-1,-2,-3,-4,-4,-4,-4,-3,-2,-1],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,1]],"moments":[[0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],[-1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1],[-4,2,0,-2,3,-1,0,-2,1,0,-1,2,-1,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0],[2,-5,5,-1,-3,5,-4,1,-2,1,0,-1,2,-3,1,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,-2,3],[0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0]]},"7":{"b":34,"g":[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,-1,0,0,-1,-1,-1,-1,-1,-1,-1,-1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,-1,0,0,1,0,0,1,0,1,-1,-1,-1,-1,-1,-1,-1,-1],[0,0,0,0,1,-1,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]],"moments":[[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1],[0,0,0,1,0,0,0,0,0,0,0,-2,0,0,1,0,0,0,0,-1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,-1,0,1,-1,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0]]}}''')

def inverse_unit(matrix):
    n=len(matrix)
    work=[[Fraction(x) for x in row]+[Fraction(i==j) for j in range(n)]
          for i,row in enumerate(matrix)]
    determinant=1
    for k in range(n):
        p=next(i for i in range(k,n) if work[i][k])
        if p!=k:
            work[p],work[k]=work[k],work[p]
            determinant=-determinant
        value=work[k][k]
        assert abs(value)==1
        determinant*=value
        work[k]=[x/value for x in work[k]]
        for i in range(n):
            if i==k: continue
            value=work[i][k]
            work[i]=[a-value*b for a,b in zip(work[i],work[k])]
    assert all(x.denominator==1 for row in work for x in row)
    return [[int(x) for x in row[n:]] for row in work],int(determinant)

def construct(m):
    data=SPEC[str(m)]
    b=data["b"];a=m+1
    g=data["g"];moments=data["moments"]
    powers=[i for i in range(m+1) if i!=2]
    assert [len(row) for row in g]==[b-p for p in range(m)]
    assert [len(row) for row in moments]==[b+m+q for q in range(m)]
    H=[[int(d+k==m-1)-int(d+k==m) for k in range(m)] for d in powers]
    inverse,determinant=inverse_unit(H)
    A=[[0 if i==2 else row[powers.index(i)] for i in range(a)] for row in inverse]
    nodes=[(k,p-k) for p in range(m) for k in range(p+1)]
    Y=[];Z=[]
    for p in range(m):
        for k in range(p+1):
            Y.append([g[p][j-k] if 0<=j-k<len(g[p]) else 0 for j in range(b)])
            Z.append(moments[p][k:k+a+b-1])
    # These scalar equations explain the construction. The independent
    # verifier substitutes into the original source instead.
    for p in range(m):
        for q in range(m-p):
            shifts={d+k for d in powers for k in range(p+q+1)}
            for ell in shifts:
                value=sum(g[p][j]*moments[q][j+ell] for j in range(b-p))
                target=(int(ell==m-1)-int(ell==m)) if p+q==m-1 else 0
                assert value==target,(m,p,q,ell,value,target)
    return {"source":[a,b],"m":m,"target":"canonical T"+str(m),
            "a_map":A,"y":Y,"z":Z,"block_factors":g,"block_moments":moments,
            "shared_hankel_matrix":H,"shared_hankel_determinant":determinant,
            "weights_x":[1-m]*m,"weights_y":[sum(node) for node in nodes],
            "weights_z":[sum(node) for node in nodes],
            "coefficient_ring":"integers","improves_omega":False}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m",type=int,choices=(5,6,7),required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    args.output.write_text(json.dumps(construct(args.m),indent=2)+"\n")
