"""Restricted discovery: exactly one three-point fiber may change its plane.

All other planes and all short directions remain at the given control's
constant directions. Offsets still vary. The first reused control is audited
and rejected separately before a changed plane is required. UNSAT without a
checked proof and timeouts are experimental outcomes only.
"""
import argparse
import json
from pathlib import Path

import octal_variable_planes as variable


def run(family, scalar, seconds, output, phase_report):
    if family not in range(3) or scalar not in range(2, 6):
        raise ValueError('family 0..2 and scalar 2..5 required')
    original_build = variable.build

    def restricted_build(base, native=False):
        cnf, points, membership = original_build(base, native)
        for var in cnf.inputs:
            key = cnf.pool.obj(var)
            if key[0] != 'direction':
                continue
            _, f, a, j, k = key
            if (f, a) == (family, scalar):
                continue
            value = a >= 6 and k == 2 * f
            cnf.clauses.append([var if value else -var])
        return cnf, points, membership

    variable.build = restricted_build
    original_doc = variable.__doc__
    variable.__doc__ = (__doc__ + '\nOnly variable plane: family ' + str(family)
                        + ', scalar ' + str(scalar) + '.')
    try:
        result = variable.run(0, seconds, 1000, output, phase_report,
                              'cryptominisat', True)
    finally:
        variable.build = original_build
        variable.__doc__ = original_doc
    result['only_variable_plane'] = {'family': family, 'scalar': scalar}
    output.write_text(json.dumps(result, separators=(',', ':')) + '\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--family', type=int, required=True)
    parser.add_argument('--scalar', type=int, required=True)
    parser.add_argument('--seconds', type=float, default=90)
    parser.add_argument('--phase-report', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    run(args.family, args.scalar, args.seconds, args.output, args.phase_report)
