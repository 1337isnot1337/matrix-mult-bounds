"""Full rectangular matrix target in a physical-compression discovery chart.

Every target top block is imposed exactly by linear elimination. All remaining
source coefficients are free, and the objective includes the complete tensor.
Floating point fits are discovery only and are not degeneration certificates.
"""

import argparse
from itertools import product
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize


HERE = Path(__file__).resolve().parent


class RectangularCompression:
    def __init__(self, a, b, vertices, seed=441011, frames=None):
        self.a, self.b = a, b
        self.vertices = tuple(vertices)
        self.physical = a * b
        self.long = a + b - 1
        self.source_dimension = self.physical * self.long
        self.dimensions = tuple(vertices[i] * vertices[(i + 1) % 3] for i in range(3))
        if max(vertices) > self.physical or max(self.dimensions) > self.source_dimension:
            raise ValueError("The selected compression cannot be surjective in this format")
        self.basis = np.zeros((self.source_dimension, self.physical, self.physical))
        for i, k, s in product(range(a), range(self.long), range(b)):
            for p in range(a):
                q = k - p
                if 0 <= q < b:
                    self.basis[(i * self.long + k) * b + s, i * b + q, p * b + s] = 1
        rng = np.random.default_rng(seed)
        self.frames = ([np.linalg.qr(rng.normal(size=(self.physical, self.physical)))[0]
                        for _ in range(3)] if frames is None else [np.asarray(g).copy() for g in frames])
        if len(self.frames) != 3 or any(g.shape != (self.physical, self.physical)
                                       or np.linalg.norm(g.conj().T @ g - np.eye(self.physical)) > 1e-10
                                       for g in self.frames):
            raise ValueError("Initial physical frames must be three unitary matrices")
        self.retractions = [self.frames[i][:, :vertices[i]].conj().T for i in range(3)]
        self.sections = [self.frames[i][:, :vertices[i]] for i in range(3)]
        self.base_coefficients, self.kernel_coefficients = [], []
        self.base_matrices, self.kernel_matrices = [], []
        self.singular_values, self.compressions = [], []
        for axis, dimension in enumerate(self.dimensions):
            linear = np.einsum('ip,cpq,qj->ijc', self.retractions[axis], self.basis,
                               self.sections[(axis + 1) % 3], optimize=True).reshape(dimension, self.source_dimension)
            left, values, right = np.linalg.svd(linear, full_matrices=True)
            if values[-1] <= 1e-12 * values[0]:
                raise ArithmeticError("The selected physical compression is not numerically surjective")
            base = ((right[:dimension].conj().T / values) @ left.conj().T).T
            kernel = right[dimension:].conj()
            self.base_coefficients.append(base)
            self.kernel_coefficients.append(kernel)
            self.base_matrices.append(np.einsum('ac,cij->aij', base, self.basis))
            self.kernel_matrices.append(np.einsum('kc,cij->kij', kernel, self.basis))
            self.singular_values.append(values)
            self.compressions.append(linear)
        self.fiber_dimensions = tuple(self.source_dimension - d for d in self.dimensions)
        self.sizes = tuple(d * f for d, f in zip(self.dimensions, self.fiber_dimensions))
        self.parameter_count = sum(self.sizes)
        self.target = np.zeros(self.dimensions)
        n0, n1, n2 = vertices
        for i, j, k in product(range(n0), range(n1), range(n2)):
            self.target[n1 * i + j, n2 * j + k, n0 * k + i] = 1
        self.target_norm_squared = n0 * n1 * n2
        self.seed = seed

    def split(self, parameter):
        if len(parameter) != self.parameter_count:
            raise ValueError("Incorrect number of complex fiber parameters")
        result, position = [], 0
        for dimension, fibers, size in zip(self.dimensions, self.fiber_dimensions, self.sizes):
            result.append(parameter[position:position + size].reshape(dimension, fibers))
            position += size
        return result

    def matrices(self, parameter):
        return [base + np.einsum('ak,kij->aij', fiber, kernel)
                for base, fiber, kernel in zip(self.base_matrices, self.split(parameter), self.kernel_matrices)]

    @staticmethod
    def pair_kernel(first, second):
        paired = np.einsum('bip,cpj->bcij', first, second, optimize=True)
        return paired.transpose(0, 1, 3, 2).reshape(len(first) * len(second), -1)

    def evaluate(self, parameter, gradient=True):
        matrices = self.matrices(parameter)
        pair0 = self.pair_kernel(matrices[1], matrices[2])
        image = (matrices[0].reshape(self.dimensions[0], -1) @ pair0.T).reshape(self.dimensions)
        residual = image - self.target
        loss = float(np.vdot(residual, residual).real / (2 * self.target_norm_squared))
        if not gradient:
            return loss, residual, matrices
        derivatives = []
        for axis in range(3):
            other = ((axis + 1) % 3, (axis + 2) % 3)
            pair = pair0 if axis == 0 else self.pair_kernel(matrices[other[0]], matrices[other[1]])
            cyclic_residual = residual.transpose(axis, *other).reshape(self.dimensions[axis], -1)
            matrix_gradient = cyclic_residual @ pair.conj() / self.target_norm_squared
            kernels = self.kernel_matrices[axis].reshape(self.fiber_dimensions[axis], -1)
            derivatives.append((matrix_gradient @ kernels.conj().T).ravel())
        return loss, np.concatenate(derivatives)

    def update_leg(self, parameter, axis, rcond=1e-12):
        matrices = self.matrices(parameter)
        other = ((axis + 1) % 3, (axis + 2) % 3)
        paired = self.pair_kernel(matrices[other[0]], matrices[other[1]])
        base_image = self.base_matrices[axis].reshape(self.dimensions[axis], -1) @ paired.T
        wanted = self.target.transpose(axis, *other).reshape(self.dimensions[axis], -1) - base_image
        design = self.kernel_matrices[axis].reshape(self.fiber_dimensions[axis], -1) @ paired.T
        solution = np.linalg.lstsq(design.T, wanted.T, rcond=rcond)[0].T
        changed = [x.copy() for x in self.split(parameter)]
        changed[axis] = solution
        return np.concatenate([x.ravel() for x in changed])

    def compression_error(self, parameter):
        errors = []
        for axis, (base, fibers, kernel) in enumerate(zip(self.base_coefficients, self.split(parameter), self.kernel_coefficients)):
            coefficients = base + fibers @ kernel
            errors.append(float(np.linalg.norm(self.compressions[axis] @ coefficients.T - np.eye(self.dimensions[axis]))
                                / np.sqrt(self.dimensions[axis])))
        return errors

    def summary(self, parameter):
        loss, residual, matrices = self.evaluate(parameter, False)
        return {"source_lengths": [self.a, self.b], "physical_matrix_size": self.physical,
                "target_vertices": list(self.vertices), "target_dimensions": list(self.dimensions),
                "source_leg_dimension": self.source_dimension,
                "fiber_dimensions_per_unit": list(self.fiber_dimensions),
                "complex_fiber_parameters": self.parameter_count,
                "fixed_physical_frame_seed": self.seed,
                "compression_condition_numbers": [float(s[0] / s[-1]) for s in self.singular_values],
                "relative_full_tensor_residual": float(np.sqrt(2 * loss)),
                "squared_target_norm": self.target_norm_squared,
                "complete_target_coefficients": int(np.prod(self.dimensions)),
                "top_block_relative_errors": self.compression_error(parameter),
                "fiber_parameter_norm": float(np.linalg.norm(parameter)),
                "physical_map_frobenius_norms": [float(np.linalg.norm(x)) for x in matrices],
                "numerical_discovery_only": True, "tensor_identity_certified": False,
                "new_exponent_established": False}


def controls():
    problem = RectangularCompression(2, 3, (2, 3, 2), 23322)
    rng = np.random.default_rng(42211)
    parameter = 0.02 * (rng.normal(size=problem.parameter_count) + 1j * rng.normal(size=problem.parameter_count))
    loss, gradient = problem.evaluate(parameter)
    direction = rng.normal(size=len(parameter)) + 1j * rng.normal(size=len(parameter))
    direction /= np.linalg.norm(direction)
    h = 1e-6
    numerical = (problem.evaluate(parameter + h * direction, False)[0]
                 - problem.evaluate(parameter - h * direction, False)[0]) / (2 * h)
    analytic = float(np.vdot(gradient, direction).real)
    derivative_error = abs(numerical - analytic) / max(1.0, abs(analytic))
    _, residual, _ = problem.evaluate(parameter, False)
    coefficients = [b + f @ k for b, f, k in zip(problem.base_coefficients, problem.split(parameter), problem.kernel_coefficients)]
    direct = np.zeros(problem.dimensions, dtype=complex)
    a, b, m = problem.a, problem.b, problem.long
    for i, j, p, q, r, s in product(range(a), range(b), range(a), range(b), range(a), range(b)):
        indices = ((i * m + p + q) * b + s, (p * m + r + s) * b + j, (r * m + i + j) * b + q)
        direct += np.einsum('a,b,c->abc', *(coefficients[axis][:, indices[axis]] for axis in range(3)))
    coefficient_error = float(np.linalg.norm(direct - problem.target - residual))
    updated = problem.update_leg(parameter, 1)
    updated_loss = problem.evaluate(updated, False)[0]
    other_blocks_fixed = all(np.array_equal(problem.split(parameter)[axis], problem.split(updated)[axis]) for axis in (0, 2))
    errors = problem.compression_error(parameter)
    complex_frames = [np.linalg.qr(rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6)))[0]
                      for _ in range(3)]
    complex_problem = RectangularCompression(2, 3, (2, 3, 2), frames=complex_frames)
    complex_errors = complex_problem.compression_error(np.zeros(complex_problem.parameter_count, dtype=complex))
    if derivative_error > 1e-7 or coefficient_error > 1e-9 or max(errors + complex_errors) > 1e-10:
        raise ArithmeticError("A full coefficient, derivative, or top-compression control failed")
    if updated_loss > loss + 1e-10 or not other_blocks_fixed:
        raise ArithmeticError("The exact single-leg least-squares update control failed")
    return {"source_lengths": [2, 3], "target_vertices": [2, 3, 2],
            "complete_source_terms_checked": a ** 3 * b ** 3,
            "complete_target_coefficients_checked": int(np.prod(problem.dimensions)),
            "complex_parameters": problem.parameter_count,
            "complex_directional_gradient_error": derivative_error,
            "full_source_coefficient_error": coefficient_error,
            "top_block_relative_errors": errors,
            "complex_unitary_frame_compression_errors": complex_errors,
            "loss_before_leg_update": loss, "loss_after_leg_update": updated_loss,
            "other_two_leg_parameter_blocks_unchanged": other_blocks_fixed,
            "complete_unmasked_objective": True,
            "numerical_control_only": True}


def run(a, b, vertices, seed, sweeps=0, iterations=0):
    problem = RectangularCompression(a, b, vertices, seed)
    rng = np.random.default_rng(seed + 1)
    parameter = 0.01 * (rng.normal(size=problem.parameter_count) + 1j * rng.normal(size=problem.parameter_count))
    started = time.monotonic()
    initial = problem.summary(parameter)
    print(json.dumps({"stage": "initial", **initial}), flush=True)
    history = []
    for sweep in range(sweeps):
        for axis in range(3):
            parameter = problem.update_leg(parameter, axis)
        loss = problem.evaluate(parameter, False)[0]
        history.append({"stage": "ALS", "sweep": sweep + 1, "relative_residual": float(np.sqrt(2 * loss))})
        print(json.dumps(history[-1]), flush=True)
    optimization = None
    if iterations:
        cached = {}
        callbacks = 0
        def objective(real_parameter):
            count = problem.parameter_count
            complex_parameter = real_parameter[:count] + 1j * real_parameter[count:]
            loss, derivative = problem.evaluate(complex_parameter)
            cached["loss"] = loss
            return loss, np.concatenate((derivative.real, derivative.imag))
        def callback(real_parameter):
            nonlocal callbacks
            callbacks += 1
            if callbacks == 1 or callbacks % 10 == 0:
                item = {"stage": "L-BFGS", "iteration": callbacks,
                        "relative_residual": float(np.sqrt(2 * cached["loss"])),
                        "seconds": round(time.monotonic() - started, 3)}
                history.append(item)
                print(json.dumps(item), flush=True)
        result = minimize(objective, np.concatenate((parameter.real, parameter.imag)), jac=True,
                          method="L-BFGS-B", callback=callback,
                          options={"maxiter": iterations, "maxls": 30, "ftol": 1e-13, "gtol": 1e-10, "maxcor": 20})
        count = problem.parameter_count
        parameter = result.x[:count] + 1j * result.x[count:]
        optimization = {"message": str(result.message), "iterations": int(result.nit), "evaluations": int(result.nfev)}
    return {"initial": initial, "final": problem.summary(parameter), "history": history,
            "optimizer": optimization, "elapsed_seconds": time.monotonic() - started}, parameter


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--source", default="4,4")
    parser.add_argument("--target", default="10,10,11")
    parser.add_argument("--seed", type=int, default=441011)
    parser.add_argument("--als-sweeps", type=int, default=0)
    parser.add_argument("--iterations", type=int, default=0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.controls:
        report = controls()
    else:
        a, b = map(int, args.source.split(","))
        vertices = tuple(map(int, args.target.split(",")))
        report, parameter = run(a, b, vertices, args.seed, args.als_sweeps, args.iterations)
        if args.output:
            np.savez_compressed(args.output.with_suffix(".npz"), parameters=parameter,
                                source=np.array([a, b]), vertices=np.array(vertices), seed=args.seed)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
