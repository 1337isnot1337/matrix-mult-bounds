"""Exact tangent identities; the five modular controls are not a census."""
import itertools
import json

import sympy as sp



def tangent_forms():
    u, v, w = sp.symbols('u v w')
    x, p1, p2, q1, q2, a, b, c, e = sp.symbols('x p1 p2 q1 q2 a b c e')
    B = sp.Matrix([[u, v], [v, w]])
    mu, d = u+w, B.det()
    Q = sp.diag(mu, 1, 1)
    Q[1:3, 1:3] = B
    F = sp.Matrix([[x, p1, p2], [q1, a, b], [q2, c, e]])
    C = F[1:3, 1:3]
    p, q = sp.Matrix([p1, p2]), sp.Matrix([q1, q2])
    qc = 3*sp.trace(B*C)**2/mu-sp.trace(C.T*B*C)-2*sp.trace(B*C*C)
    q4 = ((q.T*B*q)[0]-mu*(p.T*p)[0]
          +2*(p.T*(mu*sp.eye(2)-B)*q)[0]
          +2*((mu*p+B*q).T*B*(mu*p+B*q))[0]/d)
    return dict(B=B, mu=mu, d=d, Q=Q, F=F, C=C, p=p, q=q, qc=qc, q4=q4,
                u=u, v=v, w=w, x=x)


def require_zero(expression, label):
    if sp.cancel(expression) != 0:
        raise ArithmeticError(label)


def determinant_coefficient(matrices, degree):
    """Use column multilinearity, independently of the Schur-complement form."""
    return sp.expand(sum(
        sp.Matrix.hstack(*[matrices[order][:, j]
                          for j, order in enumerate(orders)]).det()
        for orders in itertools.product(range(len(matrices)), repeat=3)
        if sum(orders) == degree))


def symbolic_checks():
    t = tangent_forms()
    B, mu, d, Q, F, C = [t[k] for k in ('B', 'mu', 'd', 'Q', 'F', 'C')]
    p, q, qc, q4, x = [t[k] for k in ('p', 'q', 'qc', 'q4', 'x')]
    u, v, w = [t[k] for k in ('u', 'v', 'w')]
    Q1 = -F.T*Q-Q*F
    Q2 = (F.T**2)*Q+F.T*Q*F+Q*(F**2)
    ss = [2*A-sp.trace(A)*sp.eye(3) for A in (Q, Q1, Q2)]
    require_zero(determinant_coefficient(ss, 1)-8*d*(sp.trace(B*C)-mu*x),
                 'tangent differential')
    require_zero(determinant_coefficient(ss, 2).subs(x, sp.trace(B*C)/mu)
                 -4*d*(qc+q4), 'tangent quadratic coefficient')
    r = sp.Matrix(sp.symbols('r1 r2'))
    P = -mu*sp.eye(2)+2*mu**2*B/d
    expected = (r.T*P*r)[0]-2*(r.T*B*q)[0]-(q.T*B.adjugate()*q)[0]
    require_zero(q4.subs(dict(zip(p, r-q)))-expected, 'four-block substitution')
    K = (3*mu**2-d)*B-2*mu*d*sp.eye(2)
    for entry in P+B*B.adjugate().inv()*B-K/d:
        require_zero(entry, 'four-block Schur complement')
    require_zero(K.det()-d*(d*d+3*mu**4), 'Schur numerator determinant')
    lam = sp.Symbol('lam')
    require_zero(qc.subs({C[0, 0]: C[0, 0]+lam, C[1, 1]: C[1, 1]+lam})-qc,
                 'scalar C radical')
    y, z, h = sp.symbols('y z h')
    tf = {C[0, 0]: y, C[0, 1]: z, C[1, 0]: h, C[1, 1]: -y}
    T = sp.hessian(sp.expand((mu*qc).subs(tf)), (y, z, h))/2
    displayed = sp.Matrix([
        [-12*u*w, 4*u*v-2*v*w, 2*u*v-4*v*w],
        [4*u*v-2*v*w, -u*u-u*w+3*v*v, -u*u-2*u*w+3*v*v-w*w],
        [2*u*v-4*v*w, -u*u-2*u*w+3*v*v-w*w, -u*w+3*v*v-w*w]])
    for entry in T-displayed:
        require_zero(entry, 'displayed tracefree matrix')
    require_zero(T.det()-12*mu**2*d*(mu**2-d), 'tracefree determinant')
    require_zero(qc.subs({C[0, 0]: 0, C[0, 1]: 1, C[1, 0]: -1, C[1, 1]: 0})-mu,
                 'nonzero skew value')
    return t, T, {
        'tangent_linear_coefficient': '8*d*(tr(B*C)-mu*x)',
        'tangent_quadratic_coefficient': '4*d*(qC+q4)',
        'four_block_substitution_and_Schur_complement': True,
        'Schur_numerator_determinant': 'd*(d^2+3*mu^4)',
        'scalar_C_radical': True,
        'displayed_tracefree_matrix': True,
        'scaled_C_block_determinant': '12*mu^2*d*(mu^2-d)',
        'C_skew_value': 'mu',
        'coefficient_ring': 'Z[1/(2*mu*d)]',
    }


def rank_mod(matrix, prime):
    if prime == 2 or not sp.isprime(prime):
        raise ValueError('an odd prime is required')
    if any(not sp.sympify(entry).is_Integer for entry in matrix):
        raise ValueError('clear symbolic denominators before reduction')
    a = [[int(t) % prime for t in row] for row in matrix.tolist()]
    rank = 0
    for col in range(matrix.cols):
        pivot = next((j for j in range(rank, matrix.rows) if a[j][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, prime)
        a[rank] = [(t*inverse) % prime for t in a[rank]]
        for row in range(matrix.rows):
            if row != rank:
                factor = a[row][col]
                a[row] = [(a[row][j]-factor*a[rank][j]) % prime
                          for j in range(matrix.cols)]
        rank += 1
    return rank


def finite_control(t, T, prime, values):
    sub = dict(zip((t['u'], t['v'], t['w']), values))
    if not int(t['mu'].subs(sub)) % prime or not int(t['d'].subs(sub)) % prime:
        raise ValueError('mu and d must both be nonzero in the field')
    variables = tuple(t['p'])+tuple(t['q'])
    four = sp.hessian(sp.expand(t['d']*t['q4']), variables)/2
    r4, rc = rank_mod(four.subs(sub), prime), rank_mod(T.subs(sub), prime)
    if r4+rc < 5:
        raise ArithmeticError('tangent rank below five')
    return {'prime': prime, 'B': [[values[0], values[1]], [values[1], values[2]]],
            'four_block_rank': r4, 'C_block_rank': rc, 'tangent_rank': r4+rc}


def report():
    t, T, symbolic = symbolic_checks()
    controls = [finite_control(t, T, p, b) for p, b in
                [(3, (1, 0, 1)), (5, (1, 0, 2)), (5, (1, 1, 0)),
                 (7, (1, 0, 1)), (13, (1, 0, 2))]]
    return {'scope': 'Exact tangent identities and five inherited finite controls',
            'symbolic': symbolic, 'odd_prime_controls': controls,
            'finite_control_count': len(controls),
            'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
