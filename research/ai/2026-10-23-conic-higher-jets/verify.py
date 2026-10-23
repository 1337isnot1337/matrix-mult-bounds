"""Independent rational replay of explicit finite-order incidence witnesses.

Only the Python standard library is used. No tangent solver, predecessor
operator, symbolic algebra package, or cohomology certificate is imported.
"""
import argparse
import ast
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def decode(record, shape):
    if record['shape'] != list(shape):
        raise ValueError('wrong matrix shape')
    matrix = {}
    for i,j,value in record['entries']:
        if (type(i) is not int or type(j) is not int
                or not 0<=i<shape[0] or not 0<=j<shape[1] or (i,j) in matrix):
            raise ValueError('wrong matrix coordinate')
        value = Fraction(value)
        if not value:
            raise ValueError('stored zero matrix entry')
        matrix[i,j] = value
    return matrix


def add(*matrices):
    result = defaultdict(Fraction)
    for matrix in matrices:
        for index,value in matrix.items(): result[index] += value
    return {index:value for index,value in result.items() if value}


def negative(matrix):
    return {index:-value for index,value in matrix.items()}


def rows(matrix, selected):
    positions = {old:new for new,old in enumerate(selected)}
    return {(positions[i],j):value for (i,j),value in matrix.items() if i in positions}


def multiply(left, right):
    byrow = defaultdict(list)
    for (i,j),value in right.items(): byrow[i].append((j,value))
    result = defaultdict(Fraction)
    for (i,k),value in left.items():
        for j,coefficient in byrow[k]: result[i,j] += value*coefficient
    return {index:value for index,value in result.items() if value}


def rank(matrix):
    byrow = defaultdict(dict)
    for (i,j),value in matrix.items(): byrow[i][j] = value
    pivots = {}
    for _,original in sorted(byrow.items()):
        row = dict(original)
        while row:
            j = min(row)
            value = row[j]
            if j not in pivots:
                pivots[j] = {k:z/value for k,z in row.items()}
                break
            for k,z in pivots[j].items():
                updated = row.get(k,0)-value*z
                if updated: row[k] = updated
                else: row.pop(k,None)
    return len(pivots)


def source_terms():
    # Coordinate convention (u,v,z) -> 28u+7v+z.
    # Rebuilt literally from the three cyclic C(4,4) factors.
    return [(28*i+7*r+6-p-q, 28*p+7*j+6-s-r, 28*s+7*q+6-i-j)
            for i,j,p,q,s,r in product(range(4),repeat=6)]


def contract(left, right, terms):
    byleft,byright = defaultdict(list),defaultdict(list)
    for (i,j),value in left.items(): byleft[j].append((i,value))
    for (i,j),value in right.items(): byright[j].append((i,value))
    result = defaultdict(Fraction)
    for a,b,c in terms:
        for i,x in byleft[b]:
            for j,y in byright[c]: result[a,14*i+j] += x*y
    return {index:value for index,value in result.items() if value}


def verify(record):
    if record['parameters'] != {'a':'1','b':'2','d':'1'}:
        raise ValueError('this witness is for the stated rational point only')
    jet = record['witness']
    order = len(jet['source_row_corrections'])
    if len(jet['B'])!=order+1 or len(jet['C'])!=order+1:
        raise ValueError('wrong jet order')
    bs,cs = [[decode(matrix,(14,112)) for matrix in jet[key]] for key in ('B','C')]
    ys = [decode(matrix,(100,12)) for matrix in jet['source_row_corrections']]
    root = Path(__file__).resolve().parents[3]
    prior = json.loads((root/'results/conic-third-jets-2026-10-23/mixed-family.json').read_text())
    def evaluate(text):
        variables = {'a':Fraction(1),'b':Fraction(2),'d':Fraction(1)}
        def visit(node):
            if isinstance(node,ast.Constant) and type(node.value) is int:
                return Fraction(node.value)
            if isinstance(node,ast.Name) and node.id in variables:
                return variables[node.id]
            if isinstance(node,ast.UnaryOp) and isinstance(node.op,(ast.UAdd,ast.USub)):
                value = visit(node.operand)
                return -value if isinstance(node.op,ast.USub) else value
            if isinstance(node,ast.BinOp):
                left,right = visit(node.left),visit(node.right)
                if isinstance(node.op,ast.Add): return left+right
                if isinstance(node.op,ast.Sub): return left-right
                if isinstance(node.op,ast.Mult): return left*right
                if isinstance(node.op,ast.Div): return left/right
                if isinstance(node.op,ast.Pow) and right.denominator == 1:
                    return left**int(right)
            raise ValueError('unsupported predecessor expression')
        return visit(ast.parse(text,mode='eval').body)
    for key,maps in (('B',bs),('C',cs)):
        for k in range(3):
            expected = {(i,j):evaluate(value) for i,j,value in prior[key][k]['entries']}
            expected = {index:value for index,value in expected.items() if value}
            if maps[k] != expected:
                raise ValueError('changed credited coefficient through order two')
    baseline = json.loads((root/'results/conic-higher-jets-2026-10-23/rational-ten-jet.json').read_text())['witness']
    baseline_b,baseline_c = [[decode(matrix,(14,112)) for matrix in baseline[key]]
                             for key in ('B','C')]
    baseline_y = [decode(matrix,(100,12)) for matrix in baseline['source_row_corrections']]
    for key,maps,expected in (('B',bs,baseline_b),('C',cs,baseline_c)):
        for k in range(len(expected)-1):
            if maps[k] != expected[k]:
                raise ValueError(f'changed fixed prefix in {key} at order {k}')
    for k in range(len(baseline_y)-1):
        if ys[k] != baseline_y[k]:
            raise ValueError(f'changed fixed prefix in source correction Y{k+1}')
    terms = source_terms()
    first = [28*i+7*j+z for i,j,z in product((1,2),(1,2),(0,3,6))]
    outside = [i for i in range(112) if i not in first]
    fs = [add(*(contract(bs[i],cs[k-i],terms) for i in range(k+1)))
          for k in range(order+1)]
    if rows(fs[0],outside): raise ValueError('nonzero constant kernel coefficient')
    ranks = [rank(bs[0]),rank(cs[0]),rank(rows(fs[0],first))]
    if ranks != [14,14,12]: raise ValueError('wrong leading ranks')
    for k in range(1,order+1):
        residual = add(rows(fs[k],outside),negative(add(*(
            multiply(ys[i-1],rows(fs[k-i],first)) for i in range(1,k+1)))))
        if residual: raise ValueError(f'nonzero order {k} incidence coefficient')
    nonboundary = (sum(j//28 in (1,2) for i,j in bs[1])
                   +sum(j//7%4 in (1,2) for i,j in cs[1]))
    if not nonboundary: raise ValueError('missing first normal motion')
    return {'field':'Q','parameters':record['parameters'],'source_terms':len(terms),
            'leading_map_ranks':ranks[:2],'leading_first_source_rank':ranks[2],
            'jet_order':order,'kernel_coordinates_per_order':100*196,
            'positive_orders_checked':order,'first_nonboundary_entries':nonboundary,
            'matrix_target_constructed':False,'all_order_lift_established':False,
            'exponent_improvement':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness',type=Path)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.witness.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
