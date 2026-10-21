"""Replay exact S5 search circuits with the maintained group acceptance checks."""
import argparse
import importlib.util
import json
from pathlib import Path

from s5_source import data, NATIVE

spec = importlib.util.spec_from_file_location('s5_cover_search_replayer', NATIVE/'verify.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def replay(path):
    return helper.replay(path, data_provider=data, target_shape=(13, 14, 14))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    print(json.dumps(replay(args.report), indent=2))
