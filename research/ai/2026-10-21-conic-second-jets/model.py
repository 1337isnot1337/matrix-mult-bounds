"""Exact source operators for the affine conic rank-twelve incidence.

No discovery script or ignored results/local file is imported by this module.
"""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
A, B, C, D = s.symbols('a b c d')
SYMBOLS = dict(zip(('a','b','c','d'), (A,B,C,D)))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


E = load('research/ai/2026-10-21-quantum-extension-spaces/extensions.py',
         'second_jet_source')


def encode(matrix):
    return {'shape':list(matrix.shape), 'entries':[
        [i,j,str(s.expand(z))] for (i,j),z in sorted(matrix.todok().items()) if z]}


def decode(record):
    return s.MutableSparseMatrix(*record['shape'], {
        (i,j):s.sympify(z,locals=SYMBOLS) for i,j,z in record['entries']})


def expand(matrix):
    return matrix.applyfunc(s.expand)


def dicts(matrix):
    rows = [{} for _ in range(matrix.rows)]
    for (i,j),z in matrix.todok().items():
        if z: rows[i][j] = z
    return rows


def row_matrix(rows):
    return s.MutableSparseMatrix(len(rows),112,{
        (i,j):z for i,row in enumerate(rows) for j,z in row.items()})


def contract(left,right,indices):
    return expand(E.contract(dicts(left),dicts(right),indices))


@lru_cache(None)
def base():
    """Rebuild product quotient kernels in the predecessor's fixed bases."""
    v = load('research/ai/2026-10-21-biform-balanced-puncture/verify.py',
             'second_jet_biform')
    g = (1+C*v.X)*(1-C*v.Y)
    u = v.coefficient_vector(g*(1+B*v.Y),v.U_MONOMIALS)
    w = v.coefficient_vector(g*(1+A*v.X),v.V_MONOMIALS)
    p = s.Matrix(5,6,lambda i,j:1 if j==i+1 else -u[i+1] if j==0 else 0)
    q = s.Matrix(5,6,lambda i,j:1 if j==i+1 else -w[i+1] if j==0 else 0)
    data = json.loads((ROOT/'results/biform-third-core-2026-10-21/structure.json').read_text())
    au,bv = [v.rational_matrix(data[k]) for k in ('U_basis_change','V_basis_change')]
    keep = list(range(8))+list(range(12,16))
    b0 = row_matrix(E.G).col_join(s.kronecker_product(p*au.T,s.eye(2))*row_matrix(E.EB[:16])[keep,:])
    c0 = row_matrix(E.G).col_join(s.kronecker_product(q*bv.T,s.eye(2))*row_matrix(E.EC[:16])[keep,:])
    return expand(b0),expand(c0)


@lru_cache(None)
def geometry():
    b0,c0 = base()
    rawb,rawc = [[next(iter(row)) for row in rows[:16]] for rows in (E.EB,E.EC)]
    lb,lc = b0[:,rawb],c0[:,rawc]
    fields = []
    for node in range(3):
        for endpoint in (0,3):
            for middle in (1,2):
                db,dc = s.zeros(16,112),s.zeros(16,112)
                for row,j in enumerate(rawb):
                    p,rem = divmod(j,28); q,z = divmod(rem,7)
                    if node==0 and p==endpoint:
                        db[row,E.index(middle,q,z)] += 1
                        dc[row,E.index(q,middle,z)] += 1
                    if node==1 and q==endpoint: dc[row,E.index(middle,p,z)] += 1
                    if node==2 and q==endpoint: db[row,E.index(p,middle,z)] += 1
                    dl = {}
                    if endpoint==0:
                        if z==6-middle: dl[6] = -2
                        if z==3-middle: dl[3] = -1
                    else:
                        if z==6-middle: dl[3] = -1
                        if z==3-middle: dl[0] = -2
                    for zz,coef in dl.items():
                        if node==1: db[row,E.index(p,q,zz)] += coef
                        if node==2: dc[row,E.index(q,p,zz)] += coef
                fields.append((expand(lb*db),expand(lc*dc)))
    return rawb,rawc,fields


@lru_cache(None)
def flattening():
    b0,c0 = base()
    w = contract(b0,c0,E.A0)
    old = E.contract(E.G,E.G,E.A0)
    pivots = [14*(j//4)+j%4 for j in old.to_DM().rref()[1]]
    inverse = w[:,pivots].inv()
    selector = s.MutableSparseMatrix(12,196,{(i,j):1 for i,j in enumerate(pivots)})
    projector = s.eye(196)-w.T*inverse.T*selector
    return w,pivots,inverse,projector


def project(matrix):
    projector = flattening()[3]
    entries = {}
    for block in range(matrix.rows//196):
        for (i,j),z in expand(projector*matrix[196*block:196*(block+1),:]).todok().items():
            entries[196*block+i,j] = z
    return s.MutableSparseMatrix(*matrix.shape,entries)


def distinct_rows(matrix):
    byrow = {}
    for (i,j),z in matrix.todok().items(): byrow.setdefault(i,{})[j] = z
    seen, rows = set(),[]
    for _,row in sorted(byrow.items()):
        key = tuple(sorted((j,str(z)) for j,z in row.items()))
        if key not in seen: seen.add(key); rows.append(row)
    return s.MutableSparseMatrix(len(rows),matrix.cols,{
        (i,j):z for i,row in enumerate(rows) for j,z in row.items()})


@lru_cache(None)
def sector(middle):
    """Complete row-gauged tangent operator and constant leading elimination.

    middle=0: pure boundary; middle=1,2: that middle short coordinate.
    """
    b0,c0 = base(); rawb,rawc,_ = geometry()
    if middle:
        bc = [E.index(middle,j,z) for j in range(4) for z in range(7)]
        cc = [E.index(j,middle,z) for j in range(4) for z in range(7)]
        sources = [j for j in E.OUTSIDE if j%7 in (3-middle,6-middle)]
    else:
        bc = [j for j in range(112) if j//28 in (0,3) and j not in rawb[2:]]
        cc = [j for j in range(112) if j//7%4 in (0,3) and j not in rawc[2:]]
        sources = [j for j in E.OUTSIDE if j%7 in (0,3,6)]
    n = len(bc); nb,nc = [{j:1} for j in bc],[{j:1} for j in cc]
    rawb0,rawc0 = E.contract(nb,dicts(c0),sources),E.contract(dicts(b0),nc,sources)
    entries = {}
    for (i,col),z in rawb0.todok().items():
        k,cr = divmod(col,14)
        for br in range(14): entries[196*i+14*br+cr,n*br+k] = z
    for (i,col),z in rawc0.todok().items():
        br,k = divmod(col,n)
        for cr in range(14): entries[196*i+14*br+cr,14*n+n*cr+k] = z
    operator = project(s.MutableSparseMatrix(len(sources)*196,28*n,entries))
    raw = E.contract(nb,E.G,sources)
    bg = s.Matrix(len(sources)*4,n,lambda r,j:raw[r//4,4*j+r%4])
    raw = E.contract(E.G,nc,sources)
    cg = s.Matrix(len(sources)*4,n,lambda r,j:raw[r//4,n*(r%4)+j])
    bp,cp = [list(t.to_DM().rref()[1]) for t in (bg,cg)]
    rb = list(bg[:,bp].T.to_DM().rref()[1]); rc = list(cg[:,cp].T.to_DM().rref()[1])
    ib,ic = bg[rb,bp].inv(),cg[rc,cp].inv()
    eliminated = {n*r+j for r in range(4,14) for j in bp}|{14*n+n*r+j for r in range(4,14) for j in cp}
    free = [j for j in range(28*n) if j not in eliminated]
    zmap = s.MutableSparseMatrix(28*n,len(free),{(j,k):1 for k,j in enumerate(free)})
    steps = []
    for side in ('B','C'):
        for row in range(4,14):
            if side=='B':
                rows = [(r//4)*196+row*14+r%4 for r in rb]
                inverse,indices = ib,[n*row+j for j in bp]
            else:
                rows = [(r//4)*196+(r%4)*14+row for r in rc]
                inverse,indices = ic,[14*n+n*row+j for j in cp]
            # These selected equations have one constant invertible eliminated block.
            assert operator[rows,indices]==inverse.inv()
            vals = expand(-inverse*operator[rows,free])
            for (i,k),z in vals.todok().items(): zmap[indices[i],k] = z
            steps.append((rows,inverse,indices))
    return bc,cc,sources,operator,zmap,steps


def unit_eliminate(matrix,coefficient_columns,laurent=False):
    """Only rational units, or rational*d**integer units on d!=0."""
    rows = {i:{} for i in range(matrix.rows)}
    for (i,j),z in matrix.todok().items(): rows[i][j] = z
    active,operations = set(rows),[]
    def unit(z):
        if not laurent: return bool(z.is_Rational and z)
        coeff,power = z.as_coeff_exponent(D)
        return bool(coeff.is_Rational and coeff and power.is_Integer)
    while True:
        candidates = [(sum(k<coefficient_columns for k in rows[i]),i,j)
                      for i in active for j,z in rows[i].items()
                      if j<coefficient_columns and unit(z)]
        if not candidates: break
        _,i,j = min(candidates); scale = rows[i][j]
        pivot = {k:s.expand(z/scale) for k,z in rows[i].items()}
        rows[i] = pivot; active.remove(i)
        for other in sorted(active):
            factor = rows[other].get(j,0)
            if factor:
                for k,z in pivot.items():
                    value = s.expand(rows[other].get(k,0)-factor*z)
                    if value: rows[other][k] = value
                    else: rows[other].pop(k,None)
        operations.append([i,j,str(scale)])
    return rows,sorted(active),operations


def kernel_from_units(rows,active,operations,n):
    assert all(not rows[i] for i in active)
    free = [j for j in range(n) if j not in {j for _,j,_ in operations}]
    result = s.MutableSparseMatrix(n,len(free),{(j,k):1 for k,j in enumerate(free)})
    for i,j,_ in reversed(operations):
        values = s.zeros(1,len(free))
        for k,z in rows[i].items():
            if k!=j: values -= z*result[k,:]
        result[j,:] = expand(values)
    return result,free
