"""Exact finite controls for the prescribed graded correction model."""
import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = importlib.util.spec_from_file_location("quantum_correction_model", HERE/"quantum.py")
quantum = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quantum)


def decode(coefficients, field):
    value = field.zero
    for coefficient in coefficients:
        value = value*field.unit+field.convert(Fraction(coefficient))
    return value


def verify():
    field, maps, records, tensor, weights = quantum.build()
    stored_path = ROOT/"results/quantum-correction-2026-10-21/N5-m4-family.json"
    stored = json.loads(stored_path.read_text())
    assert stored["maps"] == [[[quantum.q.screen.encode_field(x) for x in row]
                              for row in matrix] for matrix in maps]
    # JSON serializes the exact (k, ell) labels as lists rather than tuples.
    assert stored["local_records"] == json.loads(json.dumps(records))
    assert tensor == {tuple(row["positions"]): decode(row["coefficient"], field)
                      for row in stored["tensor"]}
    assert all(quantum.q.core.rank_over_field(matrix, field.zero) == len(matrix)
               for matrix in maps)
    source_control = quantum.q.source_control(6, 4)
    profile = []
    for weight in sorted(set(weights[0])):
        indices = [i for i, w in enumerate(weights[0]) if w == weight]
        coefficients = ([i*i+1 for i in range(len(indices))] if weight == 0
                        else list(range(1, len(indices)+1)))
        matrix = [[sum((field.convert(c)*tensor.get((i, j, k), field.zero)
                        for i, c in zip(indices, coefficients)), field.zero)
                   for k in range(20)] for j in range(20)]
        rank = quantum.q.core.rank_over_field(matrix, field.zero)
        profile.append(dict(weight=weight, source_indices=indices,
                            source_coefficients=coefficients, exact_rank=rank,
                            target_weight_space_maximum_rank=4*len(indices)))
    assert [row["exact_rank"] for row in profile] == [6, 9, 12, 16, 20, 16, 12, 9, 6]
    assert [row["target_weight_space_maximum_rank"] for row in profile] == [4, 8, 12, 16, 20, 16, 12, 8, 4]
    central = [DomainMatrix([[tensor.get((i, j, k), field.zero) for k in range(20)]
                            for j in range(20)], (20, 20), field)
               for i in range(10, 15)]
    anchor_coefficients = [1, 2, 5, 10, 17]
    anchor = sum((matrix.scalarmul(field.convert(c))
                  for matrix, c in zip(central, anchor_coefficients)),
                 DomainMatrix.zeros((20, 20), field))
    inverse = anchor.inv()
    normalized = [matrix.matmul(inverse) for matrix in central]
    commutator = normalized[1].matmul(normalized[2])-normalized[2].matmul(normalized[1])
    commutator_rank = commutator.rank()
    assert commutator_rank == 14
    commutator_rows = commutator.to_list()
    witness = next((i, j, quantum.q.screen.encode_field(value))
                   for i, row in enumerate(commutator_rows)
                   for j, value in enumerate(row) if value)
    assignment_rows = []
    for assignment in [
        [(-8, 3, 5), (-8, 5, 3), (8, -3, -5), (8, -5, -3), (-6, 3, 3), (6, -3, -3)],
        [(-8, 3, 5), (-8, 5, 3), (8, -3, -5), (8, -5, -3), (-6, 1, 5), (6, -1, -5)],
        [(-8, 3, 5), (-8, 5, 3), (8, -3, -5), (8, -5, -3), (-6, 5, 1), (6, -5, -1)],
    ]:
        counts = [Counter(point[axis] for point in assignment) for axis in range(3)]
        assert all(sum(point) == 0 for point in assignment)
        assert counts[0].get(0, 0) == 0
        assert max(counts[1].values()) < 5 and max(counts[2].values()) < 5
        assignment_rows.append(dict(weights=assignment,
                                    maximum_auxiliary_count_at_one_B_weight=max(counts[1].values()),
                                    maximum_auxiliary_count_at_one_C_weight=max(counts[2].values()),
                                    auxiliary_count_at_A_weight_zero=0))
    return dict(source="Q(6,4)", source_format=[36, 36, 36],
                regular_point_format=[25, 20, 20], cyclotomic_order=14,
                exact_source_control_coefficients=source_control,
                exact_regular_tensor_nonzero_coefficients=len(tensor),
                full_tensor_composition_matches_stored=True,
                slice_rank_witnesses=profile,
                central_anchor_coefficients=anchor_coefficients,
                central_anchor_rank=20,
                central_commutator_source_indices=[11, 12],
                central_commutator_exact_rank=commutator_rank,
                central_commutator_nonzero_entry=witness,
                excluded_D6_weight_assignments=assignment_rows,
                excludes_all_graded_auxiliary_assignments_of_rank_at_most_four=True,
                excludes_unrestricted_corrections=False,
                improves_omega=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT/"results/quantum-correction-2026-10-21/certificate.json")
    args = parser.parse_args()
    result = verify()
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in ["exact_source_control_coefficients",
                    "exact_regular_tensor_nonzero_coefficients", "central_commutator_exact_rank",
                    "improves_omega"]}))
