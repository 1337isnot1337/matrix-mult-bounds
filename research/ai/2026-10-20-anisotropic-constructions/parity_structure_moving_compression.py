"""Moving physical splittings with an exact rectangular compression constraint.

This optional NumPy/SciPy discovery program differentiates through the full
compression solve. Its loss contains every target tensor coefficient. A small
floating point residual is not an exact restriction or degeneration witness.
"""

import argparse
from itertools import product
import json
from pathlib import Path
import time

import numpy as np
from scipy.linalg import qr
from scipy.optimize import minimize

from parity_structure_rectangular_compression import RectangularCompression


class MovingCompression:
    def __init__(self, fixed, initial_fibers=None):
        self.fixed = fixed
        self.vertices = fixed.vertices
        self.dimensions = fixed.dimensions
        self.target = fixed.target
        self.basis = fixed.basis
        self.physical = fixed.physical
        self.source_dimension = fixed.source_dimension
        self.target_norm_squared = fixed.target_norm_squared
        if initial_fibers is None:
            initial_fibers = np.zeros(fixed.parameter_count, dtype=complex)
        initial = [b + f @ k for b, f, k in
                   zip(fixed.base_coefficients, fixed.split(initial_fibers), fixed.kernel_coefficients)]
        self.pivots, self.free_columns, self.free_origins, self.free_scales = [], [], [], []
        for axis, dimension in enumerate(self.dimensions):
            _, _, ordering = qr(fixed.compressions[axis], mode="economic", pivoting=True)
            pivots = np.array(ordering[:dimension])
            free = np.array(sorted(set(range(self.source_dimension)) - set(pivots)))
            origin = initial[axis][:, free].copy()
            self.pivots.append(pivots)
            self.free_columns.append(free)
            self.free_origins.append(origin)
            self.free_scales.append(max(1.0, float(np.linalg.norm(origin) / np.sqrt(origin.size))))
        self.free_shapes = [x.shape for x in self.free_origins]
        self.splitting_shapes = [(n, self.physical - n) for n in self.vertices]
        self.parameter_count = sum(x.size for x in self.free_origins) + 2 * sum(n * r for n, r in self.splitting_shapes)
        self.frame_inverses = [g.conj().T for g in fixed.frames]

    def split(self, parameter):
        if len(parameter) != self.parameter_count:
            raise ValueError("Incorrect moving-compression parameter count")
        cursor, free, es, fs = 0, [], [], []
        for origin, scale in zip(self.free_origins, self.free_scales):
            free.append(origin + scale * parameter[cursor:cursor + origin.size].reshape(origin.shape))
            cursor += origin.size
        for n, r in self.splitting_shapes:
            es.append(parameter[cursor:cursor + n * r].reshape(n, r))
            cursor += n * r
            fs.append(parameter[cursor:cursor + n * r].reshape(r, n))
            cursor += n * r
        return free, es, fs

    def state(self, parameter):
        free, es, fs = self.split(parameter)
        retractions, sections, frames = [], [], []
        for g, inverse, e, f, n in zip(self.fixed.frames, self.frame_inverses, es, fs, self.vertices):
            r = self.physical - n
            sections.append(g @ np.concatenate((np.eye(n), f), axis=0))
            retractions.append(np.concatenate((np.eye(n) + e @ f, -e), axis=1) @ inverse)
            frames.append(g @ np.block([[np.eye(n), e], [f, np.eye(r) + f @ e]]))
        linears, pivot_linears, coefficients, matrices = [], [], [], []
        for axis, dimension in enumerate(self.dimensions):
            linear = np.einsum('ip,cpq,qj->ijc', retractions[axis], self.basis,
                               sections[(axis + 1) % 3], optimize=True).reshape(dimension, self.source_dimension)
            pivot_linear = linear[:, self.pivots[axis]]
            pivot_coefficients = np.linalg.solve(pivot_linear, np.eye(dimension) - linear[:, self.free_columns[axis]] @ free[axis].T).T
            coefficient = np.zeros((dimension, self.source_dimension), dtype=complex)
            coefficient[:, self.pivots[axis]] = pivot_coefficients
            coefficient[:, self.free_columns[axis]] = free[axis]
            linears.append(linear)
            pivot_linears.append(pivot_linear)
            coefficients.append(coefficient)
            matrices.append(np.einsum('ac,cij->aij', coefficient, self.basis, optimize=True))
        return {"free": free, "e": es, "f": fs, "r": retractions, "t": sections,
                "frames": frames, "linears": linears, "pivot_linears": pivot_linears,
                "coefficients": coefficients, "matrices": matrices}

    def evaluate(self, parameter, gradient=True, mode="raw"):
        state = self.state(parameter)
        matrices = state["matrices"]
        pair0 = self.fixed.pair_kernel(matrices[1], matrices[2])
        image = (matrices[0].reshape(self.dimensions[0], -1) @ pair0.T).reshape(self.dimensions)
        residual = image - self.target
        loss = float(np.vdot(residual, residual).real / (2 * self.target_norm_squared))
        if mode == "normalized":
            image_norm_squared = float(np.vdot(image, image).real)
            overlap = np.vdot(self.target, image)
            if abs(overlap) < 1e-200 or image_norm_squared < 1e-200:
                raise FloatingPointError("The actual target normalization is undefined")
            loss = float(0.5 * np.log(image_norm_squared * self.target_norm_squared / abs(overlap) ** 2))
            image_adjoint = image / image_norm_squared - self.target / overlap.conjugate()
        elif mode == "raw":
            image_adjoint = residual / self.target_norm_squared
        else:
            raise ValueError("Unknown full-coefficient objective")
        if not gradient:
            return loss, residual, state
        free_gradients, linear_gradients = [], []
        for axis in range(3):
            other = ((axis + 1) % 3, (axis + 2) % 3)
            pair = pair0 if axis == 0 else self.fixed.pair_kernel(matrices[other[0]], matrices[other[1]])
            cyclic_adjoint = image_adjoint.transpose(axis, *other).reshape(self.dimensions[axis], -1)
            matrix_gradient = cyclic_adjoint @ pair.conj()
            coefficient_gradient = matrix_gradient @ self.basis.reshape(self.source_dimension, -1).conj().T
            pivot_gradient = coefficient_gradient[:, self.pivots[axis]]
            elimination = np.linalg.solve(state["pivot_linears"][axis], state["linears"][axis][:, self.free_columns[axis]])
            free_gradient = coefficient_gradient[:, self.free_columns[axis]] - pivot_gradient @ elimination.conj()
            free_gradients.append((self.free_scales[axis] * free_gradient).ravel())
            linear_gradient = -np.linalg.solve(state["pivot_linears"][axis].conj().T, pivot_gradient.T) @ state["coefficients"][axis].conj()
            linear_gradients.append(linear_gradient.reshape(self.vertices[axis], self.vertices[(axis + 1) % 3], self.source_dimension))
        retraction_gradients = [np.zeros_like(r) for r in state["r"]]
        section_gradients = [np.zeros_like(t) for t in state["t"]]
        for axis in range(3):
            following = (axis + 1) % 3
            right = np.einsum('cpq,qj->cpj', self.basis, state["t"][following], optimize=True)
            left = np.einsum('ip,cpq->ciq', state["r"][axis], self.basis, optimize=True)
            retraction_gradients[axis] += np.einsum('ijc,cpj->ip', linear_gradients[axis], right.conj(), optimize=True)
            section_gradients[following] += np.einsum('ciq,ijc->qj', left.conj(), linear_gradients[axis], optimize=True)
        splitting_gradients = []
        for axis, (n, r) in enumerate(self.splitting_shapes):
            inverse = self.frame_inverses[axis]
            e, f = state["e"][axis], state["f"][axis]
            lower = np.concatenate((f, -np.eye(r)), axis=1) @ inverse
            e_gradient = retraction_gradients[axis] @ lower.conj().T
            f_gradient = self.fixed.frames[axis][:, n:].conj().T @ section_gradients[axis]
            f_gradient += e.conj().T @ retraction_gradients[axis] @ inverse[:n].conj().T
            splitting_gradients.extend((e_gradient.ravel(), f_gradient.ravel()))
        return loss, np.concatenate(free_gradients + splitting_gradients)

    def summary(self, parameter):
        loss, residual, state = self.evaluate(parameter, False)
        image = residual + self.target
        image_norm_squared = float(np.vdot(image, image).real)
        mean = np.vdot(self.target, image) / self.target_norm_squared
        correlation = float(abs(mean) * np.sqrt(self.target_norm_squared / image_norm_squared))
        normalization = 1 / mean if mean else complex(float("inf"))
        normalized_residual = float(np.linalg.norm(image / mean - self.target) / np.sqrt(self.target_norm_squared)) if mean else float("inf")
        normalized_coefficients = [normalization * state["coefficients"][0]] + state["coefficients"][1:]
        coefficient_sv = [np.linalg.svd(x, compute_uv=False) for x in state["coefficients"]]
        frame_sv = [np.linalg.svd(x, compute_uv=False) for x in state["frames"]]
        compression_sv = [np.linalg.svd(x, compute_uv=False) for x in state["linears"]]
        return {"source_lengths": [self.fixed.a, self.fixed.b], "target_vertices": list(self.vertices),
                "source_leg_dimension": self.source_dimension, "target_dimensions": list(self.dimensions),
                "complex_parameters": self.parameter_count,
                "complex_splitting_parameters": self.parameter_count - self.fixed.parameter_count,
                "relative_full_tensor_residual": float(np.sqrt(2 * loss)),
                "actual_target_coefficient_mean": [float(mean.real), float(mean.imag)],
                "target_correlation": correlation,
                "positive_target_normalized_full_residual": normalized_residual,
                "positive_target_normalization_on_first_leg": [float(normalization.real), float(normalization.imag)],
                "image_norm_squared": image_norm_squared,
                "complete_target_coefficients": int(np.prod(self.dimensions)),
                "physical_map_frobenius_norms": [float(np.linalg.norm(x)) for x in state["matrices"]],
                "source_coefficient_frobenius_norms": [float(np.linalg.norm(x)) for x in state["coefficients"]],
                "positively_normalized_source_coefficient_frobenius_norms": [float(np.linalg.norm(x)) for x in normalized_coefficients],
                "source_coefficient_smallest_singular_values": [float(x[-1]) for x in coefficient_sv],
                "source_coefficient_singular_value_ratios": [float(x[-1] / x[0]) for x in coefficient_sv],
                "physical_frame_smallest_singular_values": [float(x[-1]) for x in frame_sv],
                "physical_frame_largest_singular_values": [float(x[0]) for x in frame_sv],
                "compression_smallest_singular_values": [float(x[-1]) for x in compression_sv],
                "compression_condition_numbers": [float(x[0] / x[-1]) for x in compression_sv],
                "top_block_relative_errors": [float(np.linalg.norm(l @ c.T - np.eye(d)) / np.sqrt(d))
                                               for l, c, d in zip(state["linears"], state["coefficients"], self.dimensions)],
                "section_retraction_errors": [float(np.linalg.norm(r @ t - np.eye(n)))
                                               for r, t, n in zip(state["r"], state["t"], self.vertices)],
                "splitting_parameter_norms": [float(np.hypot(np.linalg.norm(e), np.linalg.norm(f)))
                                              for e, f in zip(state["e"], state["f"])],
                "numerical_discovery_only": True, "tensor_identity_certified": False,
                "new_exponent_established": False}

    def rechart_pivots(self, parameter):
        """Select new source pivots while preserving the current physical maps."""
        state = self.state(parameter)
        for axis, dimension in enumerate(self.dimensions):
            _, _, ordering = qr(state["linears"][axis], mode="economic", pivoting=True)
            pivots = np.array(ordering[:dimension])
            free = np.array(sorted(set(range(self.source_dimension)) - set(pivots)))
            origin = state["coefficients"][axis][:, free].copy()
            self.pivots[axis] = pivots
            self.free_columns[axis] = free
            self.free_origins[axis] = origin
            self.free_scales[axis] = max(1.0, float(np.linalg.norm(origin) / np.sqrt(origin.size)))
        parameter = np.concatenate([np.zeros(sum(x.size for x in self.free_origins), dtype=complex)]
                                   + [v.ravel() for pair in zip(state["e"], state["f"]) for v in pair])
        changed = self.state(parameter)
        error = max(float(np.linalg.norm(a - b) / max(1.0, np.linalg.norm(a)))
                    for a, b in zip(state["coefficients"], changed["coefficients"]))
        if error > 1e-8:
            raise ArithmeticError("Changing source pivots did not preserve the physical maps")
        return parameter, error

    def normalized_leg_update(self, parameter, axis, rcond=1e-12):
        """Exact least-squares projection, including one shared output scale.

The current image b and all selected-leg fiber directions span a linear
space. Projecting the full matrix target onto that space maximizes its
correlation with the target. A nonzero common scale recovers this chart.
"""
        state = self.state(parameter)
        other = ((axis + 1) % 3, (axis + 2) % 3)
        pair = self.fixed.pair_kernel(state["matrices"][other[0]], state["matrices"][other[1]])
        base = state["matrices"][axis].reshape(self.dimensions[axis], -1) @ pair.T
        wanted = self.target.transpose(axis, *other).reshape(self.dimensions[axis], -1)
        eliminated = np.linalg.solve(state["pivot_linears"][axis], state["linears"][axis][:, self.free_columns[axis]])
        fibers = len(self.free_columns[axis])
        kernel = np.zeros((fibers, self.source_dimension), dtype=complex)
        kernel[:, self.free_columns[axis]] = np.eye(fibers)
        kernel[:, self.pivots[axis]] = -eliminated.T
        physical_kernel = kernel @ self.basis.reshape(self.source_dimension, -1)
        design = physical_kernel @ pair.T
        joined = np.concatenate((base.T, wanted.T), axis=1)
        fitted = np.linalg.lstsq(design.T, joined, rcond=rcond)[0].T
        base_fitted, wanted_fitted = np.split(fitted, 2)
        base_perpendicular = base - base_fitted @ design
        wanted_perpendicular = wanted - wanted_fitted @ design
        denominator = float(np.vdot(base_perpendicular, base_perpendicular).real)
        scale = np.vdot(base_perpendicular, wanted_perpendicular) / denominator
        if abs(scale) < 1e-14:
            raise ArithmeticError("The best leg projection is on the zero-scale boundary; export a Laurent chart explicitly")
        step = (wanted_fitted - scale * base_fitted) / scale / self.free_scales[axis]
        result = parameter.copy()
        cursor = sum(self.free_origins[i].size for i in range(axis))
        result[cursor:cursor + step.size] += step.ravel()
        return result, complex(scale)


def controls():
    fixed = RectangularCompression(2, 3, (2, 3, 2), 23322)
    problem = MovingCompression(fixed)
    rng = np.random.default_rng(331101)
    parameter = 0.03 * (rng.normal(size=problem.parameter_count) + 1j * rng.normal(size=problem.parameter_count))
    checks = []
    slices = [slice(0, fixed.parameter_count), slice(fixed.parameter_count, None), slice(None)]
    for mode in ("raw", "normalized"):
        loss, gradient = problem.evaluate(parameter, mode=mode)
        for selected in slices:
            direction = np.zeros_like(parameter)
            direction[selected] = rng.normal(size=direction[selected].size) + 1j * rng.normal(size=direction[selected].size)
            direction /= np.linalg.norm(direction)
            h = 1e-6
            numerical = (problem.evaluate(parameter + h * direction, False, mode)[0]
                         - problem.evaluate(parameter - h * direction, False, mode)[0]) / (2 * h)
            analytic = float(np.vdot(gradient, direction).real)
            checks.append({"mode": mode, "finite_difference": numerical, "analytic": analytic,
                           "relative_error": abs(numerical - analytic) / max(1, abs(analytic))})
    _, residual, state = problem.evaluate(parameter, False)
    direct = np.zeros(problem.dimensions, dtype=complex)
    a, b, m = fixed.a, fixed.b, fixed.long
    for i, j, p, q, r, s in product(range(a), range(b), range(a), range(b), range(a), range(b)):
        indices = ((i * m + p + q) * b + s, (p * m + r + s) * b + j, (r * m + i + j) * b + q)
        direct += np.einsum('a,b,c->abc', *(state["coefficients"][axis][:, indices[axis]] for axis in range(3)))
    coefficient_error = float(np.linalg.norm(direct - problem.target - residual))
    summary = problem.summary(parameter)
    normalized = (direct / complex(*summary["actual_target_coefficient_mean"]))
    positive_mean_error = float(abs(np.vdot(problem.target, normalized) / problem.target_norm_squared - 1))
    permutation = np.eye(4)[:, [1, 2, 0, 3]]
    positive_fixed = RectangularCompression(2, 2, (2, 2, 2), frames=[permutation] * 3)
    positive = MovingCompression(positive_fixed)
    positive_loss, positive_gradient = positive.evaluate(np.zeros(positive.parameter_count, dtype=complex))
    before_update = problem.evaluate(parameter, False, "normalized")[0]
    updated, update_scale = problem.normalized_leg_update(parameter, 1)
    after_update = problem.evaluate(updated, False, "normalized")[0]
    _, before_es, before_fs = problem.split(parameter)
    _, after_es, after_fs = problem.split(updated)
    splittings_fixed = all(np.array_equal(a, b) for a, b in zip(before_es + before_fs, after_es + after_fs))
    recharted, rechart_error = problem.rechart_pivots(parameter)
    recharted_loss = problem.evaluate(recharted, False, "normalized")[0]
    if max(x["relative_error"] for x in checks) > 1e-7 or coefficient_error > 1e-9:
        raise ArithmeticError("Full moving-compression coefficient or gradient control failed")
    if max(summary["top_block_relative_errors"] + summary["section_retraction_errors"]) > 1e-10 or positive_mean_error > 1e-10:
        raise ArithmeticError("A physical splitting or compression identity failed")
    if abs(positive_loss) > 1e-20 or np.linalg.norm(positive_gradient) > 1e-10:
        raise ArithmeticError("The exact M2 control was not recovered by the numerical chart")
    if after_update > before_update + 1e-10 or not splittings_fixed or abs(recharted_loss - before_update) > 1e-10:
        raise ArithmeticError("A normalized leg projection or unchanged-map rechart control failed")
    return {"source_lengths": [a, b], "target_vertices": list(problem.vertices),
            "complete_source_terms_checked": a ** 3 * b ** 3,
            "complete_target_coefficients_checked": int(np.prod(problem.dimensions)),
            "complex_parameters": problem.parameter_count,
            "gradient_checks_order": ["fibers", "moving_splittings", "all_parameters"],
            "gradient_checks": checks, "full_source_coefficient_error": coefficient_error,
            "positive_target_normalization_error": positive_mean_error,
            "known_M2_control_loss": float(positive_loss),
            "known_M2_control_gradient_norm": float(np.linalg.norm(positive_gradient)),
            "normalized_objective_before_leg_update": before_update,
            "normalized_objective_after_leg_update": after_update,
            "normalized_leg_update_scale": [update_scale.real, update_scale.imag],
            "normalized_leg_update_preserves_physical_splittings": splittings_fixed,
            "pivot_rechart_coefficient_error": rechart_error,
            "top_block_relative_errors": summary["top_block_relative_errors"],
            "section_retraction_errors": summary["section_retraction_errors"],
            "numerical_control_only": True}


def run(a, b, vertices, seed, initial_path=None, iterations=0, resume_path=None, mode="raw", rechart=False, sweeps=0):
    fixed = RectangularCompression(a, b, vertices, seed)
    initial_fibers = None
    if initial_path:
        data = np.load(initial_path)
        if tuple(data["source"]) != (a, b) or tuple(data["vertices"]) != tuple(vertices) or int(data["seed"]) != seed:
            raise ValueError("The initial fibers use a different source, target, or physical frame")
        initial_fibers = data["parameters"]
    problem = MovingCompression(fixed, initial_fibers)
    parameter = np.zeros(problem.parameter_count, dtype=complex)
    if resume_path:
        data = np.load(resume_path)
        if tuple(data["source"]) != (a, b) or tuple(data["vertices"]) != tuple(vertices) or int(data["seed"]) != seed:
            raise ValueError("The moving checkpoint uses a different source, target, or base frame")
        parameter = data["parameters"].copy()
        problem.free_origins = [data[f"free_origin_{i}"].copy() for i in range(3)]
        problem.free_columns = [data[f"free_columns_{i}"].copy() for i in range(3)]
        problem.pivots = [data[f"pivots_{i}"].copy() for i in range(3)]
        problem.free_scales = list(data["free_scales"])
    rechart_error = None
    if rechart:
        parameter, rechart_error = problem.rechart_pivots(parameter)
    initial = problem.summary(parameter)
    print(json.dumps({"stage": "initial", **initial}), flush=True)
    history, cached = [], {}
    started = time.monotonic()
    callbacks = 0
    for sweep in range(sweeps):
        scales = []
        for axis in range(3):
            parameter, scale = problem.normalized_leg_update(parameter, axis)
            scales.append([scale.real, scale.imag])
        item = {"stage": "normalized ALS", "sweep": sweep + 1,
                "seconds": round(time.monotonic() - started, 3), "projection_scales": scales,
                **problem.summary(parameter)}
        history.append(item)
        print(json.dumps(item), flush=True)
    def objective(real_parameter):
        count = problem.parameter_count
        complex_parameter = real_parameter[:count] + 1j * real_parameter[count:]
        loss, derivative = problem.evaluate(complex_parameter, mode=mode)
        cached["loss"] = loss
        # A monotone transformation changes no zero or stationary point, and
        # keeps the first ill-conditioned point within a manageable scale.
        if mode == "raw":
            return np.log1p(loss), np.concatenate((derivative.real, derivative.imag)) / (1 + loss)
        return loss, np.concatenate((derivative.real, derivative.imag))
    def callback(real_parameter):
        nonlocal callbacks
        callbacks += 1
        if callbacks == 1 or callbacks % 10 == 0:
            count = problem.parameter_count
            complex_parameter = real_parameter[:count] + 1j * real_parameter[count:]
            item = {"stage": "L-BFGS", "iteration": callbacks,
                    "seconds": round(time.monotonic() - started, 3), **problem.summary(complex_parameter)}
            history.append(item)
            print(json.dumps(item), flush=True)
    optimization = None
    if iterations:
        result = minimize(objective, np.concatenate((parameter.real, parameter.imag)), jac=True,
                          method="L-BFGS-B", callback=callback,
                          options={"maxiter": iterations, "maxls": 30, "ftol": 1e-13, "gtol": 1e-10, "maxcor": 20})
        count = problem.parameter_count
        parameter = result.x[:count] + 1j * result.x[count:]
        optimization = {"message": str(result.message), "iterations": int(result.nit), "evaluations": int(result.nfev)}
    report = {"initial": initial, "final": problem.summary(parameter), "history": history,
              "optimizer": optimization, "objective_mode": mode,
              "objective_transform": ("log(1 + squared_relative_residual / 2)" if mode == "raw"
                                      else "0.5 log(image_norm_squared * target_norm_squared / squared_overlap)"),
              "initial_fixed_fibers": str(initial_path) if initial_path else None,
              "resumed_moving_checkpoint": str(resume_path) if resume_path else None,
              "pivot_rechart_coefficient_error": rechart_error,
              "elapsed_seconds": time.monotonic() - started}
    return report, parameter, problem


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--source", default="4,4")
    parser.add_argument("--target", default="10,10,11")
    parser.add_argument("--seed", type=int, default=441011)
    parser.add_argument("--initial-fixed-fibers", type=Path)
    parser.add_argument("--resume-moving", type=Path)
    parser.add_argument("--objective", choices=("raw", "normalized"), default="raw")
    parser.add_argument("--rechart-pivots", action="store_true")
    parser.add_argument("--normalized-als-sweeps", type=int, default=0)
    parser.add_argument("--iterations", type=int, default=0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.controls:
        report = controls()
    else:
        a, b = map(int, args.source.split(","))
        vertices = tuple(map(int, args.target.split(",")))
        report, parameter, problem = run(a, b, vertices, args.seed, args.initial_fixed_fibers,
                                         args.iterations, args.resume_moving, args.objective,
                                         args.rechart_pivots, args.normalized_als_sweeps)
        if args.output:
            state = problem.state(parameter)
            np.savez_compressed(args.output.with_suffix(".npz"), parameters=parameter,
                                source=np.array([a, b]), vertices=np.array(vertices), seed=args.seed,
                                **{f"coefficients_{i}": state["coefficients"][i] for i in range(3)},
                                **{f"frame_{i}": state["frames"][i] for i in range(3)},
                                **{f"free_origin_{i}": problem.free_origins[i] for i in range(3)},
                                **{f"free_columns_{i}": problem.free_columns[i] for i in range(3)},
                                **{f"pivots_{i}": problem.pivots[i] for i in range(3)},
                                free_scales=np.array(problem.free_scales))
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
