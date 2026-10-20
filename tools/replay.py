"""Replay the immutable research bundle without changing its archived files."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'research' / 'ai' / '2026-10-20'
DISPLAY_FIELDS = {'elapsed_seconds', 'ratio_float', 'ratio_to_a_4_over_3',
                  'diagonal_asymptotic_coefficient'}
RUNS = [
    ('profile_checks.json', ['verify_profile.py'], 'total_exact_grid_checks', 73856),
    ('product_filtration_checks.json', ['check_product_filtration.py', '--max-size', '12'],
     'exact_inequalities_checked', 353664),
    ('binary_search.json', ['search_degenerations.py', '--mode', 'binary', '--max-sum', '11',
     '--output', 'binary_search.json'], 'cases_tested', 12976),
    ('ternary_search.json', ['search_degenerations.py', '--mode', 'ternary', '--max-sum', '10',
     '--output', 'ternary_search.json'], 'cases_tested', 209692),
    ('random_search.json', ['search_degenerations.py', '--mode', 'random', '--samples', '20000',
     '--seed', '20261020', '--output', 'random_search.json'], 'cases_tested', 20000),
]


def check_manifest() -> dict[str, str]:
    """Reject changed or missing archive files before running any experiment."""
    manifest = json.loads((ARCHIVE / 'manifest.json').read_text())['sha256']
    for name, expected in manifest.items():
        path = ARCHIVE / name
        if path.parent != ARCHIVE or not path.is_file():
            raise ValueError(f'Invalid or missing archived path: {name}')
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f'Archive hash mismatch: {name}')
    return manifest


def exact_payload(value):
    """Remove display-only floats and timing, not witness flags or exact scores."""
    if isinstance(value, dict):
        return {key: exact_payload(item) for key, item in value.items()
                if key not in DISPLAY_FIELDS}
    if isinstance(value, list):
        return [exact_payload(item) for item in value]
    return value


def run(output: Path, timeout: float) -> dict:
    if sys.flags.optimize:
        raise RuntimeError('Do not run with -O or PYTHONOPTIMIZE: archived checks use assert.')
    if timeout <= 0:
        raise ValueError('timeout must be positive')
    import sympy
    if sympy.__version__ != '1.14.0':
        raise RuntimeError(f'SymPy 1.14.0 is required; found {sympy.__version__}')
    manifest = check_manifest()
    output = output.resolve()
    if output == ARCHIVE or ARCHIVE in output.parents:
        raise ValueError('Reports must not overwrite the immutable archive.')
    output.mkdir(parents=True, exist_ok=True)
    (output / 'summary.json').unlink(missing_ok=True)
    summary = {'status': 'passed', 'python': platform.python_version(),
               'sympy': sympy.__version__, 'platform': platform.platform(),
               'archive_files_verified': len(manifest), 'runs': [],
               'limits': 'Finite reproduction only. No independent proof review or Lean build.'}
    env = os.environ.copy()
    env['PYTHONHASHSEED'] = '0'
    start = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix='matmul-replay-') as directory:
        work = Path(directory)
        for name in manifest:
            if name.endswith('.py'):
                shutil.copy2(ARCHIVE / name, work / name)
        for filename, args, count_key, count_expected in RUNS:
            completed = subprocess.run([sys.executable, *args], cwd=work, env=env,
                                       text=True, capture_output=True, timeout=timeout)
            if completed.returncode:
                raise RuntimeError(f'{args[0]} failed:\n{completed.stdout}\n{completed.stderr}')
            path = work / filename
            actual = json.loads(path.read_text())
            expected = json.loads((ARCHIVE / filename).read_text())
            if actual[count_key] != count_expected:
                raise AssertionError(f'{filename}: unexpected coverage count')
            if actual.get('violations') or actual.get('exact_witnesses'):
                raise AssertionError(f'{filename}: a violation was found')
            if exact_payload(actual) != exact_payload(expected):
                raise AssertionError(f'{filename}: exact payload differs from the archive')
            shutil.copy2(path, output / filename)
            summary['runs'].append({'report': filename, count_key: actual[count_key],
                                    'exact_payload_matches_archive': True,
                                    'elapsed_seconds': actual['elapsed_seconds']})
            print(f'{filename}: passed ({actual[count_key]} {count_key})', flush=True)
    check_manifest()
    summary['elapsed_seconds'] = time.perf_counter() - start
    summary['total_weight_candidates'] = 12976 + 209692 + 20000
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'results' / 'local')
    parser.add_argument('--timeout', type=float, default=300,
                        help='Maximum seconds for each child process')
    args = parser.parse_args()
    try:
        run(args.output, args.timeout)
    except (OSError, ValueError, RuntimeError, AssertionError, subprocess.TimeoutExpired) as exc:
        parser.exit(1, f'Replay failed: {exc}\n')


if __name__ == '__main__':
    main()
