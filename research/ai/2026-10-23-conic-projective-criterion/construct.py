"""Export complete polynomial curves on the missing projective base strata."""
import argparse
import gzip
import importlib.util
import json
from pathlib import Path

import sympy as s

PACKAGE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('projective_curve_model', PACKAGE/'model.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
RESULTS = m.ROOT/'results/conic-projective-criterion-2026-10-23'
x, t, d = m.x, m.t, m.d


def coefficients(core, side):
    degree = max(s.Poly(z, t).degree() for z in core if z)
    return [m.encode(m.core_to_map(core.applyfunc(
        lambda z: s.expand(z).coeff(t, k)), side)) for k in range(degree+1)]


def mixed_curve(stratum):
    raw = m.base(stratum)
    data = {key: (value.subs(m.c, -d**3) if isinstance(value, s.MatrixBase)
                  else s.sympify(value).subs(m.c, -d**3) if key == 'delta'
                  else value) for key, value in raw.items()}
    U0, V0, K, L, u, v, delta = [data[key] for key in
        ('U', 'V', 'K', 'L', 'u', 'v', 'delta')]
    rho = d+delta*t
    P = lambda z: x*x+z*x+z*z
    beta = 3*d*d*t+3*d*delta*t*t+delta*delta*t**3
    U = m.expand(U0+t*P(d)*K*u.T)
    V = m.expand(V0+beta*L*v.T-t*P(rho)*L*v.T)
    return {'kind': 'finite_mixed', 'stratum': stratum,
            'conic_parameter': 'c=-d**3', 'normal_class': ['1', 'd'],
            'B': coefficients(U, 'B'), 'C': coefficients(V, 'C')}


def infinity_curve(stratum):
    data = m.base(stratum, 'infinity')
    U0, V0, K, L, u, v, delta = [data[key] for key in
        ('U', 'V', 'K', 'L', 'u', 'v', 'delta')]
    U = m.expand(U0+t*x*K*u.T)
    V = m.expand(V0-t*x*L*v.T-delta*t*t*x*x*L*v.T)
    return {'kind': 'conic_infinity', 'stratum': stratum,
            'conic_parameter': '[r:s]=[0:1]', 'normal_class': ['0', '1'],
            'B': coefficients(U, 'B'), 'C': coefficients(V, 'C')}


def construct():
    return {'schema': 'conic-projective-criterion-v1',
            'claim_id': 'AI-CONIC-PROJECTIVE-CRITERION-001',
            'base': 'P1_[r:s] x P1_[a0:a1] x P1_[b0:b1] over C',
            'criterion': '(a1*r-a0*s)*(b1*r+b0*s)*(s*lambda**3+r*mu**3)=0',
            'scope': 'existence for a nonzero normal class; boundary first velocity is free',
            'kernel': 'the fixed coordinate kernel complementary to A0',
            'families': [builder(stratum) for builder in (mixed_curve, infinity_curve)
                         for stratum in m.STRATA]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    record = construct()
    path = RESULTS/'curves.json.gz'
    if args.write:
        payload = (json.dumps(record, sort_keys=True, separators=(',', ':'))+'\n').encode()
        path.write_bytes(gzip.compress(payload, mtime=0))
    else:
        assert record == json.loads(gzip.decompress(path.read_bytes()))
    print('Complete projective polynomial curves reproduced')


if __name__ == '__main__':
    main()
