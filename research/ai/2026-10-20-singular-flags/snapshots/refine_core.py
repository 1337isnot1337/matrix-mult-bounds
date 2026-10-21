"""Exploratory ALS for a true one-parameter mixed-target degeneration.

This is discovery-only floating computation. A small residual is not a
coefficient certificate and is never accepted as a theorem by this program.
"""
from __future__ import annotations

import argparse
from itertools import permutations
import json
import os
from pathlib import Path

import numpy as np


def target_and_weights(m, order, internal_slope=1):
    D = m - 1
    points = [(a, degree - a) for degree in range(m) for a in range(degree + 1)]
    n = len(points)
    target = np.zeros((m, n, n))
    for y, (a, b) in enumerate(points):
        for z, (c, d) in enumerate(points):
            if a + b + c + d == D:
                target[a + c, y, z] = 1
    eta = [(2*D + 1) * value for value in order]
    x = [internal_slope * p for p in range(m)]
    y = [-internal_slope*a + eta[a+b] for a, b in points]
    z = [-internal_slope*c - eta[D-c-d] for c, d in points]
    total = np.array(x)[:, None, None] + np.array(y)[None, :, None] + np.array(z)[None, None, :]
    if np.any(target[total != 0]):
        raise ArithmeticError("proposed target is not weight zero")
    return target, total <= 0, {"x": x, "y": y, "z": z}


def transform(A, B, C):
    m, length = A.shape[1], B.shape[1]
    result = np.zeros((A.shape[0], B.shape[0], C.shape[0]))
    for p in range(m):
        result += A[:, p, None, None] * (B @ C[:, p:p+length].T)[None, :, :]
    return result


def least_squares(design, target, ridge):
    if ridge:
        design = np.vstack([design, np.sqrt(ridge) * np.eye(design.shape[1])])
        target = np.r_[target, np.zeros(design.shape[1])]
    return np.linalg.lstsq(design, target, rcond=1e-12)[0]


def fit(m, length, order, iterations, seed, slope=1, ridge=1e-12, start=None):
    target, mask, weights = target_and_weights(m, order, slope)
    n = target.shape[1]
    rng = np.random.default_rng(seed)
    A = np.eye(m) + .3 * rng.normal(size=(m, m))
    B = np.eye(n, length) + .3 * rng.normal(size=(n, length))
    C = rng.normal(size=(n, length + m - 1)) / np.sqrt(length)
    if start is not None:
        A, B, C = (np.array(start[key], dtype=float) for key in ('A', 'B', 'C'))
    denominator = np.linalg.norm(target[mask])
    best = None
    best_loss = float("inf")
    trajectory = []
    for iteration in range(iterations):
        # Update each first-leg row independently.
        designs = np.stack([B @ C[:, p:p+length].T for p in range(m)])
        for a in range(m):
            A[a] = least_squares(designs[:, mask[a]].T, target[a][mask[a]], ridge)
        # Update each second-leg row independently.
        designs = np.stack([sum(A[:, p, None] * C[:, p+j][None, :]
                               for p in range(m)) for j in range(length)])
        for b in range(n):
            selected = mask[:, b, :]
            B[b] = least_squares(designs[:, selected].T, target[:, b, :][selected], ridge)
        # Update each output row independently.
        designs = np.zeros((length + m - 1, m, n))
        for p in range(m):
            for j in range(length):
                designs[p+j] += A[:, p, None] * B[:, j][None, :]
        for c in range(n):
            selected = mask[:, :, c]
            C[c] = least_squares(designs[:, selected].T, target[:, :, c][selected], ridge)
        # Scalar gauges preserve the transformed tensor.
        for matrix in (A, B):
            scale = np.linalg.norm(matrix) / np.sqrt(matrix.shape[0])
            if scale:
                matrix /= scale
                C *= scale
        image = transform(A, B, C)
        loss = float(np.linalg.norm((image-target)[mask]) / denominator)
        if iteration % 100 == 0:
            trajectory.append({'iteration': iteration+1, 'relative_residual': loss,
                               'A_min_singular_value': float(np.linalg.svd(A, compute_uv=False)[-1]),
                               'B_min_singular_value': float(np.linalg.svd(B, compute_uv=False)[-1]),
                               'max_coefficient': float(max(np.max(np.abs(M)) for M in (A,B,C)))})
            print(trajectory[-1], flush=True)
        if loss < best_loss:
            best_loss = loss
            best = {"relative_residual": loss, "iteration": iteration + 1,
                    "A": A.tolist(), "B": B.tolist(), "C": C.tolist(),
                    "A_singular_values": np.linalg.svd(A, compute_uv=False).tolist(),
                    "B_singular_values": np.linalg.svd(B, compute_uv=False).tolist(),
                    "C_singular_values": np.linalg.svd(C, compute_uv=False).tolist(),
                    "max_abs_coefficient": float(max(np.max(np.abs(M)) for M in (A, B, C)))}
        if loss < 1e-11:
            break
    return {"m": m, "B": length, "order": list(order), "internal_slope": slope,
            "seed": seed, "iterations_requested": iterations,
            "ridge": ridge, "trajectory": trajectory,
            "weights": weights, "best": best,
            "certified_degeneration": False,
            "scope": "Floating ALS discovery only; exact rational/algebraic coefficient replay still required."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m", type=int, default=4)
    parser.add_argument("--B", type=int)
    parser.add_argument("--iterations", type=int, default=150)
    parser.add_argument("--patterns", type=int, default=24)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    seed = args.seed if args.seed is not None else int.from_bytes(os.urandom(8), "big")
    length = args.B if args.B is not None else args.m * (args.m + 1) // 2
    print("seed", seed, flush=True)
    reports = []
    for index, order in enumerate(permutations(range(args.m))):
        if index >= args.patterns:
            break
        report = fit(args.m, length, order, args.iterations, seed + index)
        reports.append(report)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps({"seed": seed, "seed_origin": "provided" if args.seed is not None else "os.urandom(8)",
                                          "numpy_version": np.__version__, "completed_patterns": len(reports),
                                          "reports": reports}, indent=2) + "\n")
        print("pattern", index + 1, order, "residual", report["best"]["relative_residual"], flush=True)
