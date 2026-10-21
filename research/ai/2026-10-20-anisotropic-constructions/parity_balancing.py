"""Support balancing for the A(5,5) parity110 degeneration.

Exact certificates concern support distributions, not tensor restrictions.
NumPy and SciPy are imported only by numerical discovery routines.
"""

from fractions import Fraction
from itertools import product
import argparse
import hashlib
import json
from math import comb
from pathlib import Path


def source_data():
    points = []
    triples = []
    parities = [[None] * 225 for _ in range(3)]
    for i, j, p, q, r, s in product(range(5), repeat=6):
        weights = (p + q - i - s, r + s - j - p, i + j - q - r)
        shifted = tuple((w + c) % 2 for w, c in zip(weights, (1, 1, 0)))
        if sum(shifted) != 2:
            continue
        point = ((i * 9 + p + q) * 5 + s,
                 (j * 5 + p) * 9 + r + s,
                 ((i + j) * 5 + q) * 5 + r)
        points.append(point)
        triples.append((i, j, p, q, r, s))
        for axis in range(3):
            old = parities[axis][point[axis]]
            if old is not None and old != shifted[axis]:
                raise ArithmeticError('Inconsistent coordinate parity')
            parities[axis][point[axis]] = shifted[axis]
    if len(points) != 11725 or len(set(points)) != len(points) or any(None in p for p in parities):
        raise ArithmeticError('Unexpected source support')
    return points, triples, parities


def tight_weights():
    """Injective integer weights; their sum is zero on every source term."""
    return [
        [-i+9*k-81*s for i,k,s in product(range(5),range(9),range(5))],
        [-j-9*p+81*k for j,p,k in product(range(5),range(5),range(9))],
        [h-9*q-81*r for h,q,r in product(range(9),range(5),range(5))],
    ]


def exact_optimum_checks():
    """Rational bracket and a strict capacity comparison, without logarithms."""
    polynomial = lambda p:225*p*p-19266*p+12769
    low, high = Fraction(2,3), Fraction(67,100)
    values = (polynomial(low),polynomial(high))
    if not values[0] > 0 > values[1] or not 450*high-19266 < 0:
        raise ArithmeticError('The exact marginal optimum bracket failed')
    left = 19683*112**4*113**5
    right = 64*212**9
    if not left > right:
        raise ArithmeticError('The rational-point entropy does not exceed the target screen')
    points, _, _ = source_data()
    weights = tight_weights()
    if any(len(set(row)) != 225 for row in weights):
        raise ArithmeticError('Tight weights are not injective')
    if any(sum(weights[axis][point[axis]] for axis in range(3)) != 0 for point in points):
        raise ArithmeticError('A source term violates tightness')
    return {'p_polynomial':[225,-19266,12769], 'p_bracket':[str(low),str(high)],
            'polynomial_values':[str(v) for v in values],
            'strict_capacity_comparison':{'left':str(left),'right':str(right),'verified':True},
            'injective_coordinate_weight_counts':[225,225,225],
            'zero_weight_support_equations_checked':len(points)}


def coordinate_orbit(axis, coordinate):
    """Canonical coordinate under the three convolution reversals."""
    if axis == 0:
        s, quotient = coordinate % 5, coordinate // 5
        k, i = quotient % 9, quotient // 9
        return (min(i, 4-i), min(k, 8-k), min(s, 4-s))
    if axis == 1:
        k, quotient = coordinate % 9, coordinate // 9
        p, j = quotient % 5, quotient // 5
        return (min(j, 4-j), min(p, 4-p), min(k, 8-k))
    r, quotient = coordinate % 5, coordinate // 5
    q, k = quotient % 5, quotient // 5
    return (min(k, 8-k), min(q, 4-q), min(r, 4-r))


def term_orbit(variables):
    """Canonical term under simultaneous reversal of each input pair."""
    i, j, p, q, r, s = variables
    return tuple(value for pair in ((i, j), (p, q), (r, s))
                 for value in min(pair, tuple(4-x for x in pair)))


def orbit_data():
    points, variables, parities = source_data()
    coordinate_groups = []
    coordinate_inverse = []
    for axis in range(3):
        groups = {}
        for c in range(225):
            groups.setdefault(coordinate_orbit(axis, c), []).append(c)
        coordinate_groups.append(list(groups.values()))
        coordinate_inverse.append({c: k for k, g in enumerate(groups.values()) for c in g})
    term_groups = {}
    for k, v in enumerate(variables):
        term_groups.setdefault(term_orbit(v), []).append(k)
    term_groups = list(term_groups.values())
    incidence = []
    for group in term_groups:
        hit = tuple(coordinate_inverse[axis][points[group[0]][axis]] for axis in range(3))
        for k in group:
            if tuple(coordinate_inverse[axis][points[k][axis]] for axis in range(3)) != hit:
                raise ArithmeticError('Support orbit is not coordinate-orbit constant')
        incidence.append(hit)
    return points, parities, coordinate_groups, term_groups, incidence


def rational_coordinate_marginals(p):
    """p_X=p_Y=p; p_Z=2-2p, uniform in each shifted parity class."""
    _, _, parities = source_data()
    odds = (p, p, 2-2*p)
    even = (112, 112, 113)
    odd = (113, 113, 112)
    return [[odds[axis]/odd[axis] if parity else (1-odds[axis])/even[axis]
             for parity in parities[axis]] for axis in range(3)]


def ipfp(z=None, p=None, sweeps=400):
    import numpy as np
    points, _, parities = source_data()
    points = np.asarray(points, dtype=np.int64)
    if p is not None:
        target = np.asarray(rational_coordinate_marginals(Fraction(p)), dtype=float)
    else:
        if z is None:
            # Stationarity reduces exactly to 113*z**2-112*z-226=0.
            z = (112 + (112**2+8*113**2)**0.5)/(2*113)
        target = np.asarray([[z**parity/(e+o*z) for parity in pi]
                             for pi, e, o in zip(parities, (112,112,113), (113,113,112))])
    masses = np.full(len(points), 1/len(points))
    logs = np.zeros((3,225))
    history = []
    for sweep in range(1, sweeps+1):
        for axis in range(3):
            current = np.bincount(points[:,axis], weights=masses, minlength=225)
            factors = target[axis]/current
            masses *= factors[points[:,axis]]
            logs[axis] += np.log(factors)
        if sweep == 1 or sweep % 50 == 0:
            current = np.asarray([np.bincount(points[:,axis], weights=masses, minlength=225)
                                  for axis in range(3)])
            error = float(np.max(np.abs(current-target)))
            history.append({'sweep':sweep, 'maximum_absolute_marginal_error':error,
                            'minimum_mass':float(masses.min()), 'maximum_mass':float(masses.max())})
            if error < 2e-15:
                break
    report = {'z':z, 'p':str(p) if p is not None else None, 'support_terms':len(points),
              'history':history, 'diagonal_log_ranges':[[float(row.min()),float(row.max())] for row in logs],
              'new_exponent_established':False, 'target_restriction_constructed':False}
    return report, masses, logs


def discover_rational(p, uniform_term_mass=Fraction(1,10**10)):
    """Find an orbit-invariant feasible point; reconstruct it with exact rationals."""
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    points, parities, cgroups, tgroups, incidence = orbit_data()
    dims = [len(g) for g in cgroups]
    offsets = [0, dims[0], dims[0]+dims[1]]
    rows = [offsets[axis]+hit[axis] for hit in incidence for axis in range(3)]
    cols = [k for k in range(len(incidence)) for _ in range(3)]
    matrix = coo_matrix((np.ones(len(rows)), (rows,cols)), shape=(sum(dims),len(incidence))).tocsc()
    coordinate_targets = rational_coordinate_marginals(p)
    target = [sum((coordinate_targets[axis][c] for c in group), Fraction(0))
              for axis in range(3) for group in cgroups[axis]]
    baseline = [Fraction(0) for _ in target]
    for group, hit in zip(tgroups,incidence):
        for axis in range(3):
            baseline[offsets[axis]+hit[axis]] += len(group)*uniform_term_mass
    residual_target = [value-base for value,base in zip(target,baseline)]
    solved = linprog(np.zeros(len(tgroups)), A_eq=matrix, b_eq=np.asarray(residual_target,dtype=float),
                     bounds=(0,None), method='highs', options={'primal_feasibility_tolerance':1e-9})
    if not solved.success:
        raise ArithmeticError(solved.message)
    active = np.flatnonzero(solved.x > 1e-9).tolist()
    # A basic feasible solution has independent active columns. Solve all
    # marginal equations exactly rather than accepting the solver residual.
    import sympy as sp
    active_matrix = sp.Matrix(matrix[:,active].toarray().astype(int).tolist())
    rhs = sp.Matrix([sp.Rational(q.numerator,q.denominator) for q in residual_target])
    solution, parameters = active_matrix.gauss_jordan_solve(rhs)
    if parameters.rows:
        raise ArithmeticError('Numerical support did not specify an independent feasible basis')
    values = [Fraction(int(value.p),int(value.q)) for value in solution]
    if any(value < 0 for value in values):
        raise ArithmeticError('Exact reconstruction has a negative mass')
    record = {'p': [p.numerator,p.denominator], 'coordinate_orbit_counts':dims,
              'uniform_term_mass':[uniform_term_mass.numerator,uniform_term_mass.denominator],
              'support_orbits':len(tgroups), 'active_support_orbits':len(active),
              'orbit_masses':[[index,str(value.numerator),str(value.denominator)]
                              for index,value in zip(active,values) if value],
              'new_exponent_established':False, 'target_restriction_constructed':False}
    verify_rational(record)
    return record


def verify_rational(record):
    """Replay every support coefficient and all 675 exact marginal equations."""
    points, parities, cgroups, tgroups, incidence = orbit_data()
    p = Fraction(*record['p'])
    marginals = [[Fraction(0) for _ in range(225)] for _ in range(3)]
    baseline = Fraction(*record.get('uniform_term_mass',[0,1]))
    if baseline < 0:
        raise ArithmeticError('Negative uniform term mass')
    for point in points:
        for axis in range(3):
            marginals[axis][point[axis]] += baseline
    seen = set()
    for index, numerator, denominator in record['orbit_masses']:
        if index in seen or not 0 <= index < len(tgroups):
            raise ArithmeticError('Duplicate or invalid support orbit')
        seen.add(index)
        value = Fraction(int(numerator),int(denominator))
        if value <= 0:
            raise ArithmeticError('Nonpositive orbit mass')
        value /= len(tgroups[index])
        for k in tgroups[index]:
            for axis in range(3):
                marginals[axis][points[k][axis]] += value
    if marginals != rational_coordinate_marginals(p):
        raise ArithmeticError('Exact marginal identity failed')
    return {'p':str(p), 'support_terms':len(points), 'support_orbits':len(tgroups),
            'active_orbits':len(seen), 'exact_marginal_equations_checked':675,
            'uniform_term_mass':str(baseline), 'strictly_positive_on_full_support':baseline>0,
            'exact_probability_total':str(sum(marginals[0])), 'verified':True}


def certificate_report(directory):
    records = []
    for name in ('2_3','67_100'):
        path = directory/f'parity_balancing_p_{name}.json'
        replay = verify_rational(json.loads(path.read_text()))
        replay['certificate'] = path.name
        replay['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        records.append(replay)
    return {'exact_endpoint_replays':records, 'exact_optimum_checks':exact_optimum_checks(),
            'total_exact_original_coordinate_marginal_equations':sum(r['exact_marginal_equations_checked'] for r in records),
            'arithmetic':'Python Fraction and integers; no floating acceptance decision',
            'written_consequence':'Positive exact optimal marginals and sharp cyclic asymptotic slice-rank capacity',
            'proof_review_status':'Internal arguments checked by a second agent in this generating session; no external independent review or formalization',
            'one_copy_matrix_target_status':'M14 direct sum M4 is excluded by the separate parity_annihilator argument; support entropy remains feasible',
            'new_exponent_established':False, 'target_restriction_constructed':False}


def full_cg_preconditioner(a,b,arrays=None):
    """Replay the known binomial/Vandermonde scaling for the full source."""
    m=a+b-1
    dimension=a*b*m
    squared_factors=[
        [Fraction(comb(a-1,i)*comb(b-1,s),m*comb(m-1,k))
         for i,k,s in product(range(a),range(m),range(b))],
        [Fraction(comb(b-1,j)*comb(a-1,p),m*comb(m-1,l))
         for j,p,l in product(range(b),range(a),range(m))],
        [Fraction(comb(b-1,q)*comb(a-1,r),m*comb(m-1,h))
         for h,q,r in product(range(m),range(b),range(a))],
    ]
    points=[]
    marginals=[[Fraction(0) for _ in range(dimension)] for _ in range(3)]
    for i,j,p,q,r,s in product(range(a),range(b),range(a),range(b),range(a),range(b)):
        point=((i*m+p+q)*b+s,(j*a+p)*m+r+s,((i+j)*b+q)*a+r)
        points.append(point)
        mass=squared_factors[0][point[0]]*squared_factors[1][point[1]]*squared_factors[2][point[2]]
        for axis in range(3):
            marginals[axis][point[axis]]+=mass
    target=Fraction(1,dimension)
    if any(value!=target for row in marginals for value in row):
        raise ArithmeticError('Full-source binomial scaling marginal identity failed')
    result={'source_lengths':[a,b],'source_mode':'full','source_leg_dimension':dimension,
            'source_support_terms':len(points),'exact_coordinate_marginal':str(target),
            'exact_marginal_equations_checked':3*dimension,'exact_verification_passed':True,
            'provenance':'Replay of the existing binomial/Vandermonde convolution scaling; no new theorem claimed',
            'new_exponent_established':False,'target_restriction_constructed':False}
    if arrays:
        import numpy as np
        arrays.parent.mkdir(parents=True,exist_ok=True)
        factors=np.sqrt(np.asarray(squared_factors,dtype=float))
        np.savez_compressed(arrays,A=factors[0],B=factors[1],C=factors[2],
                            points=np.asarray(points,dtype=np.int64),
                            log_probability_factors=np.log(np.asarray(squared_factors,dtype=float)))
        result['arrays']=str(arrays)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--discover', action='store_true')
    parser.add_argument('--p', default='2/3')
    parser.add_argument('--floor', default='1/10000000000')
    parser.add_argument('--ipfp', action='store_true')
    parser.add_argument('--full-cg', type=int,nargs=2,metavar=('A','B'))
    parser.add_argument('--verify', type=Path)
    parser.add_argument('--report', type=Path, help='Replay both endpoint certificates in this directory')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--arrays', type=Path, help='Save numerical IPFP arrays in NPZ format')
    args = parser.parse_args()
    if args.full_cg:
        result = full_cg_preconditioner(*args.full_cg,args.arrays)
    elif args.discover:
        result = discover_rational(Fraction(args.p),Fraction(args.floor))
    elif args.verify:
        result = verify_rational(json.loads(args.verify.read_text()))
    elif args.report:
        result = certificate_report(args.report)
    elif args.ipfp:
        result, masses, logs = ipfp()
        if args.arrays:
            import numpy as np
            args.arrays.parent.mkdir(parents=True,exist_ok=True)
            points = np.asarray(source_data()[0],dtype=np.int64)
            log_probability_factors = logs-np.log(len(points))/3
            diagonal_multipliers = np.exp(log_probability_factors/2)
            reconstructed = np.prod(diagonal_multipliers[np.arange(3)[:,None],points.T],axis=0)
            result['diagonal_coefficient_reconstruction_error'] = float(np.max(np.abs(reconstructed-np.sqrt(masses))))
            np.savez_compressed(args.arrays,points=points,masses=masses,logs=logs,
                                log_probability_factors=log_probability_factors,
                                diagonal_multipliers=diagonal_multipliers,coefficients=np.sqrt(masses),
                                A=diagonal_multipliers[0],B=diagonal_multipliers[1],C=diagonal_multipliers[2])
            result['arrays'] = str(args.arrays)
            result['ordering'] = 'product(range(5),repeat=6) in i,j,p,q,r,s order; retain shifted parity sum two'
            result['factor_convention'] = 'mass[x,y,z]=exp(log_probability_factors[0,x]+log_probability_factors[1,y]+log_probability_factors[2,z]); A,B,C are their half exponentials'
    else:
        parser.error('Choose --discover, --verify, --report, --ipfp, or --full-cg')
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    else:
        print(text,end='')
