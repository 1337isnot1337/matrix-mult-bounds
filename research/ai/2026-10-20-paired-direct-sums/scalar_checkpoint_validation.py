"""Replay every completed scalar and tetrahedral numerical checkpoint.

This validates numerical experiment records.  It does not turn a
nonzero residual into a tensor certificate.
"""
import argparse
import importlib.util
import json
from pathlib import Path


def local(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name+".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(directory):
    import numpy as np
    narrow = local("narrow_scalar_search")
    tetra = local("tetrahedral_search")
    records = []
    for stem, scalars, expected_iterations in (
            ("narrow-scalar-q3", 1, 1000), ("tetrahedral-p3", 0, 1200),
            ("tetrahedral-p3-scalar", 1, 1200), ("tetrahedral-reduced", 1, 1600)):
        for seed in range(4):
            name = f"{stem}-seed{seed}"
            report = json.loads((directory/(name+".json")).read_text())
            point = json.loads((directory/(name+"-checkpoint.json")).read_text())
            if report["iterations_completed"] != expected_iterations:
                raise ArithmeticError("A declared complete search did not finish its budget")
            if stem == "narrow-scalar-q3":
                shape, terms, target_shape, target_terms = narrow.coordinates(3, 2, 1)
                terms = {term: 1 for term in terms}
                target_terms = {term: 1 for term in target_terms}
                maps = [np.asarray(point[f"map_{k}"]) for k in range(3)]
            else:
                shape, target_shape = (9+scalars, 15+scalars, 15+scalars), (9, 9, 9)
                terms, target_terms = tetra.source_terms(scalars), tetra.target_terms()
                maps = [np.asarray(matrix) for matrix in point["maps_in_cartesian_source_coordinates"]]
            if any(matrix.shape != (target_shape[k], shape[k]) or not np.isfinite(matrix).all()
                   for k, matrix in enumerate(maps)):
                raise ArithmeticError("A checkpoint has invalid map data")
            full, target = np.zeros(target_shape), np.zeros(target_shape)
            for term, value in terms.items():
                full += value*np.einsum("i,j,k->ijk", *(maps[k][:, term[k]] for k in range(3)))
            for term, value in target_terms.items():
                target[term] = value
            error = float(np.linalg.norm(full-target)/np.linalg.norm(target))
            expected = report["best_relative_coefficient_error"]
            difference = abs(error-expected)
            if difference > 5e-12:
                raise ArithmeticError("A checkpoint does not reproduce its reported best residual")
            row = {"checkpoint": name+"-checkpoint.json", "completed_iterations": expected_iterations,
                   "full_coefficient_positions": int(np.prod(target_shape)),
                   "replayed_relative_coefficient_error": error,
                   "reported_best_relative_coefficient_error": expected,
                   "absolute_metric_difference": difference}
            if stem == "tetrahedral-reduced":
                diagonal_error = float(np.max(np.abs((full-target)[np.ix_([0,4,8], [0,4,8], [0,4,8])])))
                if diagonal_error != 0:
                    raise ArithmeticError("A fixed diagonal sector was changed")
                row["fixed_diagonal_sector_maximum_error"] = diagonal_error
            records.append(row)
    return {"checkpoint_count": len(records), "all_checkpoints_replayed": True,
            "maximum_absolute_metric_difference": max(row["absolute_metric_difference"] for row in records),
            "checkpoints": records, "scope": "Completed numerical experiments only; no matrix tensor certificate.",
            "improves_omega": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = validate(args.directory)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items() if key != "checkpoints"}, indent=2))
