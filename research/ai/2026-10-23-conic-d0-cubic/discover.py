"""Exact symbolic discovery on the d=0 cubic-conic fiber."""
import importlib.util
import json
from pathlib import Path
import sympy as s

root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location(
    'conic_d0_predecessor',
    root/'research/ai/2026-10-21-conic-second-jets/verify.py')
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
m=v.m


def back_substitute(rows,operations,n,right):
    answer=s.zeros(n,1)
    for i,j,_ in reversed(operations):
        answer[j]=(sum(rows[i].get(n+k,0)*value for k,value in enumerate(right))
                   -sum(z*answer[k] for k,z in rows[i].items() if k<n and k!=j))
    return answer


sub={m.C:0,m.D:0}
cancel=lambda matrix: matrix.applyfunc(s.cancel)
jet=v.read('witnesses')['cubic_component_two_jet']
bs,cs=[[m.decode(row).subs(sub) for row in jet[key]] for key in ('B','C')]
y2=m.decode(jet['source_row_correction_order2']).subs(sub)
w=m.contract(bs[0],cs[0],m.E.A0)
pivots=jet['output_pivot_columns']; inverse=w[:,pivots].inv()
f1=m.contract(bs[1],cs[0],m.E.A0)+m.contract(bs[0],cs[1],m.E.A0)
raw3=m.contract(bs[2],cs[1],m.E.OUTSIDE)-y2*f1
rawb,rawc,_=m.geometry()
fields=[]
for raw,side in ((rawb,'B'),(rawc,'C')):
    for row in range(14):
        for j in raw[:2]:
            db,dc=s.zeros(14,112),s.zeros(14,112)
            (db if side=='B' else dc)[row,j]=1
            fields.append((db,dc))
fields += [tuple(matrix.subs(sub) for matrix in pair) for pair in m.geometry()[2]]
fields += [tuple(matrix.subs(sub) for matrix in pair) for pair in v.normals().values()]
unknowns=len(fields)
columns=[raw3]
for field_index,(db,dc) in enumerate(fields):
    delta2=m.contract(db,cs[0],m.E.OUTSIDE)+m.contract(bs[0],dc,m.E.OUTSIDE)
    dy=delta2[:,pivots]*inverse
    assert not cancel(delta2-dy*w).todok()
    columns.append(m.contract(db,cs[1],m.E.OUTSIDE)+m.contract(bs[1],dc,m.E.OUTSIDE)-dy*f1)
positions={j:i for i,j in enumerate(m.E.OUTSIDE)}
projector=m.flattening()[3].subs(sub)
systems=[]; constraints=[]
for middle in (0,1,2):
    bc,cc,sources,L,Z,steps=m.sector(middle)
    L,Z=[matrix.subs(sub) for matrix in (L,Z)]
    flat=s.MutableSparseMatrix(len(sources)*196,len(columns),{})
    for k,column in enumerate(columns):
        rhs=-column[[positions[j] for j in sources],:]
        for (i,j),z in rhs.todok().items(): flat[196*i+j,k]=z
    projected=s.MutableSparseMatrix(flat.rows,flat.cols,{})
    for i in range(len(sources)):
        block=m.expand(projector*flat[196*i:196*(i+1),:])
        for (j,k),z in block.todok().items(): projected[196*i+j,k]=z
    lift=s.MutableSparseMatrix(L.cols,flat.cols,{})
    for selected,inv,indices in steps:
        values=m.expand(inv.subs(sub)*projected[selected,:])
        for (i,j),z in values.todok().items(): lift[indices[i],j]=z
    combined=m.distinct_rows(m.expand((L*Z).row_join(projected-L*lift)))
    rows,active,operations=m.unit_eliminate(combined,Z.cols)
    assert not any(any(j<Z.cols for j in rows[i]) for i in active)
    block=s.MutableSparseMatrix(len(active),len(columns),{})
    for i,original in enumerate(active):
        for j,z in rows[original].items():
            if j>Z.cols: block[i,j-Z.cols-1]=z
            elif j==Z.cols: block[i,len(columns)-1]=-z
    constraints.append(m.distinct_rows(block))
    systems.append((bc,cc,Z,lift,rows,operations))
    print('Symbolic sector',middle,'done',flush=True)
joint=m.distinct_rows(s.Matrix.vstack(*constraints))
print('Joint shape',joint.shape,flush=True)
rref,pivotcols=joint.to_DM().to_field().rref(); rref=rref.to_Matrix()
print('Joint pivots',pivotcols,flush=True)
if unknowns in pivotcols: raise ArithmeticError('complete symbolic third correction inconsistent')
weights=s.zeros(unknowns,1)
for i,j in enumerate(pivotcols): weights[j]=s.factor(rref[i,unknowns])
print('Weights',list(weights),flush=True)
bs.append(s.zeros(14,112)); cs.append(s.zeros(14,112))
for coefficient,(db,dc) in zip(weights,fields):
    bs[2]+=coefficient*db; cs[2]+=coefficient*dc
for bc,cc,Z,lift,rows,operations in systems:
    right=[1]+list(weights)
    free=back_substitute(rows,operations,Z.cols,right)
    coefficient=cancel(lift*s.Matrix(right)+Z*free)
    n=len(bc)
    for i,j in enumerate(bc):
        for row in range(14): bs[3][row,j]+=coefficient[n*row+i]
    for i,j in enumerate(cc):
        for row in range(14): cs[3][row,j]+=coefficient[14*n+n*row+i]
bs,cs=[[cancel(matrix) for matrix in maps] for maps in (bs,cs)]
fs=[sum((m.contract(bs[i],cs[k-i],range(112)) for i in range(k+1)),s.zeros(112,196))
    for k in range(4)]
ys=[s.zeros(100,12)]
for k in range(1,4):
    residual=cancel(fs[k][m.E.OUTSIDE,:]-sum((ys[i]*fs[k-i][m.E.A0,:] for i in range(1,k)),s.zeros(100,196)))
    y=cancel(residual[:,pivots]*inverse)
    assert not cancel(residual-y*w).todok()
    ys.append(y)
    print('Symbolic source order',k,'passed',flush=True)
denominators=sorted({str(s.factor(s.fraction(z)[1])) for matrix in bs+cs+ys for z in matrix.todok().values()})
report={'status':'discovery-only','base':'c=-d^3','second_field_weights':list(map(str,weights)),
        'coefficient_denominators':denominators,'B':[m.encode(matrix) for matrix in bs],
        'C':[m.encode(matrix) for matrix in cs],'source_row_corrections':[m.encode(matrix) for matrix in ys[1:]],
        'output_pivot_columns':pivots,'exponent_improvement':False}
target=root/'results/local/conic-d0-third-discovery.json'
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(report,indent=2)+'\n')
print('Denominators',denominators,flush=True)
