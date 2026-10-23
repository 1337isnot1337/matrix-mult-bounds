"""Two exact compositions of the coupled Laurent core with private entries.

One composition is a degeneration with a twelve-term degree-one error.
The other gives a two-channel tail exactly for every nonzero parameter.
All coefficient checks use only Python's standard library.
"""

from collections import defaultdict
import hashlib
from itertools import product
import json
from math import lcm
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parity_structure_spin_w34_laurent as core
from crossed_module11 import unpack
from spin_module14 import column_entries, full_terms, pack

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
ATTACHMENTS = DIRECTORY / "spin-channel-extension-maps.json"
DEGENERATION = DIRECTORY / "parity_structure_spin_w34_laurent_extension_maps.json"
TWO_CHANNEL = DIRECTORY / "parity_structure_spin_w34_two_channel_maps.json"
ORDINARY = DIRECTORY / "parity_structure_spin_w34_two_channel_t1_maps.json"
REPORT = DIRECTORY / "parity_structure_spin_w34_laurent_extension_certificate.json"


def build(kind):
    if kind not in ("eight_entry_degeneration", "four_two_channel_vertices"):
        raise ValueError("Unknown composition")
    original = json.loads(core.MAPS.read_text())
    maps, denominators = core.parse(original)
    attached = json.loads(ATTACHMENTS.read_text())
    X, dx = unpack(attached["maps"]["X"], (33, 960))
    Y, dy = unpack(attached["maps"]["Y"], (89, 960))
    if denominators[0] % dx or denominators[1] % dy:
        raise ArithmeticError("The common-denominator convention changed")
    if kind == "eight_entry_degeneration":
        maps[0][0].extend([[value*(denominators[0]//dx) for value in row] for row in X[9:]])
        maps[1][-1].extend([[0]*960 for _ in range(8)])
        maps[1][0].extend([[value*(denominators[1]//dy) for value in row] for row in Y[81:]])
        shape = [33, 89, 81]
    else:
        selected = list(range(9))+list(range(15, 21))+list(range(27, 33))
        maps[0][0] = [[value*(denominators[0]//dx) for value in X[row]] for row in selected]
        for vertex in range(8):
            row = [value*(denominators[1]//dy) for value in Y[81+vertex]]
            second_channel = vertex in (0, 1, 4, 5)
            maps[1][-1].append(row if second_channel else [0]*960)
            maps[1][0].append([0]*960 if second_channel else row)
        shape = [21, 89, 81]
    return {
        "kind": kind, "field": "Q(t)", "source": [8, 8],
        "target_dimensions": shape, "core": "M(3,3,27)",
        "exact_for_every_nonzero_parameter": kind == "four_two_channel_vertices",
        "maps": {name: {str(power): pack(matrix, denominator) for power, matrix in axis.items()}
                 for name, axis, denominator in zip("XYZ", maps, denominators)},
        "new_exponent_established": False,
    }


def parse(data):
    kind = data["kind"]
    shape = [33, 89, 81] if kind == "eight_entry_degeneration" else [21, 89, 81]
    if (kind not in ("eight_entry_degeneration", "four_two_channel_vertices")
            or data["source"] != [8, 8] or data["target_dimensions"] != shape
            or data.get("new_exponent_established") is not False):
        raise ArithmeticError("The composition scope changed")
    answer, denominators = [], []
    for axis, name in enumerate("XYZ"):
        powers = ({"0"}, {"-1", "0"}, {"0", "1"})[axis]
        if set(data["maps"][name]) != powers:
            raise ArithmeticError("The composition powers changed")
        parsed, denominator = {}, 1
        for power, item in data["maps"][name].items():
            matrix, value = unpack(item, (shape[axis], 960))
            parsed[int(power)] = matrix, value
            denominator = lcm(denominator, value)
        answer.append({power: [[value*(denominator//old) for value in row] for row in matrix]
                       for power, (matrix, old) in parsed.items()})
        denominators.append(denominator)
    return answer, denominators


def expected_constant(kind, scale):
    expected = {(3*I+J, 27*J+alpha, 27*I+alpha): scale
                for I, J, alpha in product(range(3), range(3), range(27))}
    if kind == "eight_entry_degeneration":
        expected.update({(9+3*vertex+I, 81+vertex, 27*I): scale
                         for vertex, I in product(range(8), range(3))})
    else:
        for vertex, old in enumerate((2, 3, 6, 7)):
            for I in range(3):
                expected[9+3*vertex+I, 81+old, 27*I] = scale
                expected[9+3*vertex+I, 81+old-2, 27*I+16] = scale
    return expected


def specialize(data):
    maps, denominators = parse(data)
    ordinary = core.specialize_one(maps)
    return {"field": "Q", "source": [8, 8], "target_dimensions": [21, 89, 81],
            "target": "M(3,3,27) glued to M(3,4,2) along middle channels0 and16",
            "maps": {name: pack(matrix, denominator)
                     for name, matrix, denominator in zip("XYZ", ordinary, denominators)},
            "new_exponent_established": False}


def verify(data, ordinary=None):
    maps, denominators = parse(data)
    kind = data["kind"]
    inverse = [core.polynomial_inverse(axis) for axis in maps]
    image = defaultdict(int)
    for x, y, z in full_terms(8, 8):
        for tx, px, cx in inverse[0].get(x, ()):
            for ty, py, cy in inverse[1].get(y, ()):
                for tz, pz, cz in inverse[2].get(z, ()):
                    image[px+py+pz, tx, ty, tz] += cx*cy*cz
    image = {key: value for key, value in image.items() if value}
    if any(power < 0 for power, _, _, _ in image):
        raise ArithmeticError("A negative-power mixed coefficient survives")
    scale = denominators[0]*denominators[1]*denominators[2]
    constant = {(tx, ty, tz): value for (power, tx, ty, tz), value in image.items() if power == 0}
    expected = expected_constant(kind, scale)
    if constant != expected:
        raise ArithmeticError("The complete constant tensor disagrees with the target")
    positive = {(tx, ty, tz): value for (power, tx, ty, tz), value in image.items() if power == 1}
    if kind == "eight_entry_degeneration":
        wanted = {(9+3*later+I, 81+earlier, 27*I+16): scale
                  for later, earlier in ((2, 0), (3, 1), (6, 4), (7, 5)) for I in range(3)}
        if positive != wanted or any(power > 1 for power, _, _, _ in image):
            raise ArithmeticError("The twelve-term positive error is incorrect")
    elif positive or any(power for power, _, _, _ in image):
        raise ArithmeticError("The two-channel family is not constant for all nonzero t")

    report = {"kind": kind, "target_dimensions": data["target_dimensions"],
              "source_terms_checked": 262144,
              "all_Laurent_target_coefficients_checked": 3*data["target_dimensions"][0]*89*81,
              "nonzero_constant_coefficients": len(constant),
              "negative_power_coefficients_zero": True,
              "positive_degree_one_coefficients": len(positive),
              "integer_coefficient_scale": scale,
              "exact_for_every_nonzero_parameter": kind == "four_two_channel_vertices",
              "full_square_target_constructed": False, "new_exponent_established": False}
    if kind == "four_two_channel_vertices":
        if ordinary is None:
            raise ArithmeticError("The exact ordinary t=1 maps must be supplied")
        if ordinary != specialize(data):
            raise ArithmeticError("The actual ordinary maps disagree with evaluation at t=1")
        numerical_maps, numerical_denominators = [], []
        for name, rows in zip("XYZ", (21, 89, 81)):
            matrix, denominator = unpack(ordinary["maps"][name], (rows, 960))
            numerical_maps.append(matrix)
            numerical_denominators.append(denominator)
        numerical_inverse = [column_entries(matrix) for matrix in numerical_maps]
        evaluated = defaultdict(int)
        for x, y, z in full_terms(8, 8):
            for tx, cx in numerical_inverse[0].get(x, ()):
                for ty, cy in numerical_inverse[1].get(y, ()):
                    for tz, cz in numerical_inverse[2].get(z, ()):
                        evaluated[tx, ty, tz] += cx*cy*cz
        evaluated = {key: value for key, value in evaluated.items() if value}
        evaluated_scale = numerical_denominators[0]*numerical_denominators[1]*numerical_denominators[2]
        if evaluated != expected_constant(kind, evaluated_scale):
            raise ArithmeticError("The complete ordinary t=1 replay failed")
        report.update({"ordinary_t1_restriction_checked": True,
                       "ordinary_t1_target_coefficients_checked": 21*89*81,
                       "new_vertices": 4, "middle_channels_per_new_vertex": 2,
                       "filled_middle_channels": [0, 16]})
    return report


if __name__ == "__main__":
    first, second = build("eight_entry_degeneration"), build("four_two_channel_vertices")
    ordinary = specialize(second)
    DEGENERATION.write_text(json.dumps(first, indent=2)+"\n")
    TWO_CHANNEL.write_text(json.dumps(second, indent=2)+"\n")
    ORDINARY.write_text(json.dumps(ordinary, indent=2)+"\n")
    report = {
        "eight_entry_degeneration": verify(json.loads(DEGENERATION.read_text())),
        "four_two_channel_vertices": verify(json.loads(TWO_CHANNEL.read_text()), json.loads(ORDINARY.read_text())),
        "new_exponent_established": False,
    }
    for key, path in (("degeneration_maps_sha256", DEGENERATION), ("two_channel_maps_sha256", TWO_CHANNEL),
                      ("ordinary_t1_maps_sha256", ORDINARY)):
        report[key] = hashlib.sha256(path.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
