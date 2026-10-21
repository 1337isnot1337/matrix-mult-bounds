"""Exact root14 Q(6,4) restriction used by the correction experiments."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "correction_nearfull_dependency",
    ROOT/"research/ai/2026-10-21-nearfull-quantum/quantum.py")
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)
q = base.q


def choices(leg):
    data = q.local_map(6, 4, leg)
    if leg == 0:
        selected = [j for j, (k, ell) in enumerate(data[1]) if k >= 1]
    else:
        selected = [j for j, (k, ell) in enumerate(data[1])
                    if k >= 2 or (k == 0 and 5 <= ell <= 6)
                    or (k == 1 and 3 <= ell <= 6)]
    return data, selected


def build():
    maps, records = [], []
    for leg in range(3):
        data, selected = choices(leg)
        field, matrix, record, generic = base.dvr_limit(data, selected, 14)
        maps.append(matrix)
        records.append(record)
    tensor = base.tensor(5, 4, maps, field)
    weights = [[2*row["weight"]-offset for row in records[axis]
                for _ in row["generic_rows"]]
               for axis, offset in enumerate([10, 11, 11])]
    assert [len(matrix) for matrix in maps] == [25, 20, 20]
    assert all(sum(weights[a][point[a]] for a in range(3)) == 0
               for point in tensor)
    return field, maps, records, tensor, weights
