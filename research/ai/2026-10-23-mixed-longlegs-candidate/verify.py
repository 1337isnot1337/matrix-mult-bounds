"""Literal exact controls for the frozen (5,100,140) candidate.

This is a necessary-condition report, not a construction certificate.
Only the Python standard library is required.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import argparse
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
RESULTS=ROOT/"results/mixed-longlegs-candidate-2026-10-23"
NAMES=("S","F2","F3","O33","O42","M2")
COUNTS={"F2":7,"F3":10,"O33":4,"O42":2,"M2":6}
EXPECTED_B_INTRINSIC={"S":117,"F2":5,"F3":12,"O33":8,"O42":8,"M2":12}
EXPECTED_C_INTRINSIC={"S":140,"F2":12,"F3":21,"O33":8,"O42":5,"M2":5}


def block(name, opposite=False):
    if name in ("S","F2","F3"):
        b={"S":10,"F2":2,"F3":3}[name]
        B,C=b,b+4
        entries=[(i,j,i+j) for i in range(5) for j in range(b)]
    elif name=="M2":
        B,C=6,2
        entries=[(i,i+k,k) for i in range(5) for k in range(2)]
    elif name in ("O33","O42"):
        B,C={"O33":(3,3),"O42":(4,2)}[name]
        entries=[(j+k,j,k) for j in range(B) for k in range(C)]
    else:
        raise ValueError("unknown named block")
    if opposite:
        return C,B,[(i,k,j) for i,j,k in entries]
    return B,C,entries


def add(row,column,value):
    row[column]=row.get(column,0)+value
    if not row[column]:
        del row[column]


def intrinsic_rows(name,opposite=False):
    b,c,entries=block(name,opposite)
    wedges=list(combinations(range(b),2))
    positions={(i,w):r for r,(i,w) in
               enumerate((i,w) for i in range(5) for w in wedges)}
    rows=[{} for _ in positions]
    for i,j,k in entries:
        for ell in range(b):
            if j!=ell:
                sign=1 if j<ell else -1
                wedge=tuple(sorted((j,ell)))
                add(rows[positions[i,wedge]],k*b+ell,sign)
    return c*b,rows


def pair_rows(left,right,opposite=False):
    b,c,entries=block(left,opposite)
    d,e,other=block(right,opposite)
    rows=[{} for _ in range(5*b*d)]
    for i,j,k in entries:
        for ell in range(d):
            add(rows[(i*b+j)*d+ell],k*d+ell,1)
    for i,ell,k in other:
        for j in range(b):
            add(rows[(i*b+j)*d+ell],c*d+k*b+j,-1)
    return c*d+e*b,rows


class Forest:
    def __init__(self,n):
        self.parent=list(range(n))
    def root(self,u):
        while self.parent[u]!=u:
            self.parent[u]=self.parent[self.parent[u]]
            u=self.parent[u]
        return u
    def edge(self,u,v):
        u=self.root(u);v=self.root(v)
        if u==v:
            return False
        self.parent[u]=v
        return True


def graph_certificate(n,rows):
    """Each literal row is an incidence edge, possibly grounded at zero.

    Independent forest rows prove the lower rank bound. Each component not
    containing the grounded vertex gives one independent indicator kernel
    vector, proving the matching upper bound.
    """
    forest=Forest(n+1)
    selected=[]
    edges=[]
    for index,row in enumerate(rows):
        if not row:
            continue
        if len(row)>2 or any(value not in (-1,1) for value in row.values()):
            raise ValueError("row is not a signed incidence relation")
        nodes=list(row)
        if len(nodes)==2:
            if sum(row.values())!=0:
                raise ValueError("two-variable row lacks opposite signs")
            u,v=nodes
        else:
            u,v=nodes[0],n
        edges.append((u,v))
        if forest.edge(u,v):
            selected.append(index)
    components={}
    for node in range(n+1):
        components.setdefault(forest.root(node),[]).append(node)
    component_list=sorted(components.values(),key=lambda nodes:nodes[0])
    labels={node:i for i,nodes in enumerate(component_list) for node in nodes}
    if any(labels[u]!=labels[v] for u,v in edges):
        raise ValueError("kernel component fails a literal equation")
    free=[nodes for nodes in component_list if n not in nodes]
    rank=n-len(free)
    if rank!=len(selected):
        raise ValueError("forest lower bound and kernel upper bound differ")
    digest=hashlib.sha256(json.dumps(
        [[(j,row[j]) for j in sorted(row)] for row in rows],
        separators=(",",":")).encode()).hexdigest()
    return {"rows":len(rows),"columns":n,"rank":rank,
            "nullity":len(free),"literal_rows_sha256":digest,
            "independent_forest_rows":selected,"kernel_components":free}


def rational_rank(rows):
    """Independent sparse Gaussian elimination for the shared-leg controls."""
    pivots={}
    for input_row in rows:
        row={j:Fraction(value) for j,value in input_row.items() if value}
        while row:
            j=min(row)
            if j not in pivots:
                scale=row[j]
                pivots[j]={k:value/scale for k,value in row.items()}
                break
            scale=row[j]
            for k,value in pivots[j].items():
                difference=row.get(k,Fraction(0))-scale*value
                if difference:
                    row[k]=difference
                else:
                    row.pop(k,None)
    return len(pivots)


def shared_rows(name,p):
    """B* tensor wedge^p A -> C tensor wedge^(p+1) A."""
    b,c,entries=block(name)
    domain=list(combinations(range(5),p))
    codomain=list(combinations(range(5),p+1))
    index={w:r for r,w in enumerate(codomain)}
    rows=[{} for _ in range(c*len(codomain))]
    for i,j,k in entries:
        for wnumber,wedge in enumerate(domain):
            if i in wedge:
                continue
            sign=(-1)**sum(v<i for v in wedge)
            output=tuple(sorted((i,)+wedge))
            add(rows[k*len(codomain)+index[output]],j*len(domain)+wnumber,sign)
    return b*len(domain),rows


def slice_rank(name):
    b,c,entries=block(name)
    coefficients=(1,2,3,5,7)
    rows=[{} for _ in range(b)]
    for i,j,k in entries:
        add(rows[j],k,coefficients[i])
    rank=rational_rank(rows)
    if rank!=min(b,c):
        raise ValueError("slice does not attain the block's ordinary bound")
    return rank


def graph_ranks(opposite):
    certificates={}
    intrinsics={}
    pairs={}
    for name in NAMES:
        n,rows=intrinsic_rows(name,opposite)
        certificate=graph_certificate(n,rows)
        intrinsics[name]=certificate["rank"]
        certificates["intrinsic/"+name]=certificate
    target_names=list(COUNTS)
    selected_pairs=[("S","S")]+[(left,right)
        for i,left in enumerate(target_names) for right in target_names[i:]]
    for left,right in selected_pairs:
        n,rows=pair_rows(left,right,opposite)
        certificate=graph_certificate(n,rows)
        pair=left+"/"+right
        pairs[pair]=certificate["rank"]
        certificates["pair/"+pair]=certificate
    expected=EXPECTED_C_INTRINSIC if opposite else EXPECTED_B_INTRINSIC
    if intrinsics!=expected:
        raise ValueError("intrinsic rank changed")
    return intrinsics,pairs,certificates


def aggregate(counts,intrinsics,pairs):
    names=list(counts)
    total=sum(counts[name]*intrinsics[name] for name in names)
    for i,left in enumerate(names):
        total+=comb(counts[left],2)*pairs[left+"/"+left]
        for right in names[i+1:]:
            total+=counts[left]*counts[right]*pairs[left+"/"+right]
    return total


def score_certificate():
    lower=Fraction(29,17)
    deficit=5-lower**3
    target_lower=304+161*lower
    gap=target_lower**3-240**3*14
    if deficit<=0 or gap<=0:
        raise ValueError("radical score comparison failed")
    return {"source":"120*cuberoot(7)",
            "target":"76*cuberoot(4)+(161/2)*cuberoot(5/2)",
            "positive_scale":"2^(4/3)",
            "scaled_source":"240*cuberoot(14)",
            "scaled_target":"304+161*cuberoot(5)",
            "cuberoot_5_lower_bound":str(lower),
            "root_bound_cube_deficit":str(deficit),
            "scaled_target_lower_bound":str(target_lower),
            "strict_cubed_gap":str(gap)}


def quantum_marginals():
    first=[Fraction(0) for _ in range(5)]
    second=[Fraction(0) for _ in range(10)]
    third=[Fraction(0) for _ in range(14)]
    for i in range(5):
        for j in range(10):
            weight=Fraction(comb(4,i)*comb(9,j),comb(13,i+j))
            first[i]+=10*weight
            second[j]+=weight
            third[i+j]+=weight
    if first!=[28]*5 or second!=[Fraction(7,5)]*10 or third!=[1]*14:
        raise ValueError("simultaneous source balancing failed")
    return {"squared_weight":"binom(4,i)*binom(9,j)/binom(13,i+j)",
            "total_mass":140,"first_each":"28",
            "second_each":"7/5","third_each":"1",
            "literal_weights":500,"marginal_coordinates":245}


def source_tail_controls():
    """Literal small controls for both exact source C-leg rank windows."""
    formats=((1,2,2),(2,1,2),(2,2,2),(3,1,2),(3,2,1),(3,2,2))
    controls=[]
    for a,b,copies in formats:
        width=a+b-1
        N=copies*width
        B=copies*b
        entries=[(i,r*b+j,r*width+i+j) for r in range(copies)
                 for i in range(a) for j in range(b)]
        for p in range(N):
            domain=list(combinations(range(N),p))
            codomain=list(combinations(range(N),p+1))
            positions={w:r for r,w in enumerate(codomain)}
            rows=[{} for _ in range(a*len(codomain))]
            for i,j,k in entries:
                for wnumber,wedge in enumerate(domain):
                    if k in wedge:
                        continue
                    sign=(-1)**sum(v<k for v in wedge)
                    output=tuple(sorted((k,)+wedge))
                    add(rows[i*len(codomain)+positions[output]],
                        j*len(domain)+wnumber,sign)
            rank=rational_rank(rows)
            ncols=B*len(domain)
            nrows=a*len(codomain)
            if p<=a-1 and rank!=ncols:
                raise ValueError("low-degree source injectivity failed")
            if p>=copies*(a-1) and rank!=nrows:
                raise ValueError("high-degree source surjectivity failed")
            if p>=a and rank>=ncols:
                raise ValueError("explicit source kernel not detected")
            if p<copies*(a-1) and rank>=nrows:
                raise ValueError("explicit source cokernel not detected")
            controls.append({"a":a,"b":b,"copies":copies,"degree":p,
                             "rows":nrows,"columns":ncols,"rank":rank})
    return {"literal_matrix_count":len(controls),"controls":controls,
            "candidate_automatic_C_degrees":[[0,4],[40,139]],
            "candidate_unresolved_C_degrees":[5,39]}


def copywise_dimension_control():
    from itertools import product
    solutions=[]
    tested=0
    for x,y,z,w,v in product(range(6),range(4),range(4),range(3),range(2)):
        tested+=1
        if 2*x+3*y+3*z+4*w+6*v==10 and 6*x+7*y+3*z+2*w+2*v==14:
            solutions.append([x,y,z,w,v])
    if tested!=576 or solutions!=[[2,0,0,0,1]]:
        raise ValueError("copy-preserving dimension calculation changed")
    return {"bounded_integer_tuples":tested,"per_copy_solutions":solutions,
            "target_counts":[7,10,4,2,6],"whole_block_copywise_allocation_possible":False,
            "arbitrary_mixing_excluded":False}


def report():
    frozen=HERE/"discovery_input.json"
    digest=hashlib.sha256(frozen.read_bytes()).hexdigest()
    if digest!="c53abefde0cb5d5e2e816f96ae6c257ee843f59e6c28d13a6ae1994de9ab88f3":
        raise ValueError("frozen candidate changed")
    candidate=json.loads(frozen.read_text())
    dims=[5,sum(count*block(name)[0] for name,count in COUNTS.items()),
          sum(count*block(name)[1] for name,count in COUNTS.items())]
    if dims!=[5,100,140]:
        raise ValueError("candidate dimension mismatch")
    degree_one={}
    certificates={}
    for leg,opposite in (("B",False),("C",True)):
        internal,pair,certs=graph_ranks(opposite)
        source=aggregate({"S":10},internal,pair)
        target=aggregate(COUNTS,internal,pair)
        expected=(12735,12587) if leg=="B" else (14000,13572)
        if (source,target)!=expected:
            raise ValueError("nonshared Koszul comparison changed")
        degree_one[leg]={"source_rank":source,"target_rank":target,
                         "source_minus_target":source-target,
                         "intrinsic":internal,"pairs":pair}
        certificates[leg]=certs
    shared={}
    for name in NAMES:
        shared[name]=[rational_rank(shared_rows(name,p)[1]) for p in range(5)]
    shared_source=[10*value for value in shared["S"]]
    shared_target=[sum(COUNTS[name]*shared[name][p] for name in COUNTS)
                   for p in range(5)]
    expected_shared=[100,440,720,520,140]
    if shared_source!=expected_shared or shared_target!=expected_shared:
        raise ValueError("shared-A Koszul equality changed")
    slice_source=10*slice_rank("S")
    slice_target=sum(count*slice_rank(name) for name,count in COUNTS.items())
    if (slice_source,slice_target)!=(100,72):
        raise ValueError("generic first-slice rank changed")
    result={"status":"exact necessary screens passed; construction unresolved",
            "candidate_sha256":digest,"format":dims,
            "degree_one_nonshared_koszul":degree_one,
            "degree_one_literal_matrix_count":44,
            "shared_A_B_star_wedge_convention":{"source":shared_source,
                "target":shared_target,"blocks":shared,"literal_matrix_count":30},
            "first_slice_coefficients":[1,2,3,5,7],
            "generic_first_slice_ranks":{"source":slice_source,"target":slice_target},
            "source_simultaneous_uniform_marginals":quantum_marginals(),
            "source_output_leg_maximal_windows":source_tail_controls(),
            "copywise_dimension_control":copywise_dimension_control(),
            "exact_score_comparison":score_certificate(),
            "all_degree_symmetric_power_scope":candidate["completed_screens"]["symmetric_power_all_degrees"],
            "higher_nonshared_Koszul_degrees":"not established by this verifier",
            "degeneration_constructed":False,"improved_exponent_established":False}
    return result,certificates


if __name__=="__main__":
    result,certificates=report()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,default=RESULTS/"verification.json")
    parser.add_argument("--certificates",type=Path,default=RESULTS/"degree_one_certificates.json")
    args=parser.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.certificates.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    args.certificates.write_text(json.dumps(certificates,indent=2)+"\n")
    print(json.dumps({"status":result["status"],"format":result["format"],
        "degree_one_literal_matrices":44,"shared_A_literal_matrices":30,
        "source_tail_literal_matrices":result["source_output_leg_maximal_windows"]["literal_matrix_count"],
        "output":str(args.output)},indent=2))

