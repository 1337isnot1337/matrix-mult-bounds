"""Replay finite congruences only; this is not a characteristic-zero existence test."""
import hashlib
import json
from pathlib import Path

def verify_lift(w,lift):
    m=w["m"];a,B=w["source"];out=a+B-1;N=m*(m+1)//2
    bits=lift["bits"];modulus=1<<bits;x=lift["parameters_mod"]
    oy=m*a;oz=oy+N*B;nvar=oz+N*out
    if bits<1 or len(x)!=nvar or any(v<0 or v>=modulus for v in x):
        raise ValueError("finite lift format")
    old=[]
    for v in w["U"]:old.extend((v>>i)&1 for i in range(a))
    for group in w["Y"]:
        for v in group:old.extend((v>>i)&1 for i in range(B))
    for group in w["Z"]:
        for v in group:old.extend((v>>i)&1 for i in range(out))
    if any((v&1)!=b for v,b in zip(x,old)):raise ValueError("wrong residue point")
    U=[x[a*i:a*(i+1)] for i in range(m)]
    Y=[x[oy+B*i:oy+B*(i+1)] for i in range(N)]
    Z=[x[oz+out*i:oz+out*(i+1)] for i in range(N)]
    products={}
    def coeff(i,y,z):
        if (i,y) not in products:
            v=[0]*out
            for k,u in enumerate(U[i]):
                if u:
                    for j,yy in enumerate(Y[y]):
                        if yy:v[k+j]=(v[k+j]+u*yy)%modulus
            products[i,y]=v
        return sum(u*v for u,v in zip(products[i,y],Z[z]))%modulus
    def idx(p,j):return p*(p+1)//2+j
    count=0
    for p in range(m):
        for q in range(m-p-1):
            for i in range(m):
                for j in range(p+1):
                    for k in range(q+1):
                        if coeff(i,idx(p,j),idx(q,k)):raise ValueError("negative congruence")
                        count+=1
    for p in range(1,m-1):
        q=m-1-p
        for i in range(m):
            for j in range(1,p+1):
                for k in range(q):
                    if (coeff(i,idx(p,j),idx(q,k))-coeff(i,idx(p,j-1),idx(q,k+1)))%modulus:
                        raise ValueError("Hankel congruence")
                    count+=1
    return {"precision_bits":bits,"equations_checked":count,"parameters":nvar,
            "scope":"finite congruences only; no characteristic-zero existence conclusion"}

if __name__=="__main__":
    root=Path(__file__).resolve().parents[3]
    folder=root/"results/affine-carry-flags-2026-10-21"
    w=json.loads((folder/"m6-f2-witness.json").read_text())
    path=folder/"m6-finite-lift-1025.json"
    report=verify_lift(w,json.loads(path.read_text()))
    report["artifact_sha256"]=hashlib.sha256(path.read_bytes()).hexdigest()
    (folder/"m6-finite-lift-replay.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report))

