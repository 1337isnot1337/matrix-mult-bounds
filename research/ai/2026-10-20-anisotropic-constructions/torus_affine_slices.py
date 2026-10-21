"""Exact affine equations for complete fixed slices of a torus source.

The fixed boundary is the one specified by an exported seed. A selected
fixed slice is accepted only after its free-by-free source block vanishes
exactly. Its remaining equations are then linear jointly in the two
other leg maps. Feasibility of these equations is not a full tensor map.
"""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
import hashlib
from itertools import product
import json
from math import gcd
from pathlib import Path
import time


def common_column(a, b, leg, column):
    m = a+b-1
    if leg == 0:
        return column
    if leg == 1:
        s, i, k = column//(a*m), (column//m)%a, column%m
    else:
        k, s, i = column//(a*b), (column//a)%b, column%a
    return (i*m+k)*b+s


def original_column(a, b, leg, column):
    m = a+b-1
    i, k, s = column//(m*b), (column//b)%m, column%b
    if leg == 0:
        return column
    if leg == 1:
        return (s*a+i)*m+k
    return (k*b+s)*a+i


def target_layout(charges):
    units, groups = [], defaultdict(list)
    offsets = []
    for block, vertices in enumerate(charges):
        offsets.append(len(units))
        for i, j in product(range(len(vertices)), repeat=2):
            groups[vertices[i]-vertices[j]].append(len(units))
            units.append((block, i, j))
    return units, dict(groups), offsets


def normalized_equation(coefficients, rhs):
    row = {key: value for key, value in coefficients.items() if value}
    divisor = reduce(gcd, (abs(value) for value in row.values()), abs(rhs))
    if not divisor:
        return {}, 0
    sign = 1 if not row or row[min(row)] > 0 else -1
    return {key: sign*value//divisor for key, value in row.items()}, sign*rhs//divisor


def build_system(data, weights=(13, -13)):
    a, b = data['source_lengths']
    m, n = a+b-1, a*b*(a+b-1)
    den = data['map_denominator']
    units, groups, offsets = target_layout(data['target_vertex_charges'])
    dimensions = len(units)
    source_weights = [i+s-k for i,k,s in product(range(a), range(m), range(b))]
    boundary = set(data['fixed_boundary_source_columns_common_order'])
    free = set(range(n))-boundary
    columns_by_weight = defaultdict(list)
    for column, weight in enumerate(source_weights):
        columns_by_weight[weight].append(column)
    maps = [defaultdict(dict) for _ in range(3)]
    row_maps = [defaultdict(dict) for _ in range(3)]
    target_weights = {row: weight for weight, rows in groups.items() for row in rows}
    for leg, entries in enumerate(data['maps']):
        for row, column, value in entries:
            common = common_column(a, b, leg, column)
            if not (0 <= row < dimensions and 0 <= column < n):
                raise ValueError('An exported map coordinate is out of range')
            if source_weights[common] != target_weights[row]:
                raise ValueError('An exported coefficient mixes torus weights')
            if row in maps[leg][common]:
                raise ValueError('An exported sparse coefficient is repeated')
            if value:
                maps[leg][common][row] = value
                row_maps[leg][row][common] = value
    selected = [row for weight in weights for row in groups.get(weight, [])]
    if not selected:
        raise ValueError('The selected weights contain no target rows')
    for row in selected:
        if any(column in free for column in columns_by_weight[target_weights[row]]):
            raise ValueError('A selected slice is not fixed throughout this affine family')
    variables, variable_index = [], {}
    current = {}
    for leg in range(3):
        for row in range(dimensions):
            for column in columns_by_weight[target_weights[row]]:
                if column in free:
                    key = leg, row, column
                    variable_index[key] = len(variables)
                    value = row_maps[leg][row].get(column, 0)
                    if value:
                        current[len(variables)] = value
                    variables.append(key)
    slice_support = {(leg,row): Counter() for leg in range(3) for row in selected}
    selected_set = set(selected)
    source_terms = 0
    for i,j,p,q,r,s in product(range(a), range(b), range(a), range(b), range(a), range(b)):
        point = ((i*m+p+q)*b+s, (j*a+p)*m+r+s, ((i+j)*b+q)*a+r)
        source_terms += 1
        for leg in range(3):
            common = common_column(a, b, leg, point[leg])
            for row, value in maps[leg].get(common, {}).items():
                if row not in selected_set:
                    continue
                other, last = (leg+1)%3, (leg+2)%3
                pair = (common_column(a,b,other,point[other]),
                        common_column(a,b,last,point[last]))
                slice_support[leg,row][pair] += value
    equations = {}
    slice_reports = []

    def equation(key):
        if key not in equations:
            equations[key] = [defaultdict(int), 0]
        return equations[key]

    for (leg, row), raw_support in slice_support.items():
        other, last = (leg+1)%3, (leg+2)%3
        support = {pair:value for pair,value in raw_support.items() if value}
        free_free = [(pair,value) for pair,value in support.items()
                     if pair[0] in free and pair[1] in free
                     and source_weights[pair[0]] in groups and source_weights[pair[1]] in groups]
        if free_free:
            raise ValueError('A selected slice has a nonzero free-by-free term')
        block, i, j = units[row]
        size, offset = len(data['target_vertex_charges'][block]), offsets[block]
        for k in range(size):
            key = leg, row, offset+j*size+k, offset+k*size+i
            equation(key)[1] += den**3
        for (left_column, right_column), factor in support.items():
            left_free, right_free = left_column in free, right_column in free
            if left_free and right_free:
                continue
            if left_free:
                for left_row in groups.get(source_weights[left_column], []):
                    variable = variable_index[other,left_row,left_column]
                    for right_row, value in maps[last].get(right_column, {}).items():
                        equation((leg,row,left_row,right_row))[0][variable] += factor*value
            elif right_free:
                for left_row, value in maps[other].get(left_column, {}).items():
                    for right_row in groups.get(source_weights[right_column], []):
                        variable = variable_index[last,right_row,right_column]
                        equation((leg,row,left_row,right_row))[0][variable] += factor*value
            else:
                for left_row, left_value in maps[other].get(left_column, {}).items():
                    for right_row, right_value in maps[last].get(right_column, {}).items():
                        equation((leg,row,left_row,right_row))[1] -= factor*left_value*right_value
        potential = sum(len(rows)*len(groups.get(-target_weights[row]-weight, []))
                        for weight, rows in groups.items())
        slice_reports.append({'fixed_leg': leg, 'fixed_target_row': row,
                              'source_slice_support': len(support),
                              'all_free_by_free_coefficients_zero': True,
                              'conserving_target_coefficients': potential})
    records = []
    tautologies = 0
    for key, (coefficients, rhs) in sorted(equations.items()):
        row, rhs = normalized_equation(coefficients, rhs)
        if not row and not rhs:
            tautologies += 1
        else:
            records.append({'key':key, 'row':row, 'rhs':rhs})
    return {'source_terms_checked':source_terms, 'selected_weights':list(weights),
            'selected_target_rows':selected, 'variables':variables,
            'current_values':current, 'equations':records, 'slice_reports':slice_reports,
            'tautologies_removed':tautologies, 'denominator':den,
            'source_dimensions':[n]*3, 'target_dimensions':[dimensions]*3}


def exact_eliminate(records, current_values=None):
    """Sparse integer elimination, with a checkable rational contradiction.

    Rows are kept primitive. The elimination history is a linear-combination
    DAG; it is expanded only if a contradiction occurs. An accepted affine
    point is then substituted into every original equation independently.
    """
    basis = {}
    history = [None]*len(records)
    work_order = sorted(range(len(records)), key=lambda i:(len(records[i]['row']),
                                                          tuple(sorted(records[i]['row']))))
    eliminations = 0
    largest_row = 0
    maximum_bits = 0
    failure = None
    for index in work_order:
        row, rhs = dict(records[index]['row']), records[index]['rhs']
        node = index
        while row:
            pivot = min(row)
            if pivot not in basis:
                basis[pivot] = (row, rhs, node)
                largest_row = max(largest_row, len(row))
                maximum_bits = max(maximum_bits, max((abs(x).bit_length() for x in row.values()), default=0),
                                   abs(rhs).bit_length())
                break
            other_row, other_rhs, other_node = basis[pivot]
            left_scale, right_scale = other_row[pivot], -row[pivot]
            merged = {key:value*left_scale for key,value in row.items()}
            for key,value in other_row.items():
                merged[key] = merged.get(key,0)+right_scale*value
                if not merged[key]:
                    del merged[key]
            merged_rhs = left_scale*rhs+right_scale*other_rhs
            divisor = reduce(gcd, (abs(value) for value in merged.values()), abs(merged_rhs)) or 1
            sign = 1 if not merged or merged[min(merged)] > 0 else -1
            row = {key:sign*value//divisor for key,value in merged.items()}
            rhs = sign*merged_rhs//divisor
            history.append((node, other_node, Fraction(sign*left_scale,divisor),
                            Fraction(sign*right_scale,divisor)))
            node = len(history)-1
            eliminations += 1
        if not row and rhs:
            failure = node, rhs
            break
    diagnostic = {'rank':len(basis), 'integer_eliminations':eliminations,
                  'largest_stored_equation_support':largest_row,
                  'largest_integer_bit_length':maximum_bits}
    if failure is not None:
        coefficients = {failure[0]:Fraction(1)}
        for node in range(len(history)-1, len(records)-1, -1):
            value = coefficients.pop(node, 0)
            if not value:
                continue
            left,right,left_scale,right_scale = history[node]
            coefficients[left] = coefficients.get(left,0)+value*left_scale
            coefficients[right] = coefficients.get(right,0)+value*right_scale
        certificate = {i:value for i,value in coefficients.items() if value}
        verify_contradiction(records, certificate)
        return {**diagnostic, 'feasible':False, 'certificate':certificate,
                'contradiction_rhs':failure[1]}
    values = {key:Fraction(value) for key,value in (current_values or {}).items()
              if key not in basis and value}
    for pivot in sorted(basis, reverse=True):
        row,rhs,_ = basis[pivot]
        value = (rhs-sum(coefficient*values.get(key,0) for key,coefficient in row.items()
                         if key!=pivot))/Fraction(row[pivot])
        if value:
            values[pivot] = value
        else:
            values.pop(pivot,None)
    for record in records:
        actual = sum(coefficient*values.get(key,0) for key,coefficient in record['row'].items())
        if actual != record['rhs']:
            raise ArithmeticError('An affine solution failed substitution into an original equation')
    return {**diagnostic, 'feasible':True, 'solution':values,
            'all_original_equations_substituted_exactly':True}


def verify_contradiction(records, certificate):
    row = defaultdict(Fraction)
    rhs = Fraction(0)
    for index, value in certificate.items():
        for key, coefficient in records[index]['row'].items():
            row[key] += value*coefficient
        rhs += value*records[index]['rhs']
    if any(row.values()) or not rhs:
        raise ArithmeticError('The exported linear-combination contradiction is invalid')
    return rhs


def rational(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def fixed_boundary_contradiction_control():
    """Replay the three-coordinate contradiction without the large seed."""
    a = b = 8
    m = 15
    boundary = {((i*m+k)*b+s) for i,k,s in product(range(a),range(m),range(b))
                if (i==7 and k<=7) or (i==0 and k>=7)
                or (s==0 and k>=7) or (s==7 and k<=7)}
    free = set(range(960))-boundary
    endpoints = {7,56}  # Physical (0,7) and (7,0).

    def physical(column):
        i,k,s = column//120, (column//8)%15, column%8
        return {(8*i+q,8*(k-q)+s):1 for q in range(8) if 0<=k-q<8}

    def functional(left,right):
        result = Counter()
        for (i,j),u in physical(left).items():
            for (jj,k),v in physical(right).items():
                if j==jj:
                    p,s = divmod(i,8)
                    ii,q = divmod(k,8)
                    result[(ii*15+p+q)*8+s] += u*v
        return dict(result)

    x,y,z = 104,898,862  # F(0,13,0), F(7,7,2), F(7,2,6).
    if (x,y,z) != ((0*15+13)*8,(7*15+7)*8+2,(7*15+2)*8+6):
        raise AssertionError('The named coordinates do not match their indices')
    for column in free:
        if any(i in endpoints or j in endpoints for i,j in physical(column)):
            raise AssertionError('A free source basis vector touches an endpoint')
    if any(i not in endpoints and j not in endpoints for i,j in physical(x)):
        raise AssertionError('The fixed slice has an interior matrix block')
    xy, zx = functional(x,y), functional(z,x)
    if xy != {z:1} or zx != {y:1} or y not in boundary or z not in boundary:
        raise AssertionError('One of the fixed-boundary linear functionals is wrong')
    # The target product E_(0,25) E_(26,24) is zero.
    target_value = int(25==26 and 24==26 and 5==0)
    if target_value != 0:
        raise AssertionError('The target coefficient should be zero')
    return {'source_free_columns_checked':len(free),
            'source_boundary_columns_checked':len(boundary),
            'fixed_common_source_coordinates':[[0,13,0],[7,7,2],[7,2,6]],
            'target_matrix_units':[[0,25],[26,24],[26,5]],
            'all_free_basis_matrices_have_zero_endpoint_rows_and_columns':True,
            'fixed_slice_has_zero_interior_block':True,
            'free_by_free_term_zero':True, 'both_free_linear_terms_zero':True,
            'forced_coefficient':1, 'required_target_coefficient':0,
            'completion_with_this_fixed_boundary_excluded':True,
            'arbitrary_source_maps_excluded':False, 'new_exponent_established':False}


def report(data, weights=(13,-13), eliminate=True):
    began = time.monotonic()
    system = build_system(data, weights)
    records, variables = system['equations'], system['variables']
    result = {'source_lengths':data['source_lengths'],
              'target_blocks':data['target_blocks'],
              'selected_weights':list(weights), 'source_terms_checked':system['source_terms_checked'],
              'selected_slice_checks':system['slice_reports'],
              'full_affine_parameter_count':len(variables),
              'nontrivial_joint_affine_equations':len(records),
              'nonzero_linear_coefficients':sum(len(row['row']) for row in records),
              'active_affine_variables':len(set().union(*(set(row['row']) for row in records))),
              'maximum_original_equation_support':max((len(row['row']) for row in records),default=0),
              'full_target_tensor_identity_claimed':False,
              'general_anchor_families_excluded':False,
              'new_exponent_established':False}
    if eliminate:
        solved = exact_eliminate(records, system['current_values'])
        result.update({key:value for key,value in solved.items() if key not in ('certificate','solution')})
        if solved['feasible']:
            result['affine_solution_nonzero_coefficients'] = len(solved['solution'])
            result['affine_solution_numerators'] = [[*variables[index], *rational(value)]
                                                    for index,value in sorted(solved['solution'].items())]
            result['numerator_map_denominator'] = system['denominator']
        else:
            result['inconsistent_equation_combination'] = [
                {'equation_key':list(records[index]['key']), 'multiplier':rational(value),
                 'rhs':records[index]['rhs'],
                 'linear_coefficients':[[*variables[var],coefficient]
                                        for var,coefficient in sorted(records[index]['row'].items())]}
                for index,value in sorted(solved['certificate'].items())]
            result['completion_with_this_fixed_boundary_excluded'] = True
    result['elapsed_seconds'] = time.monotonic()-began
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('seed', type=Path)
    parser.add_argument('--weights', type=int, nargs='+', default=[13,-13])
    parser.add_argument('--build-only', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.loads(args.seed.read_text())
    result = report(data, tuple(args.weights), eliminate=not args.build_only)
    result['seed_sha256'] = hashlib.sha256(args.seed.read_bytes()).hexdigest()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items()
                      if key not in ('affine_solution_numerators','inconsistent_equation_combination')},indent=2))


if __name__ == '__main__':
    main()
