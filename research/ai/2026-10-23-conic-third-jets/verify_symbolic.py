"""Independent source replay over Q[a,b,d,d^-1] for the explicit three-jet."""
import argparse
import ast
import gzip
import importlib.util
from itertools import product
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
PACKAGE=ROOT/'research/ai/2026-10-23-conic-third-jets'
spec=importlib.util.spec_from_file_location('symbolic_literal_source',PACKAGE/'verify.py')
f=importlib.util.module_from_spec(spec); spec.loader.exec_module(f)
a,b,d=s.symbols('a b d')
SYMBOLS={'a':a,'b':b,'d':d}


def expression(text):
    """Read only rational arithmetic in the three formal parameters."""
    def read(node):
        if isinstance(node,ast.Constant) and type(node.value) is int:
            return s.Integer(node.value)
        if isinstance(node,ast.Name) and node.id in SYMBOLS: return SYMBOLS[node.id]
        if isinstance(node,ast.UnaryOp) and isinstance(node.op,(ast.UAdd,ast.USub)):
            value=read(node.operand)
            return -value if isinstance(node.op,ast.USub) else value
        if isinstance(node,ast.BinOp):
            left,right=read(node.left),read(node.right)
            if isinstance(node.op,ast.Add): return left+right
            if isinstance(node.op,ast.Sub): return left-right
            if isinstance(node.op,ast.Mult): return left*right
            if isinstance(node.op,ast.Div): return left/right
            if isinstance(node.op,ast.Pow) and right.is_Integer: return left**right
        raise ValueError('coefficient is not rational polynomial arithmetic')
    value=s.cancel(read(ast.parse(text,mode='eval').body))
    numerator,denominator=map(lambda z:s.Poly(z,a,b,d,domain=s.QQ),s.fraction(value))
    terms=denominator.terms()
    if (len(terms)!=1 or terms[0][0][:2]!=(0,0) or terms[0][0][2]>2):
        raise ValueError('coefficient has a pole outside the stated d chart')
    return value


def normalize(matrix):
    values={index:s.cancel(value) for index,value in matrix.items()}
    return {index:value for index,value in values.items() if value}


def decode(record,shape):
    if record['shape']!=list(shape): raise ValueError('wrong symbolic matrix shape')
    matrix={}
    for i,j,value in record['entries']:
        if (type(i) is not int or type(j) is not int or (i,j) in matrix
                or not 0<=i<shape[0] or not 0<=j<shape[1]):
            raise ValueError('wrong symbolic matrix coordinate')
        matrix[i,j]=expression(value)
    return normalize(matrix)


def minor(matrix,columns):
    return s.Matrix(len(columns),len(columns),lambda i,j:matrix.get((i,columns[j]),0))


def verify(record):
    if record['base']!='c=-d^3': raise ValueError('wrong conic chart')
    pivots=record['output_pivot_columns']
    if (len(pivots)!=12 or len(set(pivots))!=12
            or any(type(j) is not int or not 0<=j<196 for j in pivots)):
        raise ValueError('wrong first-source minor coordinates')
    bs,cs=[[decode(row,(14,112)) for row in record[key]] for key in ('B','C')]
    ys=[decode(row,(100,12)) for row in record['source_row_corrections']]
    if len(bs)!=4 or len(cs)!=4 or len(ys)!=3: raise ValueError('wrong symbolic jet order')
    prior=json.loads(gzip.decompress((ROOT/'results/conic-second-jets-2026-10-21/witnesses.json.gz').read_bytes()))['cubic_component_two_jet']
    for key,maps in (('B',bs),('C',cs)):
        for k in (0,1):
            if normalize(f.add(maps[k],f.negative(decode(prior[key][k],(14,112))))):
                raise ValueError('changed credited constant or first coefficient')
    delta=(a+d**3)*(b-d**3)
    weights=[-delta**2*(b-2*d**3)/(3*d**2),
             -d*delta**2*(b+d**3)/3,
             delta**2*(b-d**3)/(3*d**2),b*d*delta**2/3]
    # Extract the middle-one normal from the credited first jet N2+d*N1.
    normal_b={index:value/d for index,value in bs[1].items() if index[1]//28==1}
    normal_c={index:value/d for index,value in cs[1].items() if index[1]//7%4==1}
    expected_b={index:delta*value/3 for index,value in normal_b.items()}
    expected_c={index:delta*value/3 for index,value in normal_c.items()}
    for r,weight in zip((0,1,2,5),weights):
        for index in ((2*r,1),(2*r+1,2)):
            expected_b[index]=expected_b.get(index,0)+weight
    for key,maps,expected in (('B',bs,expected_b),('C',cs,expected_c)):
        difference=f.add(maps[2],f.negative(decode(prior[key][2],(14,112))),f.negative(expected))
        if normalize(difference): raise ValueError('wrong five-field second correction')
    terms=f.source_terms()
    first=[28*i+7*j+z for i,j,z in product((1,2),(1,2),(0,3,6))]
    outside=[i for i in range(112) if i not in first]
    fs=[normalize(f.add(*(f.contract(bs[i],cs[k-i],terms) for i in range(k+1))))
        for k in range(4)]
    if f.rows(fs[0],outside): raise ValueError('nonzero constant kernel coefficient')
    rb=[28*p+7*j+z for p,j,z in product((0,3),(0,3),(1,2,4,5))]
    rc=[28*j+7*p+z for p,j,z in product((0,3),(0,3),(1,2,4,5))]
    determinants=[s.factor(minor(bs[0],rb[2:]).det()),
                  s.factor(minor(cs[0],rc[2:]).det()),
                  s.factor(minor(f.rows(fs[0],first),pivots).det())]
    if any(not z.is_Rational or not z for z in determinants):
        raise ValueError('leading minor is not a nonzero constant')
    for k in range(1,4):
        residual=normalize(f.add(f.rows(fs[k],outside),f.negative(f.add(*(
            f.multiply(ys[i-1],f.rows(fs[k-i],first)) for i in range(1,k+1))))))
        if residual: raise ValueError(f'nonzero symbolic order {k} incidence coefficient')
    return {'field':'Q(a,b,d)','coefficient_ring':'Q[a,b,d,d^-1]',
            'scope':'Every complex a,b,d with d nonzero, c=-d^3',
            'source_terms':len(terms),'jet_order':3,
            'leading_minor_determinants':list(map(str,determinants)),
            'kernel_coordinates_per_order':19600,'positive_orders_checked':3,
            'normal_class':'[1:d]','matrix_target_constructed':False,
            'all_order_lift_established':False,'exponent_improvement':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report=verify(json.loads(args.witness.read_text()))
    if args.output: args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
