"""Standard-library universal replay over Q[a,b,d,d^-1].

This implementation imports neither the symbolic verifier nor a discovery
operator. It checks exact sparse Laurent coefficients and expands the three
leading determinants. The resulting report matches verify_symbolic.py.
"""
import argparse
import ast
from collections import defaultdict
from fractions import Fraction
import gzip
import hashlib
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/conic-third-jets-2026-10-23"
PREDECESSOR = ROOT / "results/conic-second-jets-2026-10-21/witnesses.json.gz"
PREDECESSOR_SHA256 = "c6e529e01f0d0f6363642e6baf03ce178188215269009e3d1e0fb5f54a163a67"
MAX_EXPRESSION_LENGTH = 8192
MAX_EXPRESSION_NODES = 2048
MAX_POWER = 64
MAX_DEGREE = 128
MAX_TERMS = 8192
MAX_COEFFICIENT_BITS = 16384


class Polynomial:
    """Canonical sparse Laurent polynomials with rational coefficients."""

    def __init__(self, value=0):
        if isinstance(value, Polynomial):
            self.terms = value.terms
        elif isinstance(value, dict):
            self.terms = {k: Fraction(v) for k, v in value.items() if v}
        elif type(value) is int or isinstance(value, Fraction):
            self.terms = {(0, 0, 0): Fraction(value)} if value else {}
        else:
            raise TypeError("rational scalar or Laurent polynomial required")
        if len(self.terms) > MAX_TERMS:
            raise ValueError("coefficient exceeds the term budget")
        if any(max(v.numerator.bit_length(), v.denominator.bit_length())
               > MAX_COEFFICIENT_BITS for v in self.terms.values()):
            raise ValueError("coefficient exceeds the rational bit budget")

    def __bool__(self):
        return bool(self.terms)

    def __eq__(self, other):
        if not isinstance(other, (Polynomial, Fraction)) and type(other) is not int:
            return NotImplemented
        return self.terms == Polynomial(other).terms

    def __add__(self, other):
        result = dict(self.terms)
        for exponent, value in Polynomial(other).terms.items():
            result[exponent] = result.get(exponent, 0) + value
        return Polynomial(result)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -Polynomial(other)

    def __rsub__(self, other):
        return Polynomial(other) + -self

    def __mul__(self, other):
        other = Polynomial(other)
        if len(self.terms) * len(other.terms) > 200000:
            raise ValueError("coefficient product exceeds the expansion budget")
        result = defaultdict(Fraction)
        for left, value in self.terms.items():
            for right, coefficient in other.terms.items():
                exponent = tuple(x + y for x, y in zip(left, right))
                if sum(map(abs, exponent)) > MAX_DEGREE:
                    raise ValueError("coefficient exceeds the degree budget")
                result[exponent] += value * coefficient
        return Polynomial(result)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Polynomial(other)
        if len(other.terms) != 1:
            raise ValueError("denominator must be a nonzero rational monomial in d")
        (power, scalar), = other.terms.items()
        if power[:2] != (0, 0):
            raise ValueError("denominator must be a nonzero rational monomial in d")
        return Polynomial({
            (i, j, k - power[2]): value / scalar
            for (i, j, k), value in self.terms.items()
        })

    def __pow__(self, exponent):
        if type(exponent) is not int or abs(exponent) > MAX_POWER:
            raise ValueError("integer exponent exceeds the supported power budget")
        if exponent < 0:
            return Polynomial(1) / self ** (-exponent)
        result, factor = Polynomial(1), self
        while exponent:
            if exponent % 2:
                result = result * factor
            exponent //= 2
            if exponent:
                factor = factor * factor
        return result


A = Polynomial({(1, 0, 0): 1})
B = Polynomial({(0, 1, 0): 1})
D = Polynomial({(0, 0, 1): 1})
SYMBOLS = {"a": A, "b": B, "d": D}


def expression(text):
    """Parse rational arithmetic; never evaluate Python source or calls."""
    if not isinstance(text, str) or len(text) > MAX_EXPRESSION_LENGTH:
        raise ValueError("coefficient must be bounded arithmetic text")
    try:
        tree = ast.parse(text, mode="eval")
    except (SyntaxError, RecursionError, ValueError) as error:
        raise ValueError("invalid coefficient expression") from error
    if sum(1 for _ in ast.walk(tree)) > MAX_EXPRESSION_NODES:
        raise ValueError("coefficient exceeds the syntax budget")

    def read(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            if node.value.bit_length() > 128:
                raise ValueError("coefficient integer exceeds the bit budget")
            return Polynomial(node.value)
        if isinstance(node, ast.Name) and node.id in SYMBOLS:
            return SYMBOLS[node.id]
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return -read(node.operand)
            if isinstance(node.op, ast.UAdd):
                return read(node.operand)
        if isinstance(node, ast.BinOp):
            left, right = read(node.left), read(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
            if isinstance(node.op, ast.Pow):
                if set(right.terms) - {(0, 0, 0)}:
                    raise ValueError("coefficient exponent must be an integer")
                exponent = right.terms.get((0, 0, 0), Fraction(0))
                if exponent.denominator != 1:
                    raise ValueError("coefficient exponent must be an integer")
                return left ** int(exponent)
        raise ValueError("coefficient is not permitted rational arithmetic")

    try:
        value = read(tree.body)
    except RecursionError as error:
        raise ValueError("coefficient exceeds the nesting budget") from error
    if any(i < 0 or j < 0 or k < -2 for i, j, k in value.terms):
        raise ValueError("coefficient is outside Q[a,b,d,d^-1] with d-pole order two")
    return value


def decode(record, shape):
    if not isinstance(record, dict) or set(record) != {"shape", "entries"}:
        raise ValueError("wrong sparse matrix schema")
    if (not isinstance(record["shape"], list)
            or any(type(n) is not int for n in record["shape"])
            or record["shape"] != list(shape)):
        raise ValueError("wrong sparse matrix shape")
    if not isinstance(record["entries"], list):
        raise ValueError("matrix entries must be a list")
    matrix = {}
    for entry in record["entries"]:
        if not isinstance(entry, list) or len(entry) != 3:
            raise ValueError("wrong sparse matrix entry")
        i, j, text = entry
        if (type(i) is not int or type(j) is not int or (i, j) in matrix
                or not 0 <= i < shape[0] or not 0 <= j < shape[1]):
            raise ValueError("wrong or repeated sparse matrix coordinate")
        value = expression(text)
        if not value:
            raise ValueError("stored zero sparse matrix entry")
        matrix[i, j] = value
    return matrix


def add(*matrices):
    result = defaultdict(Polynomial)
    for matrix in matrices:
        for index, value in matrix.items():
            result[index] = result[index] + value
    return {index: value for index, value in result.items() if value}


def negative(matrix):
    return {index: -value for index, value in matrix.items()}


def rows(matrix, selected):
    indices = {old: new for new, old in enumerate(selected)}
    return {(indices[i], j): value for (i, j), value in matrix.items() if i in indices}


def multiply(left, right):
    byrow = defaultdict(list)
    for (i, j), value in right.items():
        byrow[i].append((j, value))
    result = defaultdict(Polynomial)
    for (i, k), value in left.items():
        for j, coefficient in byrow[k]:
            result[i, j] = result[i, j] + value * coefficient
    return {index: value for index, value in result.items() if value}


def contract(left, right):
    """Contract the literal 4096 terms in the published source convention."""
    byleft, byright = defaultdict(list), defaultdict(list)
    for (row, column), value in left.items():
        byleft[column].append((row, value))
    for (row, column), value in right.items():
        byright[column].append((row, value))
    result = defaultdict(Polynomial)
    for i, j, p, q, r, s in product(range(4), repeat=6):
        source = 28 * i + 7 * s + 6 - p - q
        for x, value in byleft[28 * p + 7 * j + 6 - r - s]:
            for y, coefficient in byright[28 * r + 7 * q + 6 - i - j]:
                key = source, 14 * x + y
                result[key] = result[key] + value * coefficient
    return {index: value for index, value in result.items() if value}


def determinant(matrix, columns):
    """Leibniz expansion with subsets sharing the same partial sum."""
    states = {0: Polynomial(1)}
    for row in range(len(columns)):
        following = defaultdict(Polynomial)
        entries = [(j, matrix[row, column]) for j, column in enumerate(columns)
                   if (row, column) in matrix]
        for mask, value in states.items():
            for j, coefficient in entries:
                if mask & (1 << j):
                    continue
                sign = -1 if (mask >> (j + 1)).bit_count() % 2 else 1
                key = mask | (1 << j)
                following[key] = following[key] + sign * value * coefficient
        states = {key: value for key, value in following.items() if value}
    return states.get((1 << len(columns)) - 1, Polynomial())


def verify(record, predecessor):
    """Verify the chart against predecessor data supplied by read_predecessor."""
    required = {"schema", "status", "base", "B", "C", "source_row_corrections",
                "output_pivot_columns", "second_field_weights",
                "coefficient_denominators", "exponent_improvement",
                "independent_mathematical_review"}
    if not isinstance(record, dict) or set(record) != required:
        raise ValueError("wrong mixed third-jet schema")
    if (record["schema"] != "mixed-conic-third-jet-v1"
            or record["status"] != "explicit-witness" or record["base"] != "c=-d^3"):
        raise ValueError("wrong mixed third-jet schema or conic chart")
    if (record["exponent_improvement"] is not False
            or record["independent_mathematical_review"] is not False):
        raise ValueError("wrong claim scope or review metadata")
    for key, count in (("B", 4), ("C", 4), ("source_row_corrections", 3)):
        if not isinstance(record[key], list) or len(record[key]) != count:
            raise ValueError("wrong jet order")
    pivots = record["output_pivot_columns"]
    if (not isinstance(pivots, list) or len(pivots) != 12
            or any(type(j) is not int or not 0 <= j < 196 for j in pivots)
            or len(set(pivots)) != 12):
        raise ValueError("wrong first-source minor coordinates")
    bs, cs = ([decode(row, (14, 112)) for row in record[key]] for key in ("B", "C"))
    ys = [decode(row, (100, 12)) for row in record["source_row_corrections"]]
    if (not isinstance(predecessor, dict)
            or any(not isinstance(predecessor.get(key), list)
                   or len(predecessor[key]) != 3 for key in ("B", "C"))):
        raise ValueError("wrong predecessor jet schema")
    old_b, old_c = ([decode(row, (14, 112)) for row in predecessor[key]]
                    for key in ("B", "C"))
    if bs[:2] != old_b[:2] or cs[:2] != old_c[:2]:
        raise ValueError("changed credited constant or first coefficient")

    delta = (A + D ** 3) * (B - D ** 3)
    weights = [-delta ** 2 * (B - 2 * D ** 3) / (3 * D ** 2),
               -D * delta ** 2 * (B + D ** 3) / 3,
               delta ** 2 * (B - D ** 3) / (3 * D ** 2),
               B * D * delta ** 2 / 3]
    normal_b = {index: value / D for index, value in bs[1].items() if index[1] // 28 == 1}
    normal_c = {index: value / D for index, value in cs[1].items() if index[1] // 7 % 4 == 1}
    expected_b = {index: delta * value / 3 for index, value in normal_b.items()}
    expected_c = {index: delta * value / 3 for index, value in normal_c.items()}
    for r, weight in zip((0, 1, 2, 5), weights):
        for index in ((2 * r, 1), (2 * r + 1, 2)):
            expected_b[index] = expected_b.get(index, Polynomial()) + weight
    for maps, old, expected in ((bs, old_b, expected_b), (cs, old_c, expected_c)):
        if add(maps[2], negative(old[2]), negative(expected)):
            raise ValueError("wrong five-field second correction")
    # Check the exported discovery weights without importing its tangent basis.
    expected_weights = [Polynomial() for _ in range(70)]
    for r, weight in zip((0, 1, 2, 5), weights):
        expected_weights[4 * r] = expected_weights[4 * r + 3] = weight
    expected_weights[68] = delta / 3
    if (not isinstance(record["second_field_weights"], list)
            or len(record["second_field_weights"]) != 70
            or [expression(x) for x in record["second_field_weights"]] != expected_weights):
        raise ValueError("wrong second-field weight metadata")
    denominators = record["coefficient_denominators"]
    if (not isinstance(denominators, list) or not denominators
            or any(not isinstance(x, str) for x in denominators)):
        raise ValueError("wrong denominator metadata")
    for text in denominators:
        value = expression(text)
        if (len(value.terms) != 1
                or any(i or j or k not in (0, 1, 2) for i, j, k in value.terms)):
            raise ValueError("wrong denominator metadata")

    first = [28 * i + 7 * j + z for i, j, z in product((1, 2), (1, 2), (0, 3, 6))]
    outside = [i for i in range(112) if i not in first]
    fs = [add(*(contract(bs[i], cs[k - i]) for i in range(k + 1))) for k in range(4)]
    if rows(fs[0], outside):
        raise ValueError("nonzero constant kernel coefficient")
    rb = [28 * p + 7 * j + z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    rc = [28 * j + 7 * p + z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    determinants = [determinant(bs[0], rb[2:]), determinant(cs[0], rc[2:]),
                    determinant(rows(fs[0], first), pivots)]
    if determinants != [Polynomial(1), Polynomial(1), Polynomial(-1)]:
        raise ValueError("wrong leading minor determinant")
    for k in range(1, 4):
        residual = add(rows(fs[k], outside), negative(add(*(
            multiply(ys[i - 1], rows(fs[k - i], first)) for i in range(1, k + 1)))))
        if residual:
            raise ValueError(f"nonzero Laurent order {k} incidence coefficient")
    return {
        "field": "Q(a,b,d)", "coefficient_ring": "Q[a,b,d,d^-1]",
        "scope": "Every complex a,b,d with d nonzero, c=-d^3",
        "source_terms": 4096, "jet_order": 3,
        "leading_minor_determinants": ["1", "1", "-1"],
        "kernel_coordinates_per_order": 19600, "positive_orders_checked": 3,
        "normal_class": "[1:d]", "matrix_target_constructed": False,
        "all_order_lift_established": False, "exponent_improvement": False,
    }


def read_predecessor(path=PREDECESSOR):
    data = Path(path).read_bytes()
    if hashlib.sha256(data).hexdigest() != PREDECESSOR_SHA256:
        raise ValueError("predecessor hash does not match the credited source")
    try:
        return json.loads(gzip.decompress(data))["cubic_component_two_jet"]
    except (KeyError, TypeError) as error:
        raise ValueError("missing predecessor cubic two-jet") from error


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("witness", type=Path, nargs="?", default=RESULTS / "mixed-family.json")
    parser.add_argument("--predecessor", type=Path, default=PREDECESSOR)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.witness.read_text()), read_predecessor(args.predecessor))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report))
