"""Local extension directions around the exact full-source M9 control.

The output is a numerical discovery diagnostic, not an exact larger tensor
restriction.  It computes the whitened second-order operator for adding
one inner matrix-multiplication channel while the third core map is fixed.
"""

import json
from pathlib import Path

import numpy as np
from scipy.linalg import svd

from parity_structure import mixed_m9_maps, source_tensor


def main():
    aa, bb, cc = mixed_m9_maps()
    ff = np.zeros((225, 225, 81), dtype=np.float64)
    columns = [[(int(row), int(cc[row, col]))
                for row in np.flatnonzero(cc[:, col])]
               for col in range(225)]
    for (a, b, c), coefficient in source_tensor().items():
        for z, value in columns[c]:
            ff[a, b, z] += coefficient*value
    da = np.einsum("abz,yb->ayz", ff, bb, optimize=True).reshape(225, -1)
    db = np.einsum("abz,xa->bxz", ff, aa, optimize=True).reshape(225, -1)
    ga, gb = da @ da.T, db @ db.T
    eva, eua = np.linalg.eigh(ga)
    evb, eub = np.linalg.eigh(gb)
    assert min(eva[0], evb[0]) > 1e-8
    wa = (eua / np.sqrt(eva)) @ eua.T
    wb = (eub / np.sqrt(evb)) @ eub.T

    # z=9*k+i, with source a,b still ordered by the maintained source format.
    kk = ff.reshape(225, 225, 9, 9).transpose(3, 0, 2, 1).reshape(2025, 2025)

    white = np.einsum("ac,ickd,db->iakb", wa,
                      kk.reshape(9, 225, 9, 225), wb, optimize=True)
    left, values, right = svd(white.reshape(2025, 2025),
                              full_matrices=False, check_finite=False)
    direction_a = left[:, 0].reshape(9, 225) @ wa
    direction_b = right[0].reshape(9, 225) @ wb
    norm_a = np.einsum("ia,ab,ib->", direction_a, ga, direction_a)
    norm_b = np.einsum("ka,ab,kb->", direction_b, gb, direction_b)
    cross = direction_a.reshape(-1) @ kk @ direction_b.reshape(-1)
    report = {
        "status": "Numerical local discovery diagnostic; no larger restriction",
        "source": "full A(5,5)",
        "core": "exact M9 control from parity_structure.py",
        "partial_contraction_ranks": [225, 225],
        "gram_eigenvalue_ranges": [[float(eva[0]), float(eva[-1])],
                                   [float(evb[0]), float(evb[-1])]],
        "largest_whitened_singular_values": values[:12].tolist(),
        "direction_norms": [float(norm_a), float(norm_b)],
        "direction_cross_term": float(cross),
        "hessian_quadratic_form": float(norm_a+norm_b-2*cross),
        "negative_curvature_found": bool(values[0] > 1+1e-8),
        "interpretation": "A singular value above one gives second-order descent when adding one inner channel",
    }
    destination = Path(__file__).with_name("parity_structure_curvature.json")
    destination.write_text(json.dumps(report, indent=2)+"\n")
    np.savez_compressed(Path(__file__).with_name("parity_structure_curvature.npz"),
                        A_off=direction_a, B_off=direction_b,
                        singular_values=values)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
