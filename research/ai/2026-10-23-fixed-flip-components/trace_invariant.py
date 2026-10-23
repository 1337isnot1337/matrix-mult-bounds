"""Exact positive-trace certificate for the five-split flip component.

This supports TRACE_PROOF.md.  It excludes further subset deletion under
the physical stabilizer, not arbitrary border-rank reductions.
"""
import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "five_split_component_geometry", PACKAGE / "verify.py")
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
SCHEMA = "five-split-positive-trace-v1"
SCOPE = ("Finite standard shared-factor flips and term gauges over characteristic-zero "
         "field extensions; no further nonempty-subset physical-stabilizer deletion.")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def trace_product(u, v, w):
    return sum(u[5 * i + j] * v[5 * j + k] * w[4 * k + i]
               for i in range(4) for j in range(5) for k in range(5))


def pairing(factors, group):
    """Pair Z_i=U_i tensor W_i with V_j; do not replace W_i by W_j."""
    return [[trace_product(factors[0][i], factors[1][j], factors[2][i])
             for j in group] for i in group]


def build_certificate():
    factors = C.seed("five")
    components = C.sharing_components(factors)
    groups = []
    for group in components:
        matrix = pairing(factors, group)
        groups.append({"indices": group, "scalar": matrix[0][0], "pairing": matrix})
    return {
        "schema": SCHEMA,
        "scope": SCOPE,
        "source_sha256": C.W.SOURCE_HASH,
        "replacements": [list(row) for row in C.SCENARIOS["five"]["replacements"]],
        "groups": groups,
        "original_discarded_term_traces": [0] * 5,
    }


def verify(certificate=None):
    if certificate is None:
        certificate = json.loads((PACKAGE / "trace_certificate.json").read_text())
    require(certificate.get("schema") == SCHEMA, "Trace certificate schema differs")
    require(certificate.get("scope") == SCOPE, "Trace certificate scope differs")
    require(certificate.get("source_sha256") == C.W.SOURCE_HASH,
            "Trace certificate source pin differs")
    replacements = C.SCENARIOS["five"]["replacements"]
    require(certificate.get("replacements") == [list(row) for row in replacements],
            "Trace certificate replacements differ")
    factors = C.seed("five")
    # The companion independently checks all three leg-span intersections and
    # both sides of each V-flattening, using ranks modulo 101 as lower bounds.
    components, _, _, _, checks = C.analyze_components(factors)
    records = certificate["groups"]
    require([record["indices"] for record in records] == components,
            "Trace certificate does not cover exactly the isolated components")
    values = []
    for record, group in zip(records, components):
        actual = pairing(factors, group)
        scalar = actual[0][0]
        require(scalar in (1, 2), "A component trace scalar is not positive")
        expected = [[scalar if i == j else 0 for j in range(len(group))]
                    for i in range(len(group))]
        require(actual == expected, "A component trace pairing is not scalar identity")
        require(record["scalar"] == scalar and record["pairing"] == actual,
                "Recorded trace pairing differs from direct integer contraction")
        values.extend([scalar] * len(group))
    require(Counter(values) == {1: 52, 2: 24}, "Unexpected individual trace counts")
    original = C.W.load_factors()
    discarded_traces = []
    for i, j, scalar in replacements:
        difference = [x - scalar * y for x, y in zip(original["u"][i], original["u"][j])]
        discarded_traces.append(trace_product(difference, original["v"][i], original["w"][i]))
    require(discarded_traces == [0] * 5, "Original discarded error is not trace zero")
    require(certificate["original_discarded_term_traces"] == discarded_traces,
            "Recorded discarded trace values differ")
    return {
        "claim_id": "AI-EXTERNAL-FIVE-SPLIT-TRACE-005",
        "source_sha256": C.W.SOURCE_HASH,
        "isolated_components": len(components),
        "cross_component_disjointness_checks": checks,
        "component_pairings_are_positive_scalar_identities": True,
        "individual_trace_values": {"1": 52, "2": 24},
        "total_surviving_trace": sum(values),
        "original_discarded_error_trace": sum(discarded_traces),
        "five_split_finite_flip_subset_deletion_excluded": True,
        "valid_over_Laurent_field_extensions_of_C": True,
        "four_split_subset_deletion_excluded": False,
        "general_border_rank_reduction_excluded": False,
        "proof_status": "written-unreviewed",
        "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-certificate", type=Path)
    args = parser.parse_args()
    if args.write_certificate:
        witness = build_certificate()
        result = verify(witness)
        args.write_certificate.write_text(json.dumps(witness, indent=2) + "\n")
    else:
        result = verify()
    print(json.dumps(result, indent=2))
