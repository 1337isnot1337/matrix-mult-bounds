"""Discovery census for all independent two-row / two-column deletions."""
import argparse
from collections import Counter
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import time

ROOT = Path.cwd()
PACKAGE = ROOT / 'research/ai/2026-10-23-conjugation-limit'


def load(name):
    spec = importlib.util.spec_from_file_location(name, PACKAGE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(shard, shards, output):
    verify = load('verify')
    blocks = load('block_reduction')
    matrices, labels, _ = blocks.build_blocks(verify)
    outer = [{28 * (position // 112 - 84) + position % 112: value
              for position, value in matrix.items()}
             for matrix, label in zip(matrices, labels)
             if label[0].startswith('lowest_')]
    pairs = list(combinations(range(28), 2))
    histogram = Counter()
    minimum = 47
    extremizers = []
    start = time.monotonic()
    for index, rows in enumerate(pairs):
        if index % shards != shard:
            continue
        row_projected = [{position: value for position, value in matrix.items()
                          if position // 28 not in rows} for matrix in outer]
        for columns in pairs:
            rank = verify.modular_rank(
                {position: value for position, value in matrix.items()
                 if position % 28 not in columns} for matrix in row_projected)
            histogram[rank] += 1
            if rank < minimum:
                minimum = rank
                extremizers = []
            if rank == minimum:
                extremizers.append([list(rows), list(columns)])
        if index % 50 == shard:
            print('row-pair', index, 'minimum', minimum, 'cases', sum(histogram.values()), flush=True)
    report = {'schema': 'a4-outer-coordinate-census-discovery-v1',
              'shard': shard, 'shards': shards, 'prime': verify.PRIME,
              'coordinate_size': 28, 'space_dimension': 46,
              'completed_pairs': sum(histogram.values()),
              'modular_rank_histogram': dict(sorted(histogram.items())),
              'minimum_modular_rank': minimum,
              'minimum_pairs': extremizers,
              'elapsed_seconds': time.monotonic() - start}
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'minimum_pairs'}), flush=True)


parser = argparse.ArgumentParser()
parser.add_argument('--shard', type=int, default=0)
parser.add_argument('--shards', type=int, default=1)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
run(args.shard, args.shards, args.output)
