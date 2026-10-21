"""Optional numerical leading-rank and diagonal-gauge diagnostics for M1 pilots."""
import argparse
from itertools import product
import json
from pathlib import Path
import numpy as np

from q64_m1_leading_exact import powers
from q64_torus_gauge import normalize


def diagnose(path):
    point = json.loads(Path(path).read_text())
    maps = [np.array(r)+1j*np.array(i) for r, i in zip(point['maps_real'], point['maps_imag'])]
    source = np.zeros((36, 36, 36))
    target = np.zeros((25, 20, 20))
    for p, q, y, v in product(range(6), range(6), range(4), range(4)):
        source[6*p+q, 9*y+q+v, 4*(p+y)+v] = 1
    for i, j, k in product(range(5), range(4), range(5)):
        target[5*i+k, 4*i+j, 5*j+k] = 1
    weights = [np.array(w) for w in powers()]
    degree = weights[0][:, None, None]+weights[1][None, :, None]+weights[2][None, None, :]

    def metrics(mm):
        actual = np.einsum('is,jt,ku,stu->ijk', *mm, source, optimize=True)
        error = actual-target
        h0 = np.einsum('bs,ct,ast->abc', mm[1][:4], mm[2][[0, 5, 10, 15]], source,
                       optimize=True).reshape(36, 16)
        singular = np.linalg.svd(h0, compute_uv=False)
        derivative = 2*sum(float(np.dot(w, np.sum(np.abs(m)**2, axis=1)))
                           for w, m in zip(weights, mm))
        denominator = 2*sum(float(np.dot(np.abs(w), np.sum(np.abs(m)**2, axis=1)))
                            for w, m in zip(weights, mm))
        # Tensor rows (i_A,k_A),(i_B,j_B),(j_C,k_C) become operator
        # rows (i_A,j_B,k_C), columns (i_B,j_C,k_A).
        operator_error = error.reshape(5, 5, 5, 4, 4, 5).transpose(0, 3, 5, 2, 4, 1).reshape(100, 100)
        positive = np.where(degree > 0, actual, 0)
        positive_operator = positive.reshape(5, 5, 5, 4, 4, 5).transpose(0, 3, 5, 2, 4, 1).reshape(100, 100)
        return {'relative_required_coefficient_error': float(np.linalg.norm(error[degree <= 0])/10),
                'negative_coefficient_norm': float(np.linalg.norm(actual[degree < 0])),
                'constant_coefficient_error_norm': float(np.linalg.norm(error[degree == 0])),
                'positive_coefficient_norm': float(np.linalg.norm(positive)),
                'map_norms': [float(np.linalg.norm(m)) for m in mm],
                'H0_singular_values': singular.tolist(),
                'H0_tail_after_12': float(np.linalg.norm(singular[12:])),
                'non_old_A_times_H0_norm': float(np.linalg.norm(mm[0][1:]@h0)),
                'grading_norm_derivative': derivative,
                'relative_grading_norm_derivative': derivative/denominator,
                'operator_error_cube_norm': float(np.linalg.norm(operator_error@operator_error@operator_error)),
                'positive_part_cube_norm': float(np.linalg.norm(positive_operator@positive_operator@positive_operator))}

    normal, info = normalize(maps)
    return {'artifact': Path(path).name, 'raw': metrics(maps),
            'minimum_norm_physical_diagonal_representative': metrics(normal),
            'normalizer_relative_stationarity': info['relative_stationarity'],
            'necessary_H0_rank_upper_bound_in_this_chart': 12,
            'necessary_operator_error_cube_zero_in_this_chart': True,
            'singular_values_are_numerical_diagnostics_only': True,
            'cube_norm_is_not_a_distance_to_nilpotent_tensors': True,
            'exact_coefficient_certificate': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoints', type=Path, nargs='+')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = {'diagnostics': [diagnose(path) for path in args.checkpoints]}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
