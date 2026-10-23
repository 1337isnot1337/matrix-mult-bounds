"""Exact discovery: third-order correction of the predecessor's fixed two-jet."""
import argparse
import importlib.util
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    'third_jet_predecessor',
    ROOT/'research/ai/2026-10-21-conic-second-jets/verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
m = v.m


def back_substitute(rows, operations, n, right):
    answer = s.zeros(n,1)
    for i,j,_ in reversed(operations):
        answer[j] = (sum(rows[i].get(n+k,0)*value for k,value in enumerate(right))
                     -sum(z*answer[k] for k,z in rows[i].items() if k<n and k!=j))
    return answer


def run(parameters, allow_second=False):
    a, b, d = map(s.Rational, parameters)
    substitution = {m.A:a, m.B:b, m.C:-d**3, m.D:d}
    jet = v.read('witnesses')['cubic_component_two_jet']
    bs, cs = [[m.decode(row).subs(substitution) for row in jet[key]]
              for key in ('B', 'C')]
    y2 = m.decode(jet['source_row_correction_order2']).subs(substitution)
    f1 = m.contract(bs[1],cs[0],m.E.A0)+m.contract(bs[0],cs[1],m.E.A0)
    raw3 = m.contract(bs[2],cs[1],m.E.OUTSIDE)-y2*f1
    columns = [raw3]
    if allow_second:
        rawb,rawc,planes = m.geometry()
        fields = []
        for side,raw in (('B',rawb),('C',rawc)):
            for row in range(14):
                for j in raw[:2]:
                    db,dc = s.zeros(14,112),s.zeros(14,112)
                    (db if side=='B' else dc)[row,j] = 1
                    fields.append((db,dc))
        fields += planes+list(v.normals().values())
        w = m.contract(bs[0],cs[0],m.E.A0)
        pivots = jet['output_pivot_columns']
        output_inverse = w[:,pivots].inv()
        for db,dc in fields:
            db,dc = [matrix.subs(substitution) for matrix in (db,dc)]
            delta2 = (m.contract(db,cs[0],m.E.OUTSIDE)
                      +m.contract(bs[0],dc,m.E.OUTSIDE))
            delta_y2 = delta2[:,pivots]*output_inverse
            if (delta2-delta_y2*w).todok():
                raise ArithmeticError('second-coefficient field is not tangent')
            columns.append(m.contract(db,cs[1],m.E.OUTSIDE)
                           +m.contract(bs[1],dc,m.E.OUTSIDE)-delta_y2*f1)
        print('second-coefficient fields',len(fields),flush=True)
    source_row = {j:i for i,j in enumerate(m.E.OUTSIDE)}
    results, constraints, systems = [], [], []
    for middle in (0, 1, 2):
        bc,cc,sources,operator,zmap,steps = m.sector(middle)
        operator,zmap = [matrix.subs(substitution) for matrix in (operator,zmap)]
        flat = s.MutableSparseMatrix(len(sources)*196,len(columns),{})
        for k,column in enumerate(columns):
            rhs = -column[[source_row[j] for j in sources],:]
            for (i,j),z in rhs.todok().items():
                flat[196*i+j,k] = z
        # The predecessor projector quotients arbitrary third source-row motion.
        projector = m.flattening()[3].subs(substitution)
        projected = s.MutableSparseMatrix(flat.rows,flat.cols,{})
        for i in range(len(sources)):
            block = projector*flat[196*i:196*(i+1),:]
            for (j,k),z in block.todok().items():
                projected[196*i+j,k] = z
        lift = s.MutableSparseMatrix(operator.cols,flat.cols,{})
        for rows,inverse,indices in steps:
            values = inverse.subs(substitution)*projected[rows,:]
            for (i,j),z in values.todok().items():
                lift[indices[i],j] = z
        remainder = projected-operator*lift
        combined = m.distinct_rows((operator*zmap).row_join(remainder))
        rows,active,operations = m.unit_eliminate(combined,zmap.cols)
        systems.append((bc,cc,zmap,lift,rows,operations))
        residuals = sorted({str(s.factor(rows[i].get(zmap.cols,0)))
                            for i in active if rows[i].get(zmap.cols,0)})
        if any(any(j<zmap.cols for j in rows[i]) for i in active):
            raise ArithmeticError('incomplete coefficient elimination')
        results.append({'middle':middle,'unknowns':operator.cols,
                        'unit_pivots':len(operations),
                        'nonzero_reduced_rhs':residuals,
                        'soluble':not residuals})
        print('sector',middle,'soluble',not residuals,flush=True)
        if allow_second:
            # Equation: residual0 + sum x_k residual_k = 0, in all sectors.
            block = s.MutableSparseMatrix(len(active),len(columns),{})
            for i,original in enumerate(active):
                for j,z in rows[original].items():
                    if j>zmap.cols: block[i,j-zmap.cols-1] = z
                    elif j==zmap.cols: block[i,len(columns)-1] = -z
            constraints.append(m.distinct_rows(block))
    report = {'status':'discovery-only',
            'parameters':dict(zip(('a','b','d'),map(str,(a,b,d)))),
            'second_coefficient':'fixed exported PR101 two-jet',
            'sectors':results,'third_lift_exists':all(r['soluble'] for r in results),
            'exponent_improvement':False}
    if allow_second:
        joint = m.distinct_rows(s.Matrix.vstack(*constraints))
        rows,active,operations = m.unit_eliminate(joint,len(columns)-1)
        residuals = sorted({str(rows[i].get(len(columns)-1,0)) for i in active
                            if rows[i].get(len(columns)-1,0)})
        report['allow_all_second_tangents'] = {
            'dimension':len(columns)-1,'equations':joint.rows,
            'rank':len(operations),'nonzero_reduced_rhs':residuals,
            'soluble':not residuals}
        print('all second tangents soluble',not residuals,flush=True)
        if not residuals:
            weights = back_substitute(rows,operations,len(columns)-1,[1])
            bs.append(s.zeros(14,112)); cs.append(s.zeros(14,112))
            for coefficient,(db,dc) in zip(weights,fields):
                bs[2] += coefficient*db.subs(substitution)
                cs[2] += coefficient*dc.subs(substitution)
            for bc,cc,zmap,lift,rows,operations in systems:
                right = [1]+list(weights)
                free = back_substitute(rows,operations,zmap.cols,right)
                coefficient = lift*s.Matrix(right)+zmap*free
                n = len(bc)
                for i,j in enumerate(bc):
                    for row in range(14): bs[3][row,j] += coefficient[n*row+i]
                for i,j in enumerate(cc):
                    for row in range(14): cs[3][row,j] += coefficient[14*n+n*row+i]
            contractions = [sum((m.contract(bs[i],cs[k-i],range(112))
                                for i in range(4) if 0<=k-i<4),s.zeros(112,196))
                            for k in range(5)]
            w = contractions[0][m.E.A0,:]
            corrections = [s.zeros(100,12)]
            for k in range(1,5):
                residual = (contractions[k][m.E.OUTSIDE,:]
                            -sum((corrections[i]*contractions[k-i][m.E.A0,:]
                                  for i in range(1,k)),s.zeros(100,196)))
                correction = residual[:,pivots]*output_inverse
                reduced = residual-correction*w
                if k<=3 and reduced.todok():
                    raise ArithmeticError('reconstructed third jet fails direct source replay')
                corrections.append(correction)
            report['reconstructed_third_jet'] = {
                'B':[m.encode(matrix) for matrix in bs],
                'C':[m.encode(matrix) for matrix in cs],
                'source_row_corrections':[m.encode(matrix) for matrix in corrections[1:4]],
                'output_pivot_columns':pivots,
                'second_tangent_weights':list(map(str,weights)),
                'uncorrected_order4_residual_entries':len(reduced.todok())}
            print('direct third-jet replay passed; order4 residual',len(reduced.todok()),flush=True)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parameters',nargs=3,default=['1','2','1'])
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--allow-second',action='store_true')
    args = parser.parse_args()
    report = run(args.parameters,args.allow_second)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
