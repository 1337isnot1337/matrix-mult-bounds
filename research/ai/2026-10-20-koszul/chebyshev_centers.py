"""Exact two-row Chebyshev block enumeration; no new exponent is established."""
import argparse
import json
from pathlib import Path
import time


def centers(m, seconds=None):
    started = time.monotonic()
    by_permutation = {}
    nodes = 0
    for center in range(m):
        for second_y in range(max(0, center - m + 1), center + m):
            if second_y == center:
                continue

            def visit(permutation, used_z):
                nonlocal nodes
                nodes += 1
                if seconds is not None and nodes % 100000 == 0:
                    if time.monotonic() - started > seconds:
                        raise TimeoutError
                column = len(permutation) - 1
                degree = permutation[-1]
                used = set(permutation)
                choices = [center] if column == 0 else {center + degree, abs(center - degree)}
                for z in choices:
                    if z in used_z:
                        continue
                    first = {v for v in (abs(center - z), center + z) if v < m}
                    if degree not in first or any(v in used for v in first - {degree}):
                        continue
                    second = {v for v in (abs(second_y - z), second_y + z) if v < m}
                    for next_degree in second - used:
                        if any(v in used for v in second - {next_degree}):
                            continue
                        extended = permutation + (next_degree,)
                        if len(extended) == m:
                            if second - {next_degree}:
                                continue
                            by_permutation.setdefault(extended, set()).add(center)
                        else:
                            visit(extended, used_z + (z,))

            try:
                visit((0,), ())
            except TimeoutError:
                return {"m": m, "status": "timeout", "nodes": nodes,
                        "seconds": time.monotonic() - started}
    return {"m": m, "status": "complete", "nodes": nodes,
            "seconds": time.monotonic() - started,
            "orderings": [{"permutation": list(p), "centers": sorted(cs)}
                          for p, cs in sorted(by_permutation.items())]}


def summary(result):
    if result["status"] != "complete":
        return result
    natural = list(range(result["m"]))
    nonidentity = [item for item in result["orderings"] if item["permutation"] != natural]
    return {key: result[key] for key in ("m", "status", "nodes", "seconds")} | {
        "nonidentity_permutations": len(nonidentity),
        "multiple_center_examples": [item for item in nonidentity if len(item["centers"]) > 1][:5]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=38)
    parser.add_argument("--seconds-per-m", type=float)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    results = []
    for m in range(4, args.max_m + 1):
        result = centers(m, args.seconds_per_m)
        results.append(result)
        print(json.dumps(summary(result)), flush=True)
        if result["status"] != "complete":
            break
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"status": "finite exact enumeration, subject to written reduction",
                                      "new_exponent_established": False,
                                      "results": results}, indent=2) + "\n")
