"""Exploratory alternating least squares; never a degeneration certificate.

Optional dependency: NumPy. Each run prints one JSON record. The archived
probe summary records the actual seeds, cycles, coefficient fields and version.
"""
import argparse
import json
import time

import numpy as np


def target(m):
    monomials = [(i, degree - i) for degree in range(m) for i in range(degree + 1)]
    size = len(monomials)
    tensor = np.zeros((m, size, size))
    for y, (a, b) in enumerate(monomials):
        for z, (c, d) in enumerate(monomials):
            if a + b + c + d == m - 1:
                tensor[a + c, y, z] = 1
    return tensor


def solve(m, seed, cycles=3000, complex_coefficients=False):
    rng = np.random.default_rng(seed)
    tensor = target(m)
    size = tensor.shape[1]
    output = size + m - 1
    a = rng.normal(size=(m, m))
    b = rng.normal(size=(size, size))
    c = rng.normal(size=(size, output))
    if complex_coefficients:
        a = a + 1j * rng.normal(size=a.shape)
        b = b + 1j * rng.normal(size=b.shape)
        c = c + 1j * rng.normal(size=c.shape)
    records = []
    started = time.monotonic()
    for step in range(cycles):
        design = np.stack([b @ c[:, i:i + size].T for i in range(m)])
        a = np.linalg.lstsq(design.reshape(m, -1).T,
                            tensor.reshape(m, -1).T, rcond=1e-13)[0].T
        design = np.stack([a @ c[:, j:j + m].T for j in range(size)])
        b = np.linalg.lstsq(design.reshape(size, -1).T,
                            tensor.transpose(1, 0, 2).reshape(size, -1).T, rcond=1e-13)[0].T
        design = np.zeros((output, m, size), dtype=a.dtype)
        for i in range(m):
            design[i:i + size] += np.einsum('x,yj->jxy', a[:, i], b)
        c = np.linalg.lstsq(design.reshape(output, -1).T,
                            tensor.transpose(2, 0, 1).reshape(size, -1).T, rcond=1e-13)[0].T
        norms = np.array([np.linalg.norm(factor) for factor in (a, b, c)])
        scale = np.prod(norms) ** (1 / 3)
        a *= scale / norms[0]
        b *= scale / norms[1]
        c *= scale / norms[2]
        if step in (0, 9, 99, 999, cycles - 1):
            prediction = sum(np.einsum('x,yj,zj->xyz', a[:, i], b, c[:, i:i + size])
                             for i in range(m))
            records.append({"cycle": step + 1,
                            "relative_residual": float(np.linalg.norm(prediction - tensor)
                                                       / np.linalg.norm(tensor)),
                            "factor_norm": float(scale),
                            "condition_A": float(np.linalg.cond(a)),
                            "condition_B": float(np.linalg.cond(b))})
    return {"m": m, "seed": seed, "complex_coefficients": complex_coefficients,
            "records": records, "seconds": time.monotonic() - started}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--cycles", type=int, default=3000)
    parser.add_argument("--complex", action="store_true")
    args = parser.parse_args()
    print(json.dumps(solve(args.m, args.seed, args.cycles, args.complex)))
