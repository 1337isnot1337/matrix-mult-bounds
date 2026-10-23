"""Complete literal-source replay of the pure-fiber polynomial curve."""
import argparse
import gzip
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKAGE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location(
    'pure_conic_literal_source',
    ROOT/'research/ai/2026-10-23-conic-third-jets/verify_symbolic.py')
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)


def encode(matrix):
    return {'shape':[14,112],'entries':[
        [i,j,str(s.expand(z))] for (i,j),z in sorted(matrix.items()) if z]}


def build():
    previous=json.loads(gzip.decompress(
        (ROOT/'results/conic-second-jets-2026-10-21/witnesses.json.gz').read_bytes()
    ))['cubic_component_two_jet']
    result={'schema':'pure-conic-polynomial-curve-v1','base':'c=d=0',
            'output_pivot_columns':previous['output_pivot_columns']}
    for key in ('B','C'):
        result[key]=[encode(v.normalize({index:value.subs(v.d,0)
                        for index,value in v.decode(row,(14,112)).items()}))
                     for row in previous[key]]
    return result


def verify(record=None):
    pins=json.loads((PACKAGE/'sources.json').read_text())['sha256']
    for path,digest in pins.items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest:
            raise ValueError('changed credited source pin')
    expected=build()
    record=expected if record is None else record
    if record['schema']!=expected['schema'] or record['base']!='c=d=0':
        raise ValueError('wrong pure-fiber source')
    bs,cs=[[v.decode(row,(14,112)) for row in record[key]] for key in ('B','C')]
    if len(bs)!=3 or len(cs)!=3 or cs[2]: raise ValueError('wrong polynomial degrees')
    if any(value.has(v.d) for matrix in bs+cs for value in matrix.values()):
        raise ValueError('pure coefficients must be polynomials in a,b')
    for key,maps in (('B',bs),('C',cs)):
        for k in (0,1):
            if v.normalize(v.f.add(maps[k],v.f.negative(v.decode(expected[key][k],(14,112))))):
                raise ValueError('changed credited pure first jet')
    pivots=record['output_pivot_columns']
    if len(pivots)!=12 or len(set(pivots))!=12 or any(type(j) is not int or not 0<=j<196 for j in pivots):
        raise ValueError('wrong pure source minor')
    terms=v.f.source_terms()
    first=[28*i+7*j+z for i,j,z in product((1,2),(1,2),(0,3,6))]
    outside=[i for i in range(112) if i not in first]
    # These are all possible coefficients, including the identically zero
    # highest degree. No higher coefficient can occur in these finite maps.
    fs=[v.normalize(v.f.add(*(v.f.contract(bs[i],cs[k-i],terms)
          for i in range(3) if 0<=k-i<3))) for k in range(5)]
    for k,matrix in enumerate(fs):
        if v.f.rows(matrix,outside): raise ValueError(f'nonzero pure polynomial coefficient {k}')
    rb=[28*p+7*j+z for p,j,z in product((0,3),(0,3),(1,2,4,5))]
    rc=[28*j+7*p+z for p,j,z in product((0,3),(0,3),(1,2,4,5))]
    determinants=[s.factor(v.minor(bs[0],rb[2:]).det()),
                  s.factor(v.minor(cs[0],rc[2:]).det()),
                  s.factor(v.minor(v.f.rows(fs[0],first),pivots).det())]
    if determinants!=[1,1,-1]: raise ValueError('wrong pure leading minors')
    return {'coefficient_ring':'Q[a,b]','base':'c=d=0',
            'source_terms':len(terms),'map_degrees':[2,1],
            'map_coefficient_nonzeros':{'B':list(map(len,bs)),'C':list(map(len,cs))},
            'leading_minor_determinants':list(map(str,determinants)),
            'kernel_coordinates_per_coefficient':19600,
            'complete_polynomial_coefficients_checked':5,
            'fixed_source_kernel_dimension':100,'normal_class':'[1:0]',
            'exact_polynomial_incidence_curve':True,
            'matrix_target_constructed':False,'exponent_improvement':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate',type=Path)
    parser.add_argument('--export',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    record=json.loads(args.certificate.read_text()) if args.certificate else build()
    report=verify(record)
    for path,data in ((args.export,record),(args.output,report)):
        if path:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(report))
