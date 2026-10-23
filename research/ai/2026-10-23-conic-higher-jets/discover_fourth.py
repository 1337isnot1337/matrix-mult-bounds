"""Exact fourth-order discovery from the pinned PR107 mixed three-jet."""
import argparse
import importlib.util
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('fourth_source_model',ROOT/'research/ai/2026-10-21-conic-second-jets/model.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def back_substitute(rows,operations,n,right):
    answer=s.zeros(n,1)
    for i,j,_ in reversed(operations):
        answer[j]=sum(rows[i].get(n+k,0)*value for k,value in enumerate(right))-sum(z*answer[k] for k,z in rows[i].items() if k<n and k!=j)
    return answer

def run(parameters,allow_third,symbolic=False):
    a,b,d=(m.A,m.B,m.D) if symbolic else map(s.Rational,parameters)
    substitution={m.A:a,m.B:b,m.C:-d**3,m.D:d}
    jet=json.loads((ROOT/'results/conic-third-jets-2026-10-23/mixed-family.json').read_text())
    bs,cs=[[m.decode(record).subs(substitution) for record in jet[key]] for key in ('B','C')]
    ys=[s.zeros(100,12)]+[m.decode(row).subs(substitution) for row in jet['source_row_corrections']]
    # The generic base has already been specialized in the explicit witness.
    m.base=lambda:(bs[0],cs[0])
    fs=[sum((m.contract(bs[i],cs[k-i],range(112)) for i in range(4) if 0<=k-i<4),s.zeros(112,196)) for k in range(5)]
    w=fs[0][m.E.A0,:];pivots=jet['output_pivot_columns'];inverse=w[:,pivots].inv()
    raw=fs[4][m.E.OUTSIDE,:]-sum((ys[i]*fs[4-i][m.E.A0,:] for i in range(1,4)),s.zeros(100,196))
    columns=[raw]
    fields=[]
    if allow_third:
        rawb,rawc,planes=m.geometry()
        for side,indices in (('B',rawb),('C',rawc)):
            for row in range(14):
                for j in indices[:2]:
                    db,dc=s.zeros(14,112),s.zeros(14,112)
                    (db if side=='B' else dc)[row,j]=1
                    fields.append((db,dc))
        fields+=planes
        for middle in (1,2):
            db=s.MutableSparseMatrix(14,112,{(i,j):z/(d if middle==1 else 1) for (i,j),z in bs[1].todok().items() if j//28==middle})
            dc=s.MutableSparseMatrix(14,112,{(i,j):z/(d if middle==1 else 1) for (i,j),z in cs[1].todok().items() if j//7%4==middle})
            fields.append((db,dc))
        for db,dc in fields:
            df=m.contract(db,cs[0],range(112))+m.contract(bs[0],dc,range(112))
            dy=df[m.E.OUTSIDE,:][:,pivots]*inverse
            if (df[m.E.OUTSIDE,:]-dy*w).todok():raise ArithmeticError('non-tangent correction')
            columns.append(m.contract(db,cs[1],m.E.OUTSIDE)+m.contract(bs[1],dc,m.E.OUTSIDE)-dy*fs[1][m.E.A0,:]-ys[1]*df[m.E.A0,:])
    print('third fields',len(fields),flush=True)
    positions={j:i for i,j in enumerate(m.E.OUTSIDE)}
    projector=m.flattening()[3]
    constraints=[];systems=[];sector_reports=[]
    for middle in (0,1,2):
        bc,cc,sources,L,Z,steps=m.sector(middle)
        flat=s.MutableSparseMatrix(len(sources)*196,len(columns),{})
        for k,column in enumerate(columns):
            rhs=-column[[positions[j] for j in sources],:]
            for (i,j),z in rhs.todok().items():flat[196*i+j,k]=z
        projected=s.MutableSparseMatrix(flat.rows,flat.cols,{})
        for i in range(len(sources)):
            block=projector*flat[196*i:196*(i+1),:]
            for (j,k),z in block.todok().items():projected[196*i+j,k]=z
        lift=s.MutableSparseMatrix(L.cols,flat.cols,{})
        for selected,inv,indices in steps:
            vals=inv*projected[selected,:]
            for (i,j),z in vals.todok().items():lift[indices[i],j]=z
        combined=m.distinct_rows((L*Z).row_join(projected-L*lift))
        rows,active,operations=m.unit_eliminate(combined,Z.cols)
        if any(any(j<Z.cols for j in rows[i]) for i in active):raise ArithmeticError('incomplete sector elimination')
        block=s.MutableSparseMatrix(len(active),len(columns),{})
        for i,original in enumerate(active):
            for j,z in rows[original].items():
                if j>Z.cols:block[i,j-Z.cols-1]=z
                elif j==Z.cols:block[i,len(columns)-1]=-z
        reduced=m.distinct_rows(block)
        constraints.append(reduced);systems.append((bc,cc,Z,lift,rows,operations))
        fixed_residual=sorted({str(row[-1]) for row in reduced.tolist() if row[-1]})
        sector_reports.append({'middle':middle,'fixed_nonzero_rhs_values':fixed_residual,'equations':reduced.rows})
        print('sector',middle,'equations',reduced.rows,'fixed residuals',len(fixed_residual),flush=True)
    joint=m.distinct_rows(s.Matrix.vstack(*constraints))
    rref,pivotcols=joint.to_DM().to_field().rref();rref=rref.to_Matrix()
    solved=len(fields) not in pivotcols
    print('joint',joint.shape,'rank',len(pivotcols),'solved',solved,flush=True)
    report={'status':'discovery-only','parameters':dict(zip(('a','b','d'),map(str,(a,b,d)))),'allow_third_tangents':allow_third,'third_fields':len(fields),'joint_shape':list(joint.shape),'joint_rank':len(pivotcols),'fourth_order_soluble':solved,'sectors':sector_reports,'matrix_target_constructed':False,'exponent_improvement':False}
    if not solved:return report
    weights=s.zeros(len(fields),1)
    for i,j in enumerate(pivotcols):weights[j]=rref[i,len(fields)]
    bs.append(s.zeros(14,112));cs.append(s.zeros(14,112))
    for z,(db,dc) in zip(weights,fields):bs[3]+=z*db;cs[3]+=z*dc
    for bc,cc,Z,lift,rows,operations in systems:
        right=[1]+list(weights)
        free=back_substitute(rows,operations,Z.cols,right)
        coefficient=lift*s.Matrix(right)+Z*free
        n=len(bc)
        for i,j in enumerate(bc):
            for row in range(14):bs[4][row,j]+=coefficient[n*row+i]
        for i,j in enumerate(cc):
            for row in range(14):cs[4][row,j]+=coefficient[14*n+n*row+i]
    bs,cs=[[matrix.applyfunc(s.cancel) for matrix in maps] for maps in (bs,cs)]
    fs=[sum((m.contract(bs[i],cs[k-i],range(112)) for i in range(5) if 0<=k-i<5),s.zeros(112,196)) for k in range(6)]
    ys=[s.zeros(100,12)];residual_counts=[]
    for k in range(1,6):
        residual=fs[k][m.E.OUTSIDE,:]-sum((ys[i]*fs[k-i][m.E.A0,:] for i in range(1,k)),s.zeros(100,196))
        y=(residual[:,pivots]*inverse).applyfunc(s.cancel)
        reduced=(residual-y*w).applyfunc(s.cancel)
        residual_counts.append(len(reduced.todok()))
        if k<=4 and reduced.todok():raise ArithmeticError('reconstructed fourth jet fails literal source replay')
        ys.append(y)
    report['witness']={'B':[m.encode(x) for x in bs],'C':[m.encode(x) for x in cs],'source_row_corrections':[m.encode(x) for x in ys[1:5]],'output_pivot_columns':pivots,'third_tangent_weights':list(map(str,weights)),'residual_entries_by_order':residual_counts}
    print('direct source replay',residual_counts,flush=True)
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parameters',nargs=3,default=['1','2','1'])
    parser.add_argument('--allow-third',action='store_true')
    parser.add_argument('--symbolic',action='store_true')
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args();report=run(args.parameters,args.allow_third,args.symbolic)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2)+'\n')
