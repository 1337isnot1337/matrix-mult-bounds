"""Exact finite controls for the written regular-long-leg obstruction.

The controls check the proof's matrix identities and sharp rank losses.
They do not enumerate Laurent maps or formalize its quantified theorem.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/long-leg-rank-obstruction-2026-10-23/controls.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def zero(matrix):
    return all(s.cancel(entry) == 0 for entry in matrix)


def regular(matrix, t):
    return all(s.denom(s.cancel(entry)).subs(t, 0) != 0 for entry in matrix)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "1c04903c215f396150605c0778024e856ec0b0d4",
            "Changed source baseline")
    expected = {
        "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
        "research/ai/2026-10-20-koszul/cyclic_finite_target.py",
        "research/ai/2026-10-21-cyclic-slice-determinants/unital_chart.md",
        "research/ai/2026-10-23-regular-unit-image/proof.md",
    }
    entries = record["local_dependencies"]
    require(len(entries) == len(expected) and {e["path"] for e in entries} == expected,
            "Changed predecessor inventory")
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(actual == entry["sha256"], "Changed source bytes: " + entry["path"])
    predecessor = record["concurrent_predecessor"]
    require(predecessor["pr"] == 113 and predecessor["commit"] ==
            "08ac3e983e270cf3df4e26d960ceb16415f7ef31",
            "Changed concurrent kernel-proof attribution")
    require(predecessor["claims"] == ["AI-UNIT-KERNEL-LOW-RANK-001",
                                       "AI-A4-ONE-REGULAR-LEG-002"],
            "Changed concurrent claim attribution")
    return len(entries)


def multiplication_rows(coefficients):
    """Rows span u*S_3 in homogeneous degree six, in monomial order."""
    return s.Matrix(4, 7, lambda j, h:
                    coefficients[h-j] if 0 <= h-j < 4 else 0)


def minimum_slice_controls():
    """Literal source coefficients and the fixed row-space factorization."""
    u = [1, 2, -1, 1]
    alpha, beta = 2, 1
    short = s.Matrix([[alpha**(3-j)*beta**j for j in range(4)]])
    hankel = short.T*short
    um = multiplication_rows(u)
    row_frame = s.kronecker_product(um, short, s.eye(4))
    require(um.rank() == 4 and hankel.rank() == 1 and row_frame.rank() == 16,
            "Minimum-slice row frame has wrong rank")
    records = []
    for v in ([1, 0, 0, 0], [1, -1, 2, 1], [0, 0, 0, 1]):
        vm = multiplication_rows(v).T
        column_frame = s.kronecker_product(s.eye(4), short.T, vm)
        factored = s.kronecker_product(um, hankel, vm)
        literal = s.Matrix(112, 112, lambda row, col: 0)
        rows = list(itertools.product(range(4), range(4), range(7)))
        columns = list(itertools.product(range(7), range(4), range(4)))
        for row, (j, p, ell) in enumerate(rows):
            for col, (h, q, r) in enumerate(columns):
                i, z = h-j, ell-r
                if 0 <= i < 4 and 0 <= z < 4:
                    literal[row, col] = u[i]*alpha**(6-p-q)*beta**(p+q)*v[z]
        require(literal == factored == column_frame*row_frame,
                "Literal cyclic coefficients disagree with the row-space factorization")
        require(vm.rank() == 4 and column_frame.rank() == 16,
                "A nonzero source ruling vector lost its column rank")
        records.append({"u": u, "coherent_point": [alpha, beta], "v": v,
                        "source_rank": 16, "common_row_frame_rank": 16,
                        "literal_coefficients_checked": 112*112})
    return records


def row_space_intersection_controls():
    cubics = ([1, 0, 0, 0], [0, 0, 0, 1], [1, 3, 3, 1])
    rows = [multiplication_rows(cubic) for cubic in cubics]
    records = []
    for count, expected in ((2, 1), (3, 0)):
        annihilator = s.Matrix.hstack(*[column for row in rows[:count]
                                        for column in row.nullspace()])
        dimension = 7-annihilator.rank()
        require(dimension == expected, "Cubic multiplication row intersection changed")
        records.append({"cubic_count": count, "common_sextic_space_dimension": dimension})
    q0 = s.kronecker_product(rows[0], s.Matrix([[1, 0, 0, 0]]), s.eye(4))
    q1 = s.kronecker_product(rows[0], s.Matrix([[0, 0, 0, 1]]), s.eye(4))
    require(q0.col_join(q1).rank() == 32,
            "Distinct coherent middle lines unexpectedly share a nonzero row")
    records.append({"distinct_middle_lines": 2, "common_row_space_dimension": 0})
    return records


def sextic_divisor_controls():
    x, y = s.symbols("x y")
    factors = [x+j*y for j in range(1, 7)]
    sextic = s.prod(factors)
    divisors = []
    for selected in itertools.combinations(range(6), 3):
        cubic = s.prod(factors[j] for j in selected)
        complement = s.prod(factors[j] for j in range(6) if j not in selected)
        require(s.expand(cubic*complement-sextic) == 0, "Cubic divisor identity failed")
        divisors.append(tuple(s.Poly(cubic, x, y).coeff_monomial(x**(3-j)*y**j)
                              for j in range(4)))
    require(len(set(divisors)) == 20, "Square-free sextic did not have twenty cubic divisors")
    return {"linear_factors": 6, "projective_cubic_divisors": 20,
            "integer_coefficients": [[int(z) for z in divisor] for divisor in divisors]}


def bounded_rank_space_controls():
    records = []
    for m in (2, 4, 10):
        r = m-1
        d = r*(m-r)
        form = s.zeros(2*d)
        form[:d, d:] = s.eye(d)
        form[d:, :d] = s.eye(d)
        isotropic = s.eye(2*d)[:, :d]
        require(form.rank() == 2*d and isotropic.T*form*isotropic == s.zeros(d),
                "Trace-pairing isotropic-dimension control failed")
        # All matrices supported on the first r rows attain the bound mr.
        basis = []
        for i in range(r):
            for j in range(m):
                matrix = s.zeros(m)
                matrix[i, j] = 1
                basis.append(matrix.reshape(m*m, 1))
        require(s.Matrix.hstack(*basis).rank() == m*r,
                "Sharp singular matrix-space dimension control failed")
        records.append({"matrix_size": m, "maximum_rank": r,
                        "trace_pairing_dimension": 2*d,
                        "isotropic_dimension": d, "sharp_space_dimension": m*r})
    return records


def normalized_rank_controls():
    excluded = [(rb, rc) for rb in range(1, 111) for rc in range(1, 111)
                if 224-rb-rc < 16]
    boundary = [(rb, rc) for rb in range(1, 111) for rc in range(1, 111)
                if 224-rb-rc == 16]
    require(len(excluded) == 78 and len(boundary) == 13,
            "Normalized rank-budget enumeration changed")
    require(224-109-109 == 6 and (108, 100) in boundary,
            "Incorrect minimal-defect or equality boundary")
    return {"nonzero_leading_rank_pairs_checked": 110*110,
            "excluded_by_strict_leading_pole_budget": len(excluded),
            "equality_rank_pairs": len(boundary),
            "defect_one_pair_source_budget": 6,
            "maximum_remaining_rank_sum": 208,
            "individual_rank_cap_from_corank_one_theorem": 108,
            "boundary_is_construction": False}


def residual_controls():
    """Include polar row maps whose regular right inverse vanishes at zero."""
    t = s.Symbol("t", nonzero=True)
    records = []
    for r in (3, 4):
        for k in (0, 1, 2):
            for all_positive in (False, True):
                orders = [j + int(all_positive) for j in range(r)]
                inverse_top = s.diag(*[t**order for order in orders])
                pole_top = s.diag(*[t**(-order) for order in orders])
                tail = s.Matrix(r, k, lambda i, j: (i+1)*(j+2) + int(i == j))
                b = pole_top.row_join(tail)
                d = inverse_top.col_join(s.zeros(k, r))
                kernel = (-inverse_top*tail).col_join(s.eye(k))
                coefficient = s.Matrix(k, r, lambda i, j: int(i == j))
                target = s.eye(r) + t*s.ones(r)
                y = d*target + kernel*coefficient
                require(zero(b*d-s.eye(r)), "Regular right inverse identity failed")
                require(zero(b*y-target), "Target identity failed")
                w = (y-d*(b*y)).applyfunc(s.cancel)
                require(regular(y, t) and regular(d, t) and regular(w, t),
                        "A residual specialization retained a pole")
                require(zero(b*w), "Residual does not lie in the row-map kernel")
                require(w.rank() == k and w.subs(t, 0).rank() == k,
                        "Residual exceeded or failed to reach its kernel rank")
                unit_rank = d.subs(t, 0).rank()
                require(unit_rank == int(not all_positive), "Incorrect limiting unit image")
                records.append({"target_rows": r, "row_defect": k,
                                "maximum_pole_order": max(orders),
                                "limiting_unit_image_rank": unit_rank,
                                "generic_residual_rank": k,
                                "limiting_residual_rank": k})
    return records


def rank_loss_controls():
    """Reach rho+k_B+k_C exactly for individual source matrices."""
    records = []
    for rho in (1, 2, 3):
        for kb, kc in ((0, 0), (1, 0), (0, 1), (1, 1), (2, 2)):
            r = rho+kb+kc+1
            nb, nc = r+kb, r+kc
            source = s.zeros(nb, nc)
            for j in range(rho):
                source[j, j] = 1
            for j in range(kb):
                source[r+j, rho+j] = 1
            for j in range(kc):
                source[rho+j, r+j] = 1
            c0 = s.eye(nc)[:, :r]
            d0 = s.eye(nb)[:, :r]
            target = s.zeros(r)
            for j in range(rho):
                target[j, j] = 1
            residual = source*c0-d0*target
            require(residual.rank() == kb, "Wrong residual rank budget")
            require((source*c0).rank() == rho+kb, "Wrong compressed source rank")
            require(source.rank() == rho+kb+kc, "Wrong total source rank loss")
            records.append({"target_slice_rank": rho, "row_defect": kb,
                            "column_defect": kc, "residual_rank": kb,
                            "source_rank": rho+kb+kc})
    return records


def valuation_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    for valuation in (-7, -1, 0, 3, 11):
        first = t**valuation*s.Matrix([[1, t], [t*t, 2*t]])
        row = s.Matrix([[1, t**-2], [t, 1]])
        normalized_first = (t**(-valuation)*first).applyfunc(s.cancel)
        normalized_row = t**valuation*row
        require(regular(normalized_first, t), "First-map scalar normalization failed")
        require(normalized_first.subs(t, 0) != s.zeros(2),
                "Normalized first map has zero constant coefficient")
        require(zero(normalized_row*normalized_first-row*first),
                "Scalar normalization changed the tensor product")
        records.append({"initial_valuation": valuation,
                        "normalized_valuation": 0, "product_preserved": True})
    return records


def boundary_controls():
    t = s.Symbol("t", nonzero=True)
    raw = s.Matrix([[1/t, 1], [1, t]])
    constant = raw.applyfunc(lambda entry: s.expand(entry).coeff(t, 0))
    regularized = (t*raw).applyfunc(s.cancel)
    require(raw.rank() == 1 and constant.rank() == 2,
            "Raw Laurent coefficient negative control failed")
    require(regular(regularized, t) and regularized.subs(t, 0).rank() == 1,
            "Regular matrix rank specialization failed")

    # Removing the full-row target-slice hypothesis makes a false statement.
    # The one-dimensional source is scalar multiples of I_2 (minimum rank 2).
    # A regular row map diag(1,t) gives a rank-one target with C=I_2.
    row = s.diag(1, t)
    target = row.subs(t, 0)
    require(target.rank() == 1 and s.eye(2).rank() == 2,
            "Missing-target-unit control failed")
    return {"raw_laurent_generic_rank": 1, "raw_constant_rank": 2,
            "regularized_limit_rank": 1,
            "without_full_row_target_slice": {
                "source_minimum": 2, "target_spanning_rank": 1,
                "row_defect": 0, "column_defect": 0,
                "degeneration_exists": True, "has_full_row_target_slice": False}}


@lru_cache(maxsize=1)
def report():
    rho, kb, kc, mu = 11, 2, 2, 16
    require(mu > rho+kb+kc, "Lost the A4 strict rank gap")
    matrix_units = [s.zeros(10) for _ in range(100)]
    for i in range(10):
        for j in range(10):
            matrix_units[10*i+j][i, j] = 1
    require(s.Matrix.hstack(*[x.reshape(100, 1) for x in matrix_units]).rank() == 100,
            "Matrix-unit spanning certificate failed")
    require(all(x.rank() == 1 for x in matrix_units), "A matrix unit has wrong rank")
    require(sum((matrix_units[11*i] for i in range(10)), s.zeros(10)) == s.eye(10),
            "Target unit is not the sum of diagonal matrix units")
    return {"scope": "Exact finite matrix controls for a written all-order argument.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "source_pin_count": check_sources(),
            "residuals": residual_controls(), "rank_losses": rank_loss_controls(),
            "scalar_normalization": valuation_controls(),
            "boundary_controls": boundary_controls(),
            "a4": {"source_minimum": mu, "target_spanning_rank": rho,
                   "row_defect": kb, "column_defect": kc,
                   "rank_floor_margin": mu-rho-kb-kc,
                   "spanning_matrix_units": 100, "target_unit_rank": 110,
                   "unit_image_threshold_required": False,
                   "one_missing_long_column_margin": 0,
                   "both_singular_long_limits_excluded": False},
            "minimum_slice_factorizations": minimum_slice_controls(),
            "row_space_intersections": row_space_intersection_controls(),
            "sextic_divisors": sextic_divisor_controls(),
            "bounded_rank_spaces": bounded_rank_space_controls(),
            "normalized_leading_ranks": normalized_rank_controls(),
            "corank_one": {"long_limit_rank": 109, "source_column_defect": 3,
                           "rank_one_source_lift_rank": 16,
                           "compressed_rank_one_lift_rank": 13,
                           "fixed_column_annihilator_dimension": 3,
                           "maximum_first_map_rank": 4,
                           "minimum_first_kernel_dimension": 96,
                           "maximum_singular_matrix_space_dimension": 90,
                           "minimum_unit_image_rank": 13,
                           "maximum_kernel_residual_rank": 2,
                           "excludes_leading_rank_108": False}}


def verify(record):
    check_sources()
    require(record == report(), "Changed finite controls or theorem scope")
    return {"residual_families": len(record["residuals"]),
            "sharp_rank_loss_controls": len(record["rank_losses"]),
            "scalar_valuation_controls": len(record["scalar_normalization"]),
            "spanning_matrix_units": record["a4"]["spanning_matrix_units"],
            "minimum_slice_factorizations": len(record["minimum_slice_factorizations"]),
            "row_space_intersections": len(record["row_space_intersections"]),
            "sextic_cubic_divisors": record["sextic_divisors"]["projective_cubic_divisors"],
            "bounded_rank_space_controls": len(record["bounded_rank_spaces"]),
            "normalized_rank_pairs": 110*110,
            "improves_omega": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the frozen controls")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))
