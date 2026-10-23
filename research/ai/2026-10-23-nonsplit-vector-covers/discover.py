"""Bounded numerical discovery; exact hypergraph replay checks each candidate."""
import argparse
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_array

from cover_model import classes, edges, verify_block


def run(j, seconds, even_principal=False):
    counts = classes(j)
    labels = list(counts)
    index = {label: i for i, label in enumerate(labels)}
    rows, columns = [], []
    size = len(labels)
    edge_count = 0
    for edge_count, edge in enumerate(edges(j, even_principal), start=1):
        for leg, label in enumerate(edge):
            rows.append(edge_count-1)
            columns.append(leg*size+index[label])
    matrix = coo_array((np.ones(len(rows)),
                        (np.array(rows), np.array(columns))),
                       shape=(edge_count, 3*size)).tocsc()
    weights = np.array([counts[label] for _ in range(3) for label in labels], dtype=float)
    started = time.monotonic()
    result = milp(weights, integrality=np.ones(3*size), bounds=Bounds(0, 1),
                  constraints=LinearConstraint(matrix, 1, np.inf),
                  options={'time_limit': seconds, 'mip_rel_gap': 0})
    selected, replay = None, None
    if result.x is not None:
        selected = [[label for i, label in enumerate(labels)
                     if result.x[leg*size+i] > .5] for leg in range(3)]
        replay = verify_block(j, selected, even_principal)
    return {'status': 'bounded-discovery-only', 'principal_factors': j,
            'even_principal': even_principal,
            'seconds_limit': seconds, 'elapsed_seconds': time.monotonic()-started,
            'solver_status': int(result.status), 'solver_message': result.message,
            'objective_float': None if result.fun is None else float(result.fun),
            'dual_bound_float': None if result.x is None else float(result.mip_dual_bound),
            'selected_classes': selected, 'exact_cover_replay': replay,
            'optimality_certified': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--principal-factors', type=int, choices=range(4), required=True)
    parser.add_argument('--seconds', type=float, default=180)
    parser.add_argument('--even-principal', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run(args.principal_factors, args.seconds, args.even_principal)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'selected_classes'}))
