"""Rebuild universal tangent and curvature certificates from the 4096-term source."""
import argparse
from functools import lru_cache
import gzip
import importlib.util
import json
from pathlib import Path
import sympy as s

PACKAGE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('conic_second_jet_model',PACKAGE/'model.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
ROOT = m.ROOT
RESULTS = ROOT/'results/conic-second-jets-2026-10-21'
a,b,c,d = m.A,m.B,m.C,m.D


def read(name):
    return json.loads(gzip.decompress((RESULTS/(name+'.json.gz')).read_bytes()))


def write(name,record):
    data = (json.dumps(record,sort_keys=True,separators=(',',':'))+'\n').encode()
    (RESULTS/(name+'.json.gz')).write_bytes(gzip.compress(data,mtime=0))


@lru_cache(None)
def normals():
    r = read('witnesses')
    nb2,nc2 = m.decode(r['normal_B']),m.decode(r['normal_C'])
    nb1,nc1 = s.zeros(14,112),s.zeros(14,112)
    for (i,j),z in nb2.todok().items():
        assert j//28==2
        nb1[i,j-28] = z
    for (i,j),z in nc2.todok().items():
        assert j//7%4==2
        nc1[i,j-7] = z
    return {1:(nb1,nc1),2:(nb2,nc2)}


def tangent(middle):
    bc,cc,sources,L,Z,_ = m.sector(middle)
    reduced = m.distinct_rows(m.expand(L*Z))
    rows,active,ops = m.unit_eliminate(reduced,Z.cols)
    h,free = m.kernel_from_units(rows,active,ops,Z.cols)
    kernel = m.expand(Z*h)
    assert not m.expand(L*kernel).todok()
    b0,c0 = m.base(); rawb,rawc,planes = m.geometry()
    if middle:
        fields = [planes[middle-1],planes[middle+1],normals()[middle]]
    else:
        fields = []
        for side,raw in (('B',rawb),('C',rawc)):
            for i in range(14):
                for j in raw[:2]:
                    bp,cp = s.zeros(14,112),s.zeros(14,112)
                    (bp if side=='B' else cp)[i,j] = 1
                    fields.append((bp,cp))
        fields.extend(planes[4:])
    known = s.Matrix.hstack(*[s.Matrix(list(bp[:,bc])+list(cp[:,cc])) for bp,cp in fields])
    # The unit coordinates of a polynomial kernel recover coefficients globally.
    unitrows = {}
    byrow = {}
    for (i,j),z in kernel.todok().items(): byrow.setdefault(i,{})[j] = z
    for i,row in sorted(byrow.items()):
        if len(row)==1:
            j,z = next(iter(row.items()))
            if z==1: unitrows.setdefault(j,i)
    assert len(unitrows)==kernel.cols
    indices = [unitrows[j] for j in range(kernel.cols)]
    transform = known[indices,:]
    assert not m.expand(kernel*transform-known).todok()
    determinant = s.factor(transform.det(method='domain-ge'))
    assert determinant in (s.Integer(-4),s.Integer(-1),s.Integer(1),s.Integer(4))
    return {'middle':middle,'source_indices':sources,'B_coordinates':bc,'C_coordinates':cc,
            'unknowns':L.cols,'constant_leading_eliminations':L.cols-Z.cols,
            'unit_operations':ops,'unit_pivot_count':len(ops),
            'reduced_matrix':m.encode(reduced),'kernel':m.encode(kernel),
            'free_coordinates':free,'basis_transform':m.encode(transform),
            'basis_transform_determinant':str(determinant)}


def curvature(first_middle):
    """Quotient all relevant second row coefficients, retaining every base velocity."""
    bc,cc,sources,L,Z,steps = m.sector(3-first_middle)
    b0,c0 = m.base(); rawb,rawc,planes = m.geometry()
    fields = []
    for side,raw in (('B',rawb),('C',rawc)):
        for row in range(14):
            for j in raw[:2]:
                bp,cp = s.zeros(14,112),s.zeros(14,112)
                (bp if side=='B' else cp)[row,j] = 1
                fields.append((bp,cp))
    fields.extend(planes)
    hs = []
    for normal in (1,2):
        nb,nc = normals()[normal]
        mat = s.MutableSparseMatrix(196*len(sources),68,{})
        for k,(bp,cp) in enumerate(fields):
            raw = m.contract(bp,nc,sources)+m.contract(nb,cp,sources)
            for (i,j),z in raw.todok().items(): mat[196*i+j,k] = z
        hs.append(m.project(mat))
    nb,nc = normals()[first_middle]
    raw = m.contract(nb,nc,sources)
    q = m.project(s.MutableSparseMatrix(196*len(sources),1,{
        (196*i+j,0):z for (i,j),z in raw.todok().items()}))
    extra = hs[0].row_join(hs[1]).row_join(q)
    lift = s.MutableSparseMatrix(L.cols,137,{})
    for rows,inverse,indices in steps:
        vals = m.expand(-inverse*extra[rows,:])
        for (i,k),z in vals.todok().items(): lift[indices[i],k] = z
    remainder = m.expand(extra+L*lift)
    combined = m.distinct_rows(m.expand(L*Z).row_join(remainder[:,:136]).row_join(-remainder[:,136:137]))
    rows,active,ops = m.unit_eliminate(combined,Z.cols)
    assert not any(any(j<Z.cols for j in rows[i]) for i in active)
    residual = m.distinct_rows(s.MutableSparseMatrix(len(active),137,{
        (i,j-Z.cols):z for i,row in enumerate(active) for j,z in rows[row].items() if j>=Z.cols}))
    return {'first_middle':first_middle,'unit_operations':ops,
            'unit_pivot_count':len(ops),'cohomology':m.encode(residual)}


def compatibility(sector1,sector2):
    mats = {1:m.decode(sector1['cohomology']),2:m.decode(sector2['cohomology'])}
    mixed = s.Matrix.vstack(*[
        m.expand(d*mats[k][:,:68]+mats[k][:,68:136]).row_join(
            mats[k][:,136:137]*(1 if k==2 else d*d)) for k in (2,1)])
    rows,active,ops = m.unit_eliminate(mixed,68,laurent=True)
    assert not any(any(j<68 for j in rows[i]) for i in active)
    target = (a-c)*(b+c)*(c+d**3)
    residuals = [s.cancel(rows[i].get(68,0)) for i in active if rows[i].get(68,0)]
    quotients = [s.cancel(z/target) for z in residuals]
    for z in quotients:
        _,den = z.as_numer_denom()
        coeff,power = den.as_coeff_exponent(d)
        assert coeff.is_Rational and coeff and power.is_Integer
    # Reverse containment is a direct unit multiple, not a radical calculation.
    reverse = next(i for i,z in enumerate(quotients)
                   if z.as_coeff_exponent(d)[0].is_Rational
                   and z.as_coeff_exponent(d)[0]
                   and z.as_coeff_exponent(d)[1].is_Integer)
    pure = {}
    for k in (1,2):
        mat = mats[k]
        own = mat[:,:68] if k==1 else mat[:,68:136]
        assert not own.todok()
        target_pure = (a-c)*(b+c)*(1 if k==1 else c)
        rhs = [z for z in mat[:,136] if z]
        quot = [s.cancel(z/target_pure) for z in rhs]
        assert all(z.is_polynomial(a,b,c) for z in quot)
        unit_index = next(i for i,z in enumerate(quot) if z.is_Rational and z)
        # The opposite sector has zero pure square; w=0 meets its equations.
        pure[str(k)] = {'own_base_velocity_block_zero':True,
                        'residual_generator':str(s.expand(target_pure)),
                        'reverse_unit_index':unit_index,
                        'quotients':[str(z) for z in quot]}
    return {'mixed_matrix':m.encode(mixed),'guard':'d != 0','unit_operations':ops,
            'unit_pivot_count':len(ops),'residual_generator':str(s.expand(target)),
            'residuals':[str(z) for z in residuals],
            'quotients':[str(z) for z in quotients],'reverse_unit_index':reverse,
            'pure':pure,
            'projective_generator':'(a-c)*(b+c)*(c*lambda**3+mu**3)'}


def witness_checks(record=None):
    """Direct all-source replay; no tangent or cohomology certificate is trusted."""
    record = read('witnesses') if record is None else record
    b0,c0 = m.base(); rawb,rawc,planes = m.geometry()
    assert b0[:,rawb[2:]].det()==c0[:,rawc[2:]].det()==1
    assert not m.contract(b0,c0,m.E.OUTSIDE).todok()
    v = m.load('research/ai/2026-10-21-biform-balanced-puncture/verify.py',
               'second_jet_origin')
    prior = json.loads((ROOT/'results/third-boundary-trap-2026-10-21/normal.json').read_text())
    chart = json.loads((ROOT/'results/biform-balanced-puncture-2026-10-21/affine_chart.json').read_text())
    basis,plane = [v.rational_matrix(prior[k]) for k in ('normal_basis','plane_directions')]
    family = basis[:,chart['independent_parameter_pivots']]*v.decode(chart['normal_family'])
    family = m.expand(family-plane*s.Matrix([[0,-a*b],[-a*b,0],[0,a],[a,0]]))
    coordinates = [112*i+j for i in range(8) for j in range(112)
                   if (j//28 if i<4 else j//7%4) in (1,2)]
    nb,nc = normals()[2]
    for i,j in enumerate(coordinates):
        row,col = divmod(j,112)
        assert (nb if row<4 else nc)[row%4,col]==family[i,0]
    for nb,nc in normals().values():
        assert not (m.contract(nb,c0,range(112))+m.contract(b0,nc,range(112))).todok()
    n1,n2 = normals()[1],normals()[2]
    assert not (m.contract(n1[0],n2[1],m.E.OUTSIDE)+m.contract(n2[0],n1[1],m.E.OUTSIDE)).todok()
    for substitution in ({a:c},{b:-c}):
        for nb,nc in normals().values():
            assert not m.contract(nb.subs(substitution),nc.subs(substitution),m.E.OUTSIDE).todok()
    jet = record['cubic_component_two_jet']
    bs,cs = [[m.decode(r) for r in jet[key]] for key in ('B','C')]
    assert bs[0]==b0.subs(c,-d**3) and cs[0]==c0.subs(c,-d**3)
    for mat in bs+cs+[m.decode(jet['source_row_correction_order2'])]:
        for z in mat: s.Poly(z,a,b,d)
    for k in (1,2):
        assert not bs[k][:,rawb[2:]].todok() and not cs[k][:,rawc[2:]].todok()
    expected_b,expected_c = normals()[2][0]+d*normals()[1][0],normals()[2][1]+d*normals()[1][1]
    assert cs[1]==expected_c.subs(c,-d**3)
    internal = m.expand(bs[1]-expected_b.subs(c,-d**3))
    assert all(j in rawb[:2] for i,j in internal.todok())
    f = [sum((m.contract(bs[i],cs[k-i],range(112)) for i in range(3)
              if 0<=k-i<3),s.zeros(112,196)) for k in range(4)]
    w = f[0][m.E.A0,:]; columns = jet['output_pivot_columns']
    inverse = w[:,columns].inv(); y2 = m.decode(jet['source_row_correction_order2'])
    assert not m.expand(f[1][m.E.OUTSIDE,:]).todok()
    assert not m.expand(f[2][m.E.OUTSIDE,:]-y2*w).todok()
    residual = m.expand(f[3][m.E.OUTSIDE,:]-y2*f[1][m.E.A0,:])
    residual = m.expand(residual-residual[:,columns]*inverse*w)
    assert residual==m.decode(jet['uncorrected_order3_residual'])
    assert len(residual.todok())==184
    return {'first_source_rank':12,'row_ranks':[14,14],
            'tangent_boundary_dimension':68,'normal_directions':2,
            'cubic_two_jet_residuals':[0,0],'uncorrected_third_residual_entries':184,
            'exact_linear_components':['a=c','b=-c']}


def reports():
    tangent_reports = [tangent(k) for k in (0,1,2)]
    print('Rebuilt full tangent kernels',flush=True)
    s1,s2 = curvature(1),curvature(2)
    print('Rebuilt full curvature quotient',flush=True)
    return {'tangents':tangent_reports,'curvature':[s1,s2],
            'compatibility':compatibility(s1,s2),'witness_checks':witness_checks()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args = parser.parse_args()
    report = reports()
    if args.write: write('certificates',report)
    else: assert report==read('certificates')
    print(json.dumps({'verified':True,'tangent_dimensions':[m.decode(r['kernel']).cols for r in report['tangents']],
                      'curvature_unit_pivots':report['compatibility']['unit_pivot_count'],
                      'witness_checks':report['witness_checks']},indent=2))


if __name__=='__main__': main()
