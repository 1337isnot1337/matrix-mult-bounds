"""Exact replay of source ranks and canonical target component certificates."""

from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "research/ai/2026-10-23-mixed-longlegs-candidate"
RESULTS = ROOT / "results/mixed-longlegs-candidate-2026-10-23"


def load(name):
    spec = importlib.util.spec_from_file_location("mixed_source_" + name, PACKAGE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sys.path.insert(0, str(PACKAGE))
try:
    B = load("verify_full_source_exterior")
    C = load("verify_full_source_all_c")
    PILOT = load("full_source_c_leg_pilot")
    DQ = load("shared_output_prolongation")
    SCHUR = load("shared_output_schur")
finally:
    sys.path.pop(0)


def report(name):
    return json.loads((RESULTS / name).read_text())


class MixedSourceFlatteningsTests(unittest.TestCase):
    def test_integrated_file_pins_and_preserved_reports(self):
        manifest = json.loads((PACKAGE / "source_flattenings_manifest.json").read_text())
        for path, expected in manifest["integrated_sha256"].items():
            with self.subTest(path=path):
                self.assertEqual(sha256((ROOT / path).read_bytes()).hexdigest(), expected)
        unchanged = {
            "full_source_exterior_controls.json", "full_source_c_leg_pilot.json",
            "shared_output_prolongation_controls.json", "shared_output_schur_controls.json",
            "higher_koszul_work/first_critical_source_kernel.md",
        }
        for item in manifest["originals"]:
            if item["original_name"] in unchanged:
                self.assertEqual(sha256((ROOT / item["integrated_path"]).read_bytes()).hexdigest(),
                                 item["original_sha256"])
        for path, expected in report("full_source_all_c_controls.json")["sources_sha256"].items():
            self.assertEqual(sha256((ROOT / path).read_bytes()).hexdigest(), expected)

    def test_all_120_literal_B_controls(self):
        data = report("full_source_exterior_controls.json")
        self.assertEqual(data["control_count"], 120)
        for row in data["controls"]:
            self.assertEqual(B.exact_mod2_rank(row["a"], row["widths"], row["p"]), row)
        self.assertEqual(data["new_candidate_source"]["exterior_ranks_p_0_through_3"],
                         [140, 12735, 573540, 17050935])

    def test_all_97_literal_C_controls(self):
        controls = report("full_source_c_leg_pilot.json")
        self.assertEqual(len(controls), 97)
        for row in controls:
            with self.subTest(a=row["a"], widths=row["widths"], p=row["p"]):
                self.assertEqual(PILOT.rank_mod2(row["a"], row["widths"], row["p"]), row)
                formula = C.check_formula(row["a"], row["N"], row["M"], row["p"])
                self.assertEqual(formula["rank"], row["rank_mod2"])

    def test_positive_and_alternating_C_formulas_including_endpoints(self):
        count = 0
        for a in range(2, 7):
            for n in range(1, 9):
                for d in range(6):
                    m = n + a - 1 + d
                    for p in range(m + 1):
                        row = C.check_formula(a, n, m, p)
                        self.assertGreaterEqual(row["rank"], 0)
                        count += 1
        self.assertEqual(count, 2640)
        self.assertEqual(C.check_formula(2, 1, 2, 1)["kernel"], 0)
        self.assertEqual(C.check_formula(2, 1, 2, 2)["kernel"], 1)
        data = report("full_source_all_c_controls.json")
        self.assertEqual(data["candidate"]["degrees"],
                         [C.check_formula(5, 100, 140, p) for p in range(140)])
        expected = [3, 27, 108, 237, 306, 237, 108, 27, 3]
        self.assertEqual([PILOT.rank_mod2(3, [1, 1, 1], p)["rank_mod2"] for p in range(9)],
                         expected)

    def test_all_125_target_tensor_power_systems_over_Q(self):
        data = report("shared_output_prolongation_controls.json")
        count = 0
        for saved in data["target_controls"]:
            self.assertEqual(DQ.target_control(saved["degree"], rational=True), saved)
            self.assertFalse(saved["exclusion_over_complex_numbers"])
            count += len(saved["block_tuples"])
        self.assertEqual(count, 125)
        self.assertEqual([row["target_rank_rational"] for row in data["target_controls"]],
                         [140, 25317, 3432270, 412195367])

    def test_Schur_source_characters_and_mixed_literal_traces(self):
        data = report("shared_output_schur_controls.json")
        for row in data["source_trace_controls"]:
            if row["width"] != 2:
                continue
            actual = SCHUR.tuple_kernel_trace([("Full", 5, 2)] * row["degree"],
                                               tuple(row["permutation"]))
            self.assertEqual(actual["trace"], row["formula"])
        selections = [(3, "21", [4, 2]), (4, "22", [2, 0]), (4, "31", [2, 4])]
        for q, class_name, labels in selections:
            saved_degree = next(item for item in data["degrees"] if item["degree"] == q)
            saved_class = next(item for item in saved_degree["class_records"] if item["class"] == class_name)
            saved = next(item for item in saved_class["controls"] if item["cycle_types"] == labels)
            permutation = next(item[2] for item in SCHUR.CLASSES[q] if item[0] == class_name)
            kinds = [None] * q
            for cycle, label in zip(SCHUR.cycles(permutation), labels):
                for position in cycle:
                    kinds[position] = DQ.TYPES[label][:3]
            actual = SCHUR.tuple_kernel_trace(kinds, permutation)
            self.assertEqual(actual, {key: saved[key] for key in ("kernel_dimension", "trace")})

    def test_all_ten_Schur_component_rank_comparisons(self):
        data = report("shared_output_schur_controls.json")
        nullities = {row["degree"]: row["target_nullity_rational"]
                     for row in report("shared_output_prolongation_controls.json")["target_controls"]}
        count = 0
        for degree in data["degrees"]:
            q = degree["degree"]
            SCHUR.verify_character_table(q)
            characters = degree["kernel_characters"]
            self.assertEqual(characters[0], nullities[q])
            for index, record in enumerate(degree["class_records"], 1):
                self.assertEqual(sum(row["weight"] * row["trace"] for row in record["controls"]),
                                 characters[index])
            total = 0
            for piece in degree["pieces"]:
                partition = tuple(piece["partition"])
                irreducible = SCHUR.CHARACTERS[q][partition]
                numerator = sum(item[1] * chi * value for item, chi, value
                                in zip(SCHUR.CLASSES[q], irreducible, characters))
                self.assertEqual(numerator, factorial(q) * piece["target_kernel"])
                domain = 5 * SCHUR.schur_dimension(partition, 100)
                source_kernel = (5 - q) * SCHUR.schur_dimension(partition, 90)
                self.assertEqual(piece["source_rank"], domain - source_kernel)
                self.assertEqual(piece["target_rank"], domain - piece["target_kernel"])
                self.assertLessEqual(piece["target_rank"], piece["source_rank"])
                total += irreducible[0] * piece["target_kernel"]
                count += 1
            self.assertEqual(total, nullities[q])
        self.assertEqual(count, 10)


if __name__ == "__main__":
    unittest.main()
