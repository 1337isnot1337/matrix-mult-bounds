"""Exact finite controls for source_capacity.md; no numerical rank decisions."""

from fractions import Fraction
import json


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    pivot = 0
    for col in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        d = a[pivot][col]
        a[pivot] = [x / d for x in a[pivot]]
        for i in range(pivot + 1, len(a)):
            d = a[i][col]
            if d:
                a[i] = [x - d * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def coordinate_subspace(l, h, k):
    if not 0 <= k <= l * h:
        raise ValueError("Invalid subspace dimension")
    forms = []
    for cell in range(k):
        a = [[Fraction(0) for _ in range(h)] for _ in range(l)]
        a[cell // h][cell % h] = Fraction(1)
        forms.append(a)
    return forms


def mix_subspace(forms):
    """Invertible rational row and basis operations; no floating point."""
    if not forms:
        return []
    l, h = len(forms[0]), len(forms[0][0])
    moved = []
    for form in forms:
        moved.append([
            [sum(Fraction(i + 1, j + 1) * form[j][a]
                 for j in range(i + 1)) for a in range(h)]
            for i in range(l)
        ])
    return [
        [[sum(Fraction(t + 1) * moved[t][i][a] for t in range(s + 1))
          for a in range(h)] for i in range(l)]
        for s in range(len(moved))
    ]


def restricted_flattening(l, h, r, forms, omit=None):
    """Contract all native M(l,h,r) coefficients, optionally omitting one."""
    result = [[Fraction(0) for _ in range(len(forms) * h * r)]
              for _ in range(l * r)]
    for i in range(l):
        for a in range(h):
            for j in range(r):
                if omit == (i, a, j):
                    continue
                for s, form in enumerate(forms):
                    result[i * r + j][s * h * r + a * r + j] += form[i][a]
    return result


def check_case(l, h, r, forms, label):
    k = len(forms)
    dimension = rank([[entry for row in form for entry in row] for form in forms])
    if dimension != k:
        raise ValueError("The supplied matrices are not an independent subspace basis")
    columns = [[forms[s][i][a] for s in range(k) for a in range(h)]
               for i in range(l)]
    column_rank = rank(columns)
    tensor_rank = rank(restricted_flattening(l, h, r, forms))
    lower_bound = r * ((k + h - 1) // h)
    if tensor_rank != r * column_rank or tensor_rank < lower_bound:
        raise AssertionError("The restricted matrix tensor failed the support identity")
    return {"label": label, "l": l, "h": h, "r": r,
            "subspace_dimension": k, "joint_column_rank": column_rank,
            "restricted_a_rank": tensor_rank, "ceiling_lower_bound": lower_bound,
            "coefficient_positions": l * r * k * h * r}


def report():
    cases = []
    for l, h, r, k in [(2, 3, 2, 0), (3, 2, 4, 1), (3, 2, 4, 5),
                        (4, 3, 2, 7), (2, 2, 3, 4)]:
        forms = coordinate_subspace(l, h, k)
        cases.append(check_case(l, h, r, forms, "coordinate"))
        if k:
            cases.append(check_case(l, h, r, mix_subspace(forms), "rational-mixed"))
    spread = [
        [[1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]],
    ]
    cases.append(check_case(4, 3, 4, spread, "strict-ceiling"))
    unit = coordinate_subspace(1, 1, 1)
    bad = rank(restricted_flattening(1, 1, 2, unit, omit=(0, 0, 0)))
    if bad == 2:
        raise AssertionError("The deliberate coefficient deletion was not detected")
    return {
        "status": "passed", "arithmetic": "exact rational",
        "cases": cases,
        "coefficient_positions": sum(c["coefficient_positions"] for c in cases),
        "negative_control": {"expected_rank": 2, "altered_rank": bad, "rejected": True},
        "positive_width_margin": [b for b in range(1, 21) if 81 * b > 256],
        "limits": "Finite support controls, not proof of the closed limit step or an exponent improvement.",
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
