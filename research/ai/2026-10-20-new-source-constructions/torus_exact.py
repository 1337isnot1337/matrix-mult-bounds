"""Exact nonmonic flag certificate checks and optional finite-field discovery."""
from __future__ import annotations

import argparse
from functools import reduce
import hashlib
import json
from pathlib import Path
import sys
import time

PREDECESSOR = Path(__file__).resolve().parents[1] / "2026-10-20-balanced-coefficients"
sys.path.insert(0, str(PREDECESSOR))
from coefficient_system import System
from finite_field import equations
from target_orbit import incidence_data


class Field:
    def __init__(self, order):
        if order not in (3, 4):
            raise ValueError("only F3 and F4 are implemented")
        self.order = order

    def add(self, a, b):
        return (a+b) % 3 if self.order == 3 else a ^ b

    def neg(self, a):
        return (-a) % 3 if self.order == 3 else a

    def mul(self, a, b):
        if self.order == 3:
            return a*b % 3
        a0, a1, b0, b1 = a & 1, a >> 1, b & 1, b >> 1
        return ((a0 & b0) ^ (a1 & b1)) | (((a0 & b1) ^ (a1 & b0) ^ (a1 & b1)) << 1)

    def inv(self, a):
        if not a:
            raise ZeroDivisionError
        return a if self.order == 3 else self.mul(a, a)

    def product(self, values):
        return reduce(self.mul, values, 1)

    def sum(self, values):
        return reduce(self.add, values, 0)


def rank_field(matrix, field):
    matrix = [list(row) for row in matrix]
    count, pivots = 0, []
    for column in range(len(matrix[0]) if matrix else 0):
        pivot = next((row for row in range(count, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[count], matrix[pivot] = matrix[pivot], matrix[count]
        inverse = field.inv(matrix[count][column])
        matrix[count] = [field.mul(inverse, value) for value in matrix[count]]
        for row in range(count+1, len(matrix)):
            factor = matrix[row][column]
            if factor:
                matrix[row] = [field.add(a, field.neg(field.mul(factor, b)))
                               for a, b in zip(matrix[row], matrix[count])]
        count += 1
        pivots.append(column)
        if count == len(matrix):
            break
    return count, pivots


class ExactModel:
    def __init__(self):
        self.system = System()
        self.variables, self.equations = equations(self.system)
        self.all_triples = [(p,y,z) for level in self.system.levels
                            for p,y,z,_ in level["constraints"]]
        self.targets, self.incidence, self.columns, relations = incidence_data(self.system)
        self.relations = [[int(value) for value in relation] for relation in relations]
        self.target_indices = [self.all_triples.index(triple) for triple in self.targets]
        self.zero_indices = [index for index, (_, wanted) in enumerate(self.equations) if not wanted]
        self.rows = list(self.incidence[:, self.columns].T.rref()[1])
        self.minor = self.incidence.extract(self.rows, self.columns)
        self.inverse = self.minor.inv()
        if self.minor.det() != -1 or any(value.q != 1 for value in self.inverse):
            raise ArithmeticError("expected integral torus normalization failed")

    def coefficient_values(self, values, field):
        if len(values) != len(self.variables) or any(not isinstance(v, int) or not 0 <= v < field.order for v in values):
            raise ValueError("invalid coefficient vector")
        coefficients, jacobian = [], []
        for terms, _ in self.equations:
            value, row = 0, [0]*len(values)
            for term in terms:
                value = field.add(value, field.product(values[j] for j in term))
                for position, column in enumerate(term):
                    derivative = field.product(values[j] for i,j in enumerate(term) if i != position)
                    row[column] = field.add(row[column], derivative)
            coefficients.append(value)
            jacobian.append(row)
        return coefficients, jacobian

    def replay(self, values, order):
        field = Field(order)
        coefficients, derivatives = self.coefficient_values(values, field)
        targets = [coefficients[index] for index in self.target_indices]
        target_derivatives = [derivatives[index] for index in self.target_indices]
        errors = [coefficients[index] for index in self.zero_indices]
        jacobian = [derivatives[index] for index in self.zero_indices]
        toric_errors = []
        for relation in self.relations:
            sides = [[i for i,n in enumerate(relation) if n == sign] for sign in (1, -1)]
            products = [field.product(targets[i] for i in side) for side in sides]
            error = field.add(products[0], field.neg(products[1]))
            row = [0]*len(values)
            for sign, side in zip((1, -1), sides):
                for differentiated in side:
                    factor = field.product(targets[i] for i in side if i != differentiated)
                    for column, derivative in enumerate(target_derivatives[differentiated]):
                        term = field.mul(factor, derivative)
                        if sign == -1:
                            term = field.neg(term)
                        row[column] = field.add(row[column], term)
            toric_errors.append(error)
            errors.append(error)
            jacobian.append(row)
        rank, pivots = rank_field(jacobian, field)
        return {"field_order": order, "coefficients_checked": len(coefficients),
                "zero_equations": len(self.zero_indices), "toric_equations": len(self.relations),
                "nonzero_zero_equations": sum(bool(coefficients[i]) for i in self.zero_indices),
                "toric_errors": toric_errors, "zero_target_coefficients": sum(not v for v in targets),
                "target_coefficients": targets, "jacobian_rows": len(jacobian),
                "jacobian_rank": rank, "jacobian_pivot_columns": pivots,
                "nonsingular_hensel_premise": not any(errors) and all(targets) and rank == len(errors)}

    def normalize_target(self, values, order):
        """Recover row scalars using only integer powers and field operations."""
        field = Field(order)
        if len(values) != len(self.targets) or not all(values):
            raise ValueError("twenty nonzero target coefficients required")
        selected = [values[row] for row in self.rows]
        scalars = [1]*24
        for local, column in enumerate(self.columns):
            factors = []
            for power, value in zip(self.inverse[local, :], selected):
                power = int(power)
                factors.extend([value if power >= 0 else field.inv(value)] * abs(power))
            scalars[column] = field.product(factors)
        recovered = [field.product(scalars[column] for column in (p,4+y,14+z)) for p,y,z in self.targets]
        if recovered != values:
            raise ValueError("target coefficients do not lie in the diagonal orbit")
        return scalars

    def structure(self):
        return {"target_terms": self.targets, "incidence_columns": self.columns,
                "incidence_rows": self.rows, "incidence_minor_determinant": int(self.minor.det()),
                "incidence_minor_inverse": [[int(v) for v in row] for row in self.inverse.tolist()],
                "relations": self.relations, "nonpositive_entries": len(self.equations),
                "zero_entries": len(self.zero_indices), "monic_variables": len(self.variables),
                "target_orbit_dimension": len(self.columns)}


def discover(model, order, seed, timeout_ms, max_models, query_path):
    import z3
    solver = z3.Solver(); solver.set(random_seed=seed)
    x = [z3.BitVec(f"c{j}", 2) for j in range(len(model.variables))]
    zero, one = z3.BitVecVal(0,2), z3.BitVecVal(1,2)
    if order == 3:
        solver.add(*(v != 3 for v in x))
        def multiply(a,b):
            return z3.If(z3.Or(a == 0, b == 0), zero, z3.If(a == b, one, z3.BitVecVal(2,2)))
        def add(a,b):
            return z3.If(a == 0, b, z3.If(b == 0, a,
                        z3.If(a == b, z3.BitVecVal(3,2)-a, zero)))
    else:
        def multiply(a,b):
            a0,a1,b0,b1 = a&1,z3.LShR(a,1),b&1,z3.LShR(b,1)
            return ((a0&b0)^(a1&b1)) | (((a0&b1)^(a1&b0)^(a1&b1))<<1)
        add = lambda a,b: a ^ b
    coefficients = []
    for terms, wanted in model.equations:
        products = [reduce(multiply, (x[j] for j in term), one) for term in terms]
        coefficient = reduce(add, products, zero)
        coefficients.append(coefficient)
        solver.add(coefficient != 0 if wanted else coefficient == 0)
    targets = [coefficients[index] for index in model.target_indices]
    for relation in model.relations:
        sides = [[targets[i] for i,value in enumerate(relation) if value == sign] for sign in (1,-1)]
        solver.add(reduce(multiply, sides[0], one) == reduce(multiply, sides[1], one))
    query = solver.to_smt2()
    query_path.write_text(query)
    started = time.monotonic(); records = []; status = "not-started"; reason = None
    for index in range(max_models):
        remaining = timeout_ms-int(1000*(time.monotonic()-started))
        if remaining <= 0:
            status = "total-time-limit"
            break
        solver.set(timeout=remaining)
        answer = solver.check(); status = str(answer)
        if answer != z3.sat:
            if answer == z3.unknown:
                reason = solver.reason_unknown()
            break
        solution = solver.model()
        values = [solution.eval(v, model_completion=True).as_long() for v in x]
        check = model.replay(values, order)
        record = {"index": index, "coefficients": values, "verification": check}
        records.append(record)
        print("model", index, "rank", check["jacobian_rank"], flush=True)
        if check["nonsingular_hensel_premise"]:
            status = "nonsingular-certificate"
            break
        solver.add(z3.Or(*(v != value for v,value in zip(x,values))))
    return {"field_order": order, "seed": seed, "timeout_ms": timeout_ms,
            "max_models": max_models, "status": status, "reason_unknown": reason,
            "models": records, "elapsed_seconds": time.monotonic()-started,
            "solver_version": z3.get_version_string(),
            "query_sha256": hashlib.sha256(query.encode()).hexdigest()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, choices=(3,4), default=4)
    parser.add_argument("--seed", type=int, default=20261020)
    parser.add_argument("--timeout-ms", type=int, default=120000)
    parser.add_argument("--max-models", type=int, default=8)
    parser.add_argument("--structure-only", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    model = ExactModel()
    report = {"structure": model.structure(), "exact_solution_found": False, "improves_omega": False,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if not args.structure_only:
        report["discovery"] = discover(model, args.order, args.seed, args.timeout_ms,
                                        args.max_models, args.output.with_suffix(".smt2"))
        report["exact_solution_found"] = report["discovery"]["status"] == "nonsingular-certificate"
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print({k:v for k,v in report.items() if k not in ("structure",)}, flush=True)
