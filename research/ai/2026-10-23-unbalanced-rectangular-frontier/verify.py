"""Exact ordinary single-rectangular screen for all cyclic sources N<=1377."""
from __future__ import annotations

import argparse
import importlib.util
import json
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "unbalanced_rectangular_hankel_controls",
    ROOT / "research/ai/2026-10-21-hankel-pencil-degree/verify.py",
)
controls = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(controls)


def source_formats():
    a = 2
    while a*a*(2*a-1) <= 1377:
        b = a
        while a*b*(a+b-1) <= 1377:
            yield a, b
            b += 1
        a += 1


def exclusion(a, b, shape):
    size = a*b*(a+b-1)
    for x, y, z in [shape, shape[1:]+shape[:1], shape[2:]+shape[:2]]:
        lift = z+2*size-z*(x+y)
        common = {"matrix_parameter_dimensions": [x, y], "slice_rank": z,
                  "lift_rank_upper_bound": lift, "block_parameter_dimension": x*y}
        if lift < a*b:
            return {"gate": "minimum_slice_rank", "required_rank": a*b, **common}
        if lift < 2*a*b and x*y > a*b:
            return {"gate": "polynomial_rank_locus", "required_rank": 2*a*b,
                    "dimension_cap": a*b, **common}
        for r in range(2, a):
            cap = controls.symbol_cap(a, b, r)
            if cap is not None and x*y > cap*a*b and lift < (r+1)*a*b:
                return {"gate": "hankel_linear_annihilator", "symbol_rank": r,
                        "symbol_image_cap": cap, "dimension_cap": cap*a*b,
                        "required_rank": (r+1)*a*b, **common}
    return None


def source_report(a, b):
    size = a*b*(a+b-1)
    threshold = (3*(a+b)-2)**4
    rows = []
    for l in range(1, isqrt(size)+1):
        for h in range(l, isqrt(size)+1):
            low = max(h, threshold//(216*l*h)+1)
            for n in range(low, size//h+1):
                shape = [l, h, n]
                witness = exclusion(a, b, shape)
                rows.append({"shape": shape, "leg_dimensions": [l*h, h*n, n*l],
                             "volume": l*h*n, "excluded": witness is not None,
                             "witness": witness})
    survivors = [row["shape"] for row in rows if not row["excluded"]]
    return {"source": [a, b], "source_leg_dimension": size,
            "improving_shapes": len(rows),
            "excluded_shapes": sum(row["excluded"] for row in rows),
            "survivors": survivors,
            "survivor_higher_rank_constraints": [
                higher_rank_constraint(a, b, shape) for shape in survivors
            ],
            "records": rows}


def higher_rank_constraint(a, b, shape):
    """Elementary source-rank bound, without a Segre-image dimension claim."""
    r = min(a, b)-1
    orientations = []
    for x, y, z in [shape, shape[1:]+shape[:1], shape[2:]+shape[:2]]:
        loss = 2*a*b*(a+b-1)-z*(x+y)
        k = min(x, y, max(0, ((r+1)*a*b-1-loss)//z))
        orientations.append({"matrix_parameter_dimensions": [x, y],
                             "slice_rank_multiplier": z, "long_leg_loss": loss,
                             "maximum_parameter_rank": k,
                             "lift_rank_upper_bound": k*z+loss,
                             "strict_source_rank_threshold": (r+1)*a*b,
                             "hankel_rank_upper_bound": r})
    return {"shape": shape, "orientations": orientations,
            "stronger_global_dimension_bound_proved": False}


def report():
    sources = [source_report(a, b) for a, b in source_formats()]
    sources.sort(key=lambda row: (row["source_leg_dimension"], row["source"]))
    return {
        "scope": "Ordinary complex restrictions to one rectangular matrix block; 2<=a<=b; ab(a+b-1)<=1377; sorted target shapes, all three cyclic slice orientations.",
        "source_count": len(sources), "maximum_source_dimension": 1377,
        "improving_shapes": sum(row["improving_shapes"] for row in sources),
        "excluded_shapes": sum(row["excluded_shapes"] for row in sources),
        "surviving_sources": [row["source"] for row in sources if row["survivors"]],
        "sources": sources,
        "survivors_are_constructions": False,
        "singular_degenerations_excluded": False,
        "independent_review": False, "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2)+"\n")
    print(f"Checked {data['source_count']} sources and {data['improving_shapes']} improving shapes; {data['excluded_shapes']} excluded.")
