"""Complete symbolic leading-block second-order obstruction calculation."""
from collections import defaultdict
import sympy as sp

def calculate(m,d):
    parameters=sp.symbols('t0:172')
    A=sp.MutableSparseMatrix(*d['shape'],{(i,j):sp.Rational(n,q) for i,j,n,q in d['entries']})
    linear=A*sp.Matrix(parameters);P=defaultdict(list);Q=defaultdict(list);G=defaultdict(list)
    for b in range(4):
     for old in range(112):
      if linear[b*112+old]:P[old].append((b,linear[b*112+old]))
      if linear[448+b*112+old]:Q[old].append((b,linear[448+b*112+old]))
     for old,value in m.G[b].items():G[old].append((b,value))
    first=defaultdict(lambda:sp.S.Zero);second=defaultdict(lambda:sp.S.Zero);Kpos={a:i for i,a in enumerate(m.OUTSIDE)}
    for a,b,c in m.TERMS:
     for i,x in P[b]:
      for j,y in G[c]:first[a,4*i+j]+=x*y
     for i,x in G[b]:
      for j,y in Q[c]:first[a,4*i+j]+=x*y
     if a in Kpos:
      for i,x in P[b]:
       for j,y in Q[c]:second[Kpos[a],4*i+j]+=x*y
    S1=sp.MutableSparseMatrix(112,16,dict(first));S2=sp.MutableSparseMatrix(100,16,dict(second))
    F,cb,cc,H,top,ann=m.matrices();F0=F.extract(m.A0,list(range(16)));_,pc=F0.to_DM().rref();pc=list(pc)
    Y=S1.extract(m.OUTSIDE,pc)*F0[:,pc].inv()
    assert S1.extract(m.OUTSIDE,list(range(16)))==Y*F0
    corrected=S2-Y*S1.extract(m.A0,list(range(16)))
    projected=corrected*ann.T
    vector=sp.Matrix(400,1,lambda i,j:projected[i//4,i%4])
    cokernel=top.T.to_DM().nullspace().to_Matrix();assert cokernel.shape==(36,400)
    obstructions=[sp.expand(x) for x in cokernel*vector]

    records=[];monomials=set();active=set()
    for i,expression in enumerate(obstructions):
     terms=[]
     for exponents,value in sp.Poly(expression,*parameters,domain=sp.QQ).terms():
      if not value:continue
      if sum(exponents)!=2:raise ArithmeticError('nonquadratic term')
      indices=[j for j,e in enumerate(exponents) for _ in range(e)];indices=tuple(indices)
      monomials.add(indices);active.update(indices);terms.append([*indices,int(value.p),int(value.q)])
     records.append({'cokernel_row':i,'terms':terms})
    columns=sorted(monomials);positions={ij:i for i,ij in enumerate(columns)}
    coefficient=sp.MutableSparseMatrix(36,len(columns),{})
    for i,row in enumerate(records):
     for a,b,n,q in row['terms']:coefficient[i,positions[a,b]]=sp.Rational(n,q)
    rank=m.rational_rank(coefficient)
    liftable=[]
    for j in range(172):
     if all(not any(a==j and b==j and n for a,b,n,q in row['terms']) for row in records):liftable.append(j)
    report=dict(parameters=172,quadratic_equations=36,nonzero_equations=sum(bool(r['terms']) for r in records),independent_quadratic_polynomials=rank,distinct_monomials=len(columns),active_parameters=sorted(active),coordinate_directions_satisfying_all_quadrics=liftable,departure_coordinate_directions_satisfying_all_quadrics=[j for j in d['departure_columns'] if j in liftable],records=records,scope='Exact complete leading-block second-order obstructions on the fixed DB/DC first-span prolongation family. A zero is only a compatible second jet, not a full formal degeneration or exponent bound.')
    return report
