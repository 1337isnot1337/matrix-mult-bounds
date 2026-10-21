"""Exhaust all nonnegative integer factor pairs for the H1100 Cartan characters."""
from collections import defaultdict
from itertools import combinations_with_replacement, product
import json


def multiply(f, g):
    result = [0]*(len(f)+len(g)-1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            result[i+j] += x*y
    return result


def positive_factors(q, first_sum, second_sum):
    """Every nonnegative-coefficient factor pair, normalized with nonzero endpoints."""
    degree = len(q)-1
    answers, nodes = [], 0
    for first_degree in range(degree+1):
        second_degree = degree-first_degree
        for f0 in range(1, first_sum+1):
            if q[0] % f0:
                continue
            g0 = q[0]//f0
            if not 1 <= g0 <= second_sum:
                continue
            f, g = [f0]+[0]*first_degree, [g0]+[0]*second_degree

            def visit(k, fs, gs):
                nonlocal nodes
                nodes += 1
                if fs > first_sum or gs > second_sum:
                    return
                if k > max(first_degree, second_degree):
                    if (fs == first_sum and gs == second_sum and f[-1] > 0 and g[-1] > 0
                            and multiply(f, g) == q):
                        answers.append([f.copy(), g.copy()])
                    return
                known = sum(f[i]*g[k-i] for i in range(1, min(k, first_degree+1))
                            if 0 <= k-i <= second_degree)
                choices = (range(1 if k == first_degree else 0, first_sum-fs+1)
                           if k <= first_degree else (0,))
                for fk in choices:
                    remainder = q[k]-known-fk*g0
                    if k <= second_degree:
                        if remainder < 0 or remainder % f0:
                            continue
                        gk = remainder//f0
                        if gk > second_sum-gs or (k == second_degree and gk == 0):
                            continue
                    else:
                        if remainder:
                            continue
                        gk = 0
                    if k <= first_degree:
                        f[k] = fk
                    if k <= second_degree:
                        g[k] = gk
                    visit(k+1, fs+fk, gs+gk)

            visit(1, f0, g0)
    return answers, nodes


def report():
    p = multiply(multiply([1]*4, [1]*4), [1]*7)
    records, candidates = [], []
    for i, j in combinations_with_replacement(range(13), 2):
        q = p.copy()
        q[i] -= 1
        q[j] -= 1
        if min(q) < 0:
            continue
        shift = 0
        while q[0] == 0:
            shift += 1
            q.pop(0)
        while q[-1] == 0:
            q.pop()
        pairs, nodes = positive_factors(q, 10, 11)
        records.append({"deficit": [i, j], "reduced_coefficients": q, "monomial_shift": shift,
                        "nodes_visited": nodes, "positive_factor_pairs": pairs})
        for f, g in pairs:
            candidates.append({"deficit": [i, j], "U": f, "W": g[::-1],
                               "U_shift_relative_to_W": shift-6+len(g)-1})
    survivors = []
    for first, second in product(candidates, repeat=2):
        if first["W"] != second["W"]:
            continue
        uv = defaultdict(int)
        for i, j in product(range(len(first["U"])), range(len(second["U"]))):
            weight = i-j+first["U_shift_relative_to_W"]-second["U_shift_relative_to_W"]
            uv[weight] += first["U"][i]*second["U"][j]
        if all(value <= (p[weight+6] if 0 <= weight+6 < len(p) else 0)
               for weight, value in uv.items()):
            survivors.append({"U": first["U"], "V": second["U"], "W": first["W"],
                              "U_shift": first["U_shift_relative_to_W"],
                              "V_shift": second["U_shift_relative_to_W"], "W_shift": 0})
    assert len(records) == 89 and len(candidates) == 4 and len(survivors) == 1
    expected = {"U": [1, 1, 2, 2, 2, 1, 1], "V": [1, 1, 2, 2, 2, 1, 1],
                "W": [1, 2, 2, 1, 2, 2, 1], "U_shift": 0, "V_shift": 0, "W_shift": 0}
    assert survivors == [expected]
    return {"source": "A4", "target": "M(10,10,11)", "source_character_coefficients": p,
            "source_weight_offset": -6, "deficit_patterns_checked": len(records),
            "coefficient_search_nodes": sum(r["nodes_visited"] for r in records),
            "records": records, "pair_candidates": candidates, "surviving_vertex_characters": survivors,
            "character_pattern_is_a_construction": False, "new_exponent_established": False}


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
