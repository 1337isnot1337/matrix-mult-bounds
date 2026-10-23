"""Independent full-source check of the literal binary five-sector witness.

This checks finite maps over F2. The separate integral chart and its odd
Jacobian minor are required for the characteristic-zero existence theorem.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT = ROOT / "results/free-isotropic-flags-2026-10-21/literal-f2-witness.json"

def multiply(a, b):
    """Ordinary polynomial product, without reducing by the chart modulus."""
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result

def rank(rows):
    basis = {}
    for row in rows:
        while row:
            col = row.bit_length()-1
            if col in basis:
                row ^= basis[col]
            else:
                basis[col] = row
                break
    return len(basis)

def verify(data):
    m, a, b = 5, 7, 15
    U, Y, Z, H = (data[key] for key in ("U", "Y", "Z", "H"))
    assert len(U) == m and len(Y) == len(Z) == len(H) == m
    assert all(isinstance(row, int) and 0 <= row < (1 << a) for row in U)
    for p in range(m):
        assert len(Y[p]) == len(Z[p]) == p+1 and len(H[p]) == m
        for rows, width in ((Y[p], b), (Z[p], a+b-1), (H[p], m)):
            assert all(isinstance(row, int) and 0 <= row < (1 << width) for row in rows)
    ranks = {"shared": rank(U), "Y": rank(sum(Y, [])), "Z": rank(sum(Z, [])),
             "sector": [rank(h) for h in H]}
    assert ranks == {"shared": 5, "Y": 15, "Z": 15, "sector": [5]*5}
    counts = {"total": 0, "negative": 0, "constant": 0,
              "constant_nonzero": 0, "positive_nonzero": 0}
    for i, u in enumerate(U):
        for p, rows in enumerate(Y):
            for j, y in enumerate(rows):
                product = multiply(u, y)
                for q, forms in enumerate(Z):
                    for k, z in enumerate(forms):
                        value = (product & z).bit_count() & 1
                        degree = p+q-(m-1)
                        counts["total"] += 1
                        if degree < 0:
                            assert value == 0, ("negative", i, p, j, q, k, value)
                            counts["negative"] += 1
                        elif degree == 0:
                            expected = (H[p][i] >> (j+k)) & 1
                            assert value == expected, ("constant", i, p, j, q, k, value, expected)
                            counts["constant"] += 1
                            counts["constant_nonzero"] += value
                        elif value:
                            counts["positive_nonzero"] += 1
    assert counts["total"] == 1125
    assert counts["negative"] == counts["constant"] == 175
    return {"status": "exact full-source F2 replay passed", "source": [a, b, a+b-1],
            "target": [m, b, b], "counts": counts, "ranks": ranks,
            "coefficient_field": "F2", "improves_omega": False,
            "scope": "Literal binary witness only; characteristic-zero existence uses verify_chart.py and its written proof."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--witness", type=Path, default=DEFAULT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(verify(json.loads(args.witness.read_text())), indent=2)+"\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
