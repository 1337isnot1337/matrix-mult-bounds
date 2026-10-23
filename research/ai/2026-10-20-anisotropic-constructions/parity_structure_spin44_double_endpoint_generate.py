"""Exact rational reconstruction of the two-endpoint graph repair."""

from fractions import Fraction
import hashlib
import json
from math import lcm

from parity_structure_spin44_double_endpoint import (
    BASE,CLAIM,DELETED,S,T,WITNESS,MAPS,MINOR,base_and_fibers,reconstruct,full_response,determinant_mod,PRIME,
)


# Each row is supported in one of the two nine-coordinate endpoint blocks.
L=[
 [0,10,4,0,4,-2,-8,1,-1,0,0,0,0,0,0,0,0,0],
 [0,8,0,0,4,0,10,-1,2,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,8,-4,0,-4,-2,0,8,-8,4],
 [0,0,0,0,0,0,0,0,0,-8,-2,0,4,-1,0,12,8,-2],
 [0,0,0,0,0,0,0,0,0,-8,2,0,4,1,0,56,6,4],
]


def transpose(a):return [list(row) for row in zip(*a)]


def multiply(a,b):
    bt=transpose(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]


def rref(a):
    a=[[Fraction(v) for v in row] for row in a]
    r,pivots=0,[]
    for c in range(len(a[0])):
        selected=next((i for i in range(r,len(a)) if a[i][c]),None)
        if selected is None:continue
        a[r],a[selected]=a[selected],a[r]
        pivot=a[r][c];a[r]=[v/pivot for v in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                f=a[i][c];a[i]=[v-f*w for v,w in zip(a[i],a[r])]
        pivots.append(c);r+=1
        if r==len(a):break
    return a,pivots


def inverse(a):
    n=len(a)
    reduced,pivots=rref([row+[int(i==j) for j in range(n)] for i,row in enumerate(a)])
    if pivots[:n]!=list(range(n)):raise ArithmeticError("Singular rational inverse")
    return [row[n:] for row in reduced]


def pack(a):
    denominator=lcm(*(Fraction(v).denominator for row in a for v in row))
    return {"shape":[len(a),len(a[0])],"denominator":denominator,
            "entries":[[i,j,int(v*denominator)] for i,row in enumerate(a) for j,v in enumerate(row) if v]}


def make_minor(response):
    basis,rows,columns={},[],[]
    for source in sorted(response):
        row={c:v%PRIME for c,v in response[source].items() if v%PRIME}
        while row:
            pivot=min(row)
            if pivot not in basis:
                inv=pow(row[pivot],-1,PRIME)
                basis[pivot]={c:v*inv%PRIME for c,v in row.items()}
                rows.append(source);columns.append(pivot);break
            f=row[pivot]
            for c,v in basis[pivot].items():
                value=(row.get(c,0)-f*v)%PRIME
                if value:row[c]=value
                else:row.pop(c,None)
    det=determinant_mod([[response[r].get(c,0) for c in columns] for r in rows],PRIME)
    return {"prime":PRIME,"source_columns":rows,"output_columns":columns,"determinant_mod_prime":det}


def main():
    _,data=base_and_fibers()
    (yr,gy,_),(zr,gz,_)=data
    cy=[(15*p+7+r)*8+j for p in range(2) for r in range(3) for j in range(3)]
    cz=[(15*r+7+j)*8+q for q in range(2) for r in range(3) for j in range(3)]
    f=[[row.get(c,0) for c in cy] for row in gy]
    g=[[row.get(c,0) for c in cz] for row in gz]
    ry=[[row.get(c,0) for c in cy] for row in yr]
    rz=[[row.get(c,0) for c in cz] for row in zr]
    complete=g+L
    _,pc=rref(complete)
    if len(pc)!=11:raise ArithmeticError("The boundary complement is not independent")
    inv=inverse([[row[c] for c in pc] for row in complete])
    coordinates=multiply([[row[c] for c in pc] for row in rz],inv)
    if multiply(coordinates,complete)!=rz:raise ArithmeticError("The boundary section misses a retained Z direction")
    b=[[-v for v in row[:6]] for row in coordinates]
    pairing=multiply(f,transpose(L))
    _,pr=rref(transpose(pairing))
    if len(pr)!=5:raise ArithmeticError("The endpoint pairing is not surjective")
    correction=multiply(multiply(ry,transpose(L)),inverse([pairing[r] for r in pr]))
    a=[[Fraction(0) for _ in range(9)] for _ in range(81)]
    for row,values in enumerate(correction):
        for c,value in zip(pr,values):a[row][c]=-value
    witness={"claim_id":CLAIM,"deleted_channels":DELETED,"S":S,"T":T,
             "base_maps_sha256":hashlib.sha256(BASE.read_bytes()).hexdigest(),
             "endpoint_boundary_columns_Y":cy,"endpoint_boundary_columns_Z":cz,
             "split_boundary_section":L,"boundary_complement_columns":pc,
             "pairing_rows":pr,"A":pack(a),"B":pack(b),
             "new_exponent_established":False,
             "recovery_status":"fresh rational graph coefficients; old byte sequence was lost"}
    maps=reconstruct(witness)
    WITNESS.write_text(json.dumps(witness,separators=(",",":"))+"\n")
    MAPS.write_text(json.dumps(maps,separators=(",",":"))+"\n")
    response,_,_=full_response(maps["maps"]["Y"]["entries"],maps["maps"]["Z"]["entries"])
    minor=make_minor(response)
    MINOR.write_text(json.dumps(minor,separators=(",",":"))+"\n")
    print(json.dumps({"map_denominators":[maps["maps"][n]["denominator"] for n in "XYZ"],
                      "sparse_map_entries":[len(maps["maps"][n]["entries"]) for n in "XYZ"],
                      "response_support":len(response),"response_minor_size":len(minor["source_columns"]),
                      "response_minor_determinant":minor["determinant_mod_prime"]}),flush=True)


if __name__=="__main__":main()
