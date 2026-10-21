"""Replay saved Q(6,4) leading-M4 points using the standard library.

All coefficient and derivative controls run with Python -S. The separate
--svd option imports NumPy lazily for numerical singular-value diagnostics.
Saved floating-point points are discovery states, never exact certificates.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
RESULTS = REPO / "results/leading-m4-search-2026-10-21"
ARCHIVE = RESULTS / "search-history.json.gz"


def load_history(path: Path = ARCHIVE) -> dict:
    history = json.loads(gzip.decompress(path.read_bytes()))
    for item in history["files"]:
        digest = hashlib.sha256(item["text"].encode()).hexdigest()
        if digest != item["sha256"]:
            raise ValueError(f"Archive checksum mismatch: {item['name']}")
    return history


def terminal_points(history: dict):
    for item in history["files"]:
        if item["role"] == "terminal_point":
            yield item["name"], item["family"], json.loads(item["text"])


def target_tensor():
    """Flattened A,B,C target array; all 4,096 positions are retained."""
    target = [0] * 4096
    for i in range(4):
        for j in range(4):
            for h in range(4):
                target[(4*i+h)*256 + (4*i+j)*16 + 4*j+h] = 1
    return target


def norm(values):
    return math.sqrt(math.fsum(abs(x)**2 for x in values))


def native_pre_a(B, C):
    """The 36 source A slices as rows of length 256, with native loops."""
    if any(len(M) != 16 or any(len(row) != 36 for row in M) for M in (B, C)):
        raise ValueError("Expected target-by-source long maps of shape (16,36)")
    S = [[0] * 256 for _ in range(36)]
    for p in range(6):
        for q in range(6):
            output = S[6*p+q]
            for y in range(4):
                for v in range(4):
                    bcol = 9*y+q+v
                    ccol = 4*(p+y)+v
                    cvalues = [row[ccol] for row in C]
                    for b in range(16):
                        scale = B[b][bcol]
                        offset = 16*b
                        for c, value in enumerate(cvalues):
                            output[offset+c] += scale * value
    return S


def full_contraction(maps):
    A, B, C = maps
    if len(A) != 16 or any(len(row) != 36 for row in A):
        raise ValueError("Expected target-by-source A map of shape (16,36)")
    S = native_pre_a(B, C)
    tensor = [0] * 4096
    for a in range(16):
        offset = 256*a
        for s, scale in enumerate(A[a]):
            for bc, value in enumerate(S[s]):
                tensor[offset+bc] += scale * value
    return tensor, S


def optional_svd(pre_a):
    """Discovery diagnostic only; NumPy is not a verification dependency."""
    try:
        import numpy as np
    except ImportError as exc:
        raise RuntimeError("--svd requires an optional NumPy installation; default replay does not") from exc
    return np.linalg.svd(np.asarray(pre_a), compute_uv=False).tolist()


def replay_point(name: str, family: str, point: dict, svd: bool = False) -> dict:
    maps = [
        [[complex(r, i) for r, i in zip(rrow, irow)]
         for rrow, irow in zip(real, imag)]
        for real, imag in zip(point["maps_real"], point["maps_imag"])
    ]
    if not all(math.isfinite(z.real) and math.isfinite(z.imag)
               for M in maps for row in M for z in row):
        raise ValueError(f"Nonfinite saved map: {name}")
    tensor, pre_a = full_contraction(maps)
    residual = [a-b for a, b in zip(tensor, target_tensor())]
    coefficient_relative = norm(residual) / 8
    saved = point["diagnostics"]
    keys = ("coefficient_relative", "full_coefficient_relative_error",
            "exact_family_full_coefficient_residual")
    saved_relative = next(saved[k] for k in keys if k in saved)
    coefficient_delta = abs(coefficient_relative - saved_relative)
    if coefficient_delta > 2e-11:
        raise AssertionError((name, "coefficient replay mismatch", coefficient_delta))
    archived_singular = saved.get("preA_singular", saved.get("pre_A_singular"))
    result = {
        "name": name,
        "family": family,
        "source_terms_replayed": 576,
        "coefficient_positions_replayed": 4096,
        "target_support_positions": 64,
        "off_support_positions": 4032,
        "coefficient_relative_error": coefficient_relative,
        "coefficient_max_abs_error": max(map(abs, residual)),
        "coefficient_replay_delta": coefficient_delta,
        "map_norms": [norm(z for row in M for z in row) for M in maps],
        "archived_tail27_absolute": norm(archived_singular[27:]),
        "archived_tail27_relative": norm(archived_singular[27:]) / norm(archived_singular),
        "archived_pre_A_singular_values": archived_singular,
        "svd_recomputed": svd,
        "exact_certificate": False,
        "rank_upper_bound_certified": False,
    }
    if svd:
        singular = optional_svd(pre_a)
        tail_absolute = norm(singular[27:])
        tail_relative = tail_absolute / norm(singular)
        if "tail27_absolute" in saved:
            tail_delta = abs(tail_absolute - saved["tail27_absolute"])
        else:
            tail_delta = abs(tail_relative - saved["tail27_relative"])
        if tail_delta > 2e-9:
            raise AssertionError((name, "rank-tail replay mismatch", tail_delta))
        result.update(pre_A_singular_values=singular, tail27_absolute=tail_absolute,
                      tail27_relative=tail_relative, tail_replay_delta=tail_delta)
    return result


def positive_control_maps():
    """Embed the previously certified integer Q(5,4) -> M4 maps into Q(6,4)."""
    path = REPO / "research/ai/2026-10-20-paired-construction/q54-exact.json"
    certificate = json.loads(path.read_text())
    old_A, old_B, old_C = certificate["maps_target_by_source"]
    A, B, C = [[[0]*36 for _ in range(16)] for _ in range(3)]
    for row in range(16):
        for p in range(5):
            for q in range(5):
                A[row][6*p+q] = old_A[row][5*p+q]
        for y in range(4):
            for s in range(8):
                B[row][9*y+s] = old_B[row][8*y+s]
        C[row][:32] = old_C[row]
    return [A, B, C]


def active_penalty_control():
    """Isolate the quartic norm-cap derivative corrected in the last pilot."""
    x = list(map(float, range(1, 9)))
    direction = list(map(float, range(8, 0, -1)))
    length = norm(direction)
    direction = [z/length for z in direction]
    reg, scale = 10.0, 64.0

    def dot(u, v):
        return math.fsum(a*b for a, b in zip(u, v))

    def loss(z):
        excess = max(0.0, dot(z, z)/scale-1.0)
        return 0.5*reg*excess**2

    excess = dot(x, x)/scale-1.0
    corrected = [2.0*reg*excess*z/scale for z in x]
    historical = [reg*excess*z/scale for z in x]
    epsilon = 1e-5
    plus = [a+epsilon*b for a, b in zip(x, direction)]
    minus = [a-epsilon*b for a, b in zip(x, direction)]
    finite_difference = (loss(plus)-loss(minus))/(2*epsilon)
    return {
        "penalty_is_active": excess > 0,
        "corrected_gradient_error": abs(finite_difference-dot(corrected, direction)),
        "historical_gradient_error": abs(finite_difference-dot(historical, direction)),
    }


def verify_all(path: Path = ARCHIVE, svd: bool = False) -> dict:
    history = load_history(path)
    rows = [replay_point(*point, svd=svd) for point in terminal_points(history)]
    tensor, _ = full_contraction(positive_control_maps())
    if tensor != target_tensor():
        raise AssertionError("Integer positive control failed")
    altered = positive_control_maps()
    location = next((i, j) for i, row in enumerate(altered[0])
                    for j, value in enumerate(row) if value)
    altered[0][location[0]][location[1]] *= -1
    altered_tensor, _ = full_contraction(altered)
    perturbation_failures = sum(a != b for a, b in zip(altered_tensor, target_tensor()))
    if not perturbation_failures:
        raise AssertionError("Deliberate sign error was not detected")
    families = {}
    for row in rows:
        family = families.setdefault(row["family"], {"terminal_points": 0,
            "best_coefficient_relative_error": float("inf"),
            "smallest_archived_tail27_absolute": float("inf")})
        family["terminal_points"] += 1
        family["best_coefficient_relative_error"] = min(
            family["best_coefficient_relative_error"], row["coefficient_relative_error"])
        family["smallest_archived_tail27_absolute"] = min(
            family["smallest_archived_tail27_absolute"], row["archived_tail27_absolute"])
    return {
        "scope": "Finite floating-point search history; no exclusion and no new exponent bound",
        "coefficient_verification_dependencies": "Python standard library only",
        "svd_diagnostics_recomputed": svd,
        "archived_singular_values_are_not_default_verification": True,
        "archive_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "terminal_points_replayed": len(rows),
        "source_terms_per_point": 576,
        "coefficient_positions_per_point": 4096,
        "integer_positive_control_passed": True,
        "deliberate_sign_error_positions": perturbation_failures,
        "active_penalty_control": active_penalty_control(),
        "families": families,
        "points": rows,
        "exact_low_rank_certificate_found": False,
        "improves_omega": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=ARCHIVE)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--svd", action="store_true", help="Also recompute numerical SVD using optional NumPy")
    parser.add_argument("--extract", type=Path,
                        help="Extract the archived discovery files without running them")
    args = parser.parse_args()
    if args.extract:
        args.extract.mkdir(parents=True, exist_ok=True)
        for item in load_history(args.archive)["files"]:
            if Path(item["name"]).name != item["name"]:
                raise ValueError("Archive filename is not a basename")
            (args.extract/item["name"]).write_text(item["text"])
        return
    result = verify_all(args.archive, svd=args.svd)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "points"}, indent=2))


if __name__ == "__main__":
    main()
