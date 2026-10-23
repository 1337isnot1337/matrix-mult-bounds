"""Optional finite-field discovery of a private boundary spin channel.

The first experiment constructs a twelve-channel (m,n)=(3,8) core,
shifts its r coordinates, and adds an explicit endpoint pair at r=0.
A later quotient computation tests a changed first map. Discovery only.
"""
import json
from pathlib import Path
import numpy as np
from undoubled_spin_discovery import matrices
from spin_module_discovery import toolkit

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"results/anisotropic-constructions-2026-10-20"
kit=toolkit()
prime=kit["prime"]
rank,rref,kernel=kit["rank"],kit["rref"],kit["kernel"]

def transfer(U,m,n=8):
    _,K,L=matrices(m,n)
    Q=kernel(U.T).T
    q0,q1=Q@K[0]%prime,Q@K[1]%prime
    zero=np.zeros_like(q0)
    D=kernel(np.block([[q1,zero],[zero,q0],[q0,-q1]])%prime)
    V=K[0]@D[:m*(n+1)]%prime
    Wfull=np.concatenate([a@U%prime for a in L],axis=1)
    piv=rref(Wfull)[1]
    W=Wfull[:,piv]
    LP=[L[1],(L[0]-L[3])*pow(2,-1,prime)%prime,L[2]]
    B=np.concatenate([W]+[a@V%prime for a in LP],axis=1)%prime
    return {"U":U,"D":D,"V":V,"W":W,"W_pivots":piv,"LP":LP,"B":B,"rank":rank(B)}

def discover(trials=50):
    records=[]
    for profile in [(3,3,2,2),(3,3,3,1)]:
        for trial in range(trials):
            seed=930000+1000*profile[-1]+trial
            rng=np.random.default_rng(seed)
            cols=[];gens=[]
            for length in profile:
                g=np.zeros((4-length,8),dtype=np.int64)
                positions=rng.choice(g.size,min(5,g.size),replace=False)
                g.ravel()[positions]=rng.choice([-1,1],size=len(positions))
                gens.append(g.tolist())
                for shift in range(length):
                    v=np.zeros((3,8),dtype=np.int64)
                    v[shift:shift+4-length]=g
                    cols.append(v.ravel())
            U=np.array(cols,dtype=np.int64).T
            if rank(U)!=10:continue
            t=transfer(U,3)
            rec={"profile":list(profile),"trial":trial,"seed":seed,"U_dimension":10,"W_dimension":t["W"].shape[1],"D_dimension":t["D"].shape[1],"full_join_rank":t["rank"]}
            records.append(rec)
            if t["D"].shape[1]!=12 or t["W"].shape[1]!=28 or t["rank"]!=64:continue
            shifted=np.zeros((32,11),dtype=np.int64)
            shifted[8:,:10]=U
            shifted[0,10]=1;shifted[7,10]=-1
            new=transfer(shifted,4)
            # Use the old twelve pairs and the explicit boundary pair as a
            # prescribed basis rather than an arbitrary RREF basis.
            pairs=np.zeros((72,13),dtype=np.int64)
            pairs[9:36,:12]=t["D"][:27]
            pairs[45:72,:12]=t["D"][27:]
            pairs[0,12]=1;pairs[36+8,12]=1
            _,K,L=matrices(4,8)
            V=K[0]@pairs[:36]%prime
            B=np.concatenate([new["W"]]+[a@V%prime for a in new["LP"]],axis=1)%prime
            rec.update(private_U_dimension=11,private_W_dimension=new["W"].shape[1],private_D_dimension=new["D"].shape[1],private_join_rank=rank(B),private_join_columns=B.shape[1])
            candidate={"scope":"finite-field boundary-channel discovery only","prime":prime,"base_source":[2,3,8],"target_base":[3,3,12],"record":rec,"generators":gens,"base_U":U.tolist(),"base_pairs":t["D"].tolist(),"private_U":shifted.tolist(),"private_pairs":pairs.tolist(),"new_exponent_established":False}
            (OUT/"spin-private-boundary-candidate.json").write_text(json.dumps(candidate,indent=2)+"\n")
            (OUT/"spin-private-boundary-discovery.json").write_text(json.dumps({"records":records,"base_candidate_found":True,"scope":"finite-field discovery, no rational maps or square construction"},indent=2)+"\n")
            print(json.dumps(rec),flush=True)
            return candidate
    (OUT/"spin-private-boundary-discovery.json").write_text(json.dumps({"records":records,"base_candidate_found":False,"scope":"finite-field discovery only"},indent=2)+"\n")
    print(json.dumps({"trials":len(records),"base_candidate_found":False,"best_join":max((r["full_join_rank"] for r in records),default=0)}),flush=True)
    return None


def changed_first_quotient():
    path=OUT/"spin-private-boundary-candidate.json"
    data=json.loads(path.read_text())
    pairs=np.array(data["private_pairs"],dtype=np.int64)%prime
    r=13
    z=np.zeros((3*r,72),dtype=np.int64)
    half=pow(2,-1,prime)
    z[:r,36:]=pairs[:36].T
    z[r:2*r,:36]=pairs[:36].T*half%prime
    z[r:2*r,36:]=-pairs[36:].T*half%prime
    z[2*r:,:36]=pairs[36:].T
    witness=json.loads((OUT/"spin-module14-witness.json").read_text())
    x=np.zeros((9,12),dtype=np.int64)
    for i,j,v in witness["X"]["entries"]:x[i,j]=v
    x=x*pow(int(witness["X"]["denominator"]),-1,prime)%prime
    M=np.zeros((9,3*r,80),dtype=np.int64)
    for i in range(2):
      for p in range(2):
       for q in range(2):
        for a in range(4):
         for j in range(8):
          for s in range(2):
           M[:,:,(p*5+a+s)*8+j]+=np.outer(x[:,(i*3+p+q)*2+s],z[:,(q*4+a)*9+i+j])
           M[:,:,(p*5+a+s)*8+j]%=prime
    M=M.reshape(27*r,80)%prime
    T=np.zeros((9,3*r,3*r),dtype=np.int64)
    for i in range(3):
      for j in range(3):
       for a in range(r):T[3*i+j,i*r+a,j*r+a]=1
    T=T.reshape(27*r,3*r)
    Q=kernel(M.T).T
    R=Q@T%prime
    rM,rR=rank(M),rank(R)
    report={"scope":"finite-field quotient screen for the prescribed private-channel first-map repair","prime":prime,"low_Y_columns":80,"coefficient_rows":27*r,"low_Y_coefficient_matrix_rank":rM,"target_quotient_dimension":rR,"extra_first_response_budget":3,"first_map_repair_parameters":"F(0,3,0),F(1,3,0),F(2,3,0) in reduced coordinates; added Y supported at p2,L0,j0,6,7","new_exponent_established":False}
    # Each new column is an affine linear function of nine coefficients
    # of its added first source coordinate. Solve membership in M+target.
    P=kernel(R.T).T@Q%prime
    linear=[];constant=[]
    for vertex,factor in [(0,1),(1,-half),(1,-half)]:
        A=np.zeros((27*r,9),dtype=np.int64)
        for j in range(9):A[j*(3*r)+vertex*r+12,j]=factor%prime
        linear.append(A)
        constant.append(np.zeros(27*r,dtype=np.int64))
    constant[0][2*(3*r)+r+12]=half
    constant[1][1*(3*r)+2*r+12]=half
    constant[1][5*(3*r)+2*r+12]=-2
    affine=[]
    for A,c in zip(linear,constant):
        C=P@A%prime;d=-P@c%prime
        aug,piv=rref(np.column_stack([C,d]))
        if 9 in piv:
            affine.append(None);continue
        particular=np.zeros(9,dtype=np.int64)
        particular[piv]=aug[:,-1]
        directions=kernel(C)
        assert np.all((C@particular-d)%prime==0)
        affine.append((particular,directions))
    report["column_membership_feasible"]=[a is not None for a in affine]
    report["column_parameter_dimensions"]=[None if a is None else a[1].shape[1] for a in affine]
    if all(a is not None for a in affine):
        rng=np.random.default_rng(944001)
        best=0;best_params=None
        for trial in range(100):
            parameters=[a+b@rng.integers(0,prime,size=b.shape[1])%prime for a,b in affine]
            columns=np.column_stack([(A@v+c)%prime for A,c,v in zip(linear,constant,parameters)])
            size=rank(Q@columns%prime)
            if size>best:best,best_params=size,parameters
            if size==rR:
                report["candidate_first_coefficients"]=[v.tolist() for v in parameters]
                report["target_in_extended_response"]=rank(np.concatenate([M,columns,T],axis=1))==rank(np.concatenate([M,columns],axis=1))
                break
        report["best_added_quotient_rank"]=best
    (OUT/"spin-private-boundary-quotient.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report),flush=True)
    return report




if __name__ == "__main__":
    discover()
    changed_first_quotient()
