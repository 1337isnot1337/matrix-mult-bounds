"""Sixteen exact, disjoint cases classify every projective cancellation chart."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('balanced_affine_dependency', HERE/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

# Each list gives rows and columns of an identically unit triangular minor.
# The cases are disjoint: the first nonzero coefficient of g is normalized
# to one; each residual linear form either has constant coefficient one or
# is its other monomial. No inverse of a variable coefficient is used.
MINORS = {
    (0,0): ([1,2,27,25,28], [0,1,2,3,5]),
    (0,1): ([6,8,28,26,29], [0,1,2,3,5]),
    (0,2): ([8,10,39,37,40], [0,1,2,3,5]),
    (0,3): ([9,15,40,38,41], [0,1,2,3,5]),
    (1,0): ([1,6,25,33,34], [0,1,3,4,5]),
    (1,1): ([6,9,26,43,34,35], [0,1,3,2,4,5]),
    (1,2): ([8,15,37,45,46], [0,1,3,4,5]),
    (1,3): ([9,16,38,46,47], [0,1,3,4,5]),
    (2,0): ([2,6,26,27,33,40], [0,1,2,3,4,5]),
    (2,1): ([8,9,54,28,34,41], [0,1,2,3,4,5]),
    (2,2): ([10,15,29,39,45,52], [0,1,2,3,4,5]),
    (2,3): ([15,16,35,40,46,53], [0,1,2,3,4,5]),
    (3,0): ([25,26,28,34,40], [0,1,3,4,5]),
    (3,1): ([26,43,29,35,41], [0,1,2,4,5]),
    (3,2): ([37,29,40,46,52], [0,1,3,4,5]),
    (3,3): ([38,35,41,47,53], [0,1,3,4,5]),
}


def generators(g_case, line_case):
    x,y,a,b,c,d,e = v.X,v.Y,v.A,v.B,v.C,v.D,v.E
    gs = [1+c*x+d*y+e*x*y, x+d*y+e*x*y, y+e*x*y, x*y]
    lines = [(1+a*x,1+b*y), (x,1+b*y), (1+a*x,y), (x,y)]
    g = gs[g_case]
    lx,ly = lines[line_case]
    hs = [h for j,h in enumerate(v.H_MONOMIALS) if j!=g_case]
    _,_,matrices = v.syzygies(g,lx,ly,hs)
    matrix = sp.Matrix.hstack(*(v.flat(m) for m in matrices))
    return g,lx,ly,matrix


def ideal_identities(residual):
    """Export two row identities for the reverse inclusion of ideals."""
    c,d,e,a,b = v.C,v.D,v.E,v.A,v.B
    f1,f2 = c+d,d**2+e
    first = next((i,sign) for i,value in enumerate(residual)
                 for sign in [1,-1] if sp.expand(value-sign*f1)==0)
    gb = sp.groebner([f1,f2],c,d,e,a,b)
    if any(gb.reduce(sp.expand(value))[1] for value in residual):
        raise ArithmeticError('a projective residual is outside the conic ideal')
    for i,value in enumerate(residual):
        for sign in [1,-1]:
            quotient,remainder = sp.reduced(sp.expand(value-sign*f2),[f1],c,d,e,a,b)
            if remainder == 0:
                return {'first_row':first[0], 'first_sign':first[1],
                        'second_row':i, 'second_sign':sign,
                        'first_generator_coefficient':str(sp.expand(quotient[0]))}
    raise ArithmeticError('reverse conic ideal identity missing')


@lru_cache(None)
def certificate():
    data = v.core_data()
    records = []
    for g_case in range(4):
        for line_case in range(4):
            g,lx,ly,syzygies = generators(g_case,line_case)
            system = (data['annihilator']*sp.diag(syzygies,syzygies)).applyfunc(sp.expand)
            rows,columns = MINORS[g_case,line_case]
            minor = system.extract(rows,columns)
            determinant = sp.expand(minor.det())
            if determinant not in [1,-1]:
                raise ArithmeticError('projective minor is not a constant unit')
            record = {'g_case':g_case, 'line_case':line_case,
                      'g':str(g), 'lx':str(lx), 'ly':str(ly),
                      'syzygies':v.encode(syzygies), 'system':v.encode(system),
                      'unit_minor_rows':rows, 'unit_minor_columns':columns,
                      'unit_minor_determinant':int(determinant)}
            if len(columns)==6:
                record.update(status='empty', reason='six by six unit minor',
                              pair_kernel_dimension=0)
                records.append(record)
                continue
            free = next(j for j in range(6) if j not in columns)
            direction = sp.zeros(6,1)
            direction[free] = 1
            solution = -minor.inv()*system[rows,free]
            for j,value in zip(columns,solution):
                direction[j] = sp.expand(value)
            residual = (system*direction).applyfunc(sp.expand)
            record.update(free_coordinate=free, kernel_direction=v.encode(direction),
                          residual=v.encode(residual))
            if g_case==1:
                unit_rows = next((i,j,sign,int(value))
                    for i in range(60) for j in range(i+1,60)
                    for sign in [1,-1]
                    for value in [sp.expand(residual[i]+sign*residual[j])]
                    if value in [1,-1])
                record.update(status='empty', reason='unit residual',
                              unit_residual_rows=list(unit_rows[:2]),
                              unit_residual_second_coefficient=unit_rows[2],
                              unit_residual_constant=unit_rows[3],
                              pair_kernel_dimension=0)
            else:
                if g_case==0:
                    record['reverse_ideal_identities'] = ideal_identities(residual)
                    record['residual_ideal'] = ['c + d','d**2 + e']
                    substitution = {v.D:-v.C, v.E:-v.C**2}
                elif g_case==3:
                    if residual != sp.zeros(60,1):
                        raise ArithmeticError('last coefficient chart is not identically incident')
                    record['residual_ideal'] = []
                    substitution = {}
                else:
                    raise ArithmeticError('unexpected projective case')
                image = (sp.diag(syzygies,syzygies)*direction).subs(substitution)
                pair = data['pair']
                pivots = list(pair.T.to_DM().rref()[1])
                normal = (pair[pivots,:].inv()*image[pivots,:]).applyfunc(sp.expand)
                if any(sp.expand(value) for value in pair*normal-image):
                    raise ArithmeticError('projective family is outside the actual normal space')
                full = sp.zeros(24,2)
                for i,j,value in zip(data['first'],data['second'],normal):
                    full[i,0] = value
                    full[j,1] = value
                record.update(status='incident exactly on residual ideal',
                              pair_kernel_dimension=1, nonplane_normal_dimension=2,
                              normal_family=v.encode(full))
            records.append(record)
    return {'base_main':'00d5133',
            'scope':'All nonzero projective g, lx and ly, partitioned into sixteen disjoint cases',
            'g_coefficient_order':['x0*y0','x1*y0','x0*y1','x1*y1'],
            'global_shared_factor_equations':['g10 + g01','g00*g11 + g10**2'],
            'global_shared_factor_parameterization':'(r*x0+s*x1)*(r*y0-s*y1), [r:s] in P1',
            'all_incident_nonplane_fibers_dimension':2,
            'all_nonzero_incident_core_first_ranks':2,
            'all_later_tensor_coefficients_verified':False,
            'cases':records}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(certificate(),indent=2)+'\n')
    print('sixteen projective cases written',flush=True)
