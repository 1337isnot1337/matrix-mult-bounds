"""Select conservative package-level regression tests from a Git diff.

Unknown executable/data changes fall back to the full suite. This is a
routing aid, not a mathematical dependency proof. Nightly CI tests all files.
"""
from __future__ import annotations
import argparse
import ast
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CORE = 'test_research.py'
ARCHIVES = ('research/ai/2026-10-20/', 'research/ai/2026-10-20-session2/')


def package(path):
    parts = Path(path).parts
    return '/'.join(parts[:3]) if len(parts) >= 4 and parts[:2] == ('research', 'ai') else None


def select(root, changed, force_full=False):
    root = Path(root)
    tests = sorted(p.name for p in (root / 'tests').glob('test_*.py'))
    changed = sorted(set(changed))
    full = force_full
    replay = force_full
    reasons = []
    selected = {CORE} if CORE in tests else set()
    pyfiles = sorted(root.glob('research/ai/**/*.py')) + sorted(root.glob('tests/test_*.py'))
    texts = {str(p.relative_to(root)): p.read_text() for p in pyfiles}
    packages = {package(p) for p in texts if package(p)}
    stems = {}
    for path in texts:
        stems.setdefault(Path(path).stem, set()).add(path)
    dependencies = {p: {p} for p in texts}
    for path, text in texts.items():
        # Directory literals also capture split Path expressions and dynamic loaders.
        for pkg in packages:
            if Path(pkg).name in text:
                dependencies[path].update(p for p in texts if package(p) == pkg)
        try:
            tree = ast.parse(text)
        except SyntaxError:
            full = True
            reasons.append('Unparseable Python: ' + path)
            continue
        modules = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.extend(x.name.split('.')[0] for x in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.append(node.module.split('.')[0])
        for module in modules:
            candidates = stems.get(module, set())
            local = {p for p in candidates if Path(p).parent == Path(path).parent}
            dependencies[path].update(local or candidates)
    closure = {}
    for test in tests:
        todo = ['tests/' + test]
        reached = set()
        while todo:
            path = todo.pop()
            if path not in reached:
                reached.add(path)
                todo.extend(dependencies.get(path, ()))
        closure[test] = reached
    for path in changed:
        if path.startswith(ARCHIVES):
            full = replay = True
            reasons.append('Archived source changed: ' + path)
            continue
        if path == 'requirements.txt' or path.startswith('tools/'):
            full = replay = True
            reasons.append('Shared tooling/dependencies changed: ' + path)
            continue
        if path.startswith('.github/') or path == 'tests/__init__.py':
            full = True
            reasons.append('CI configuration changed: ' + path)
            continue
        if path.endswith('.md') or path in ('LICENSE', '.gitignore', 'research/claims.json', 'references/sources.json'):
            continue
        if path.startswith('tests/') and Path(path).name in tests:
            selected.add(Path(path).name)
            continue
        pkg = package(path)
        owners = set()
        for test, reached in closure.items():
            if pkg and any(package(p) == pkg for p in reached):
                owners.add(test)
            elif not pkg:
                # Saved certificates can live outside their source package.
                tokens = tuple(x for x in (path, Path(path).parent.name, Path(path).name) if x and x != '.')
                if any(any(token in texts.get(p, '') for token in tokens) for p in reached):
                    owners.add(test)
        if owners:
            selected.update(owners)
        else:
            full = True
            reasons.append('No known test owner; full fallback: ' + path)
    if force_full:
        reasons.append('Scheduled or manual full verification')
    return {'full': full, 'replay': replay, 'tests': tests if full else sorted(selected),
            'changed': changed, 'reasons': reasons,
            'scope': 'Conservative static package/import routing; full suite remains scheduled.'}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--base')
    p.add_argument('--head', default='HEAD')
    p.add_argument('--full', action='store_true')
    p.add_argument('--event', action='store_true', help='Read GitHub event/base through environment')
    p.add_argument('--plan', type=Path, default=Path('ci-plan.json'))
    p.add_argument('--github-output', type=Path)
    p.add_argument('--run', action='store_true')
    args = p.parse_args()
    if args.run:
        import unittest
        plan = json.loads(args.plan.read_text())
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        for name in plan['tests']:
            if Path(name).name != name or not name.startswith('test_') or not name.endswith('.py'):
                raise ValueError('Invalid test name')
            suite.addTests(loader.discover(str(ROOT / 'tests'), pattern=name))
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        raise SystemExit(0 if result.wasSuccessful() else 1)
    if args.event:
        args.full = os.environ.get('CI_EVENT') in ('schedule', 'workflow_dispatch')
        args.base = os.environ.get('CI_BASE', '')
        if not args.base or set(args.base) == {'0'}:
            args.full = True
    if not args.full and not args.base:
        p.error('--base is required unless --full is set')
    changed = [] if args.full else subprocess.check_output(
        ['git', 'diff', '--name-only', '--no-renames', args.base, args.head, '--'],
        cwd=ROOT, text=True).splitlines()
    plan = select(ROOT, changed, args.full)
    args.plan.write_text(json.dumps(plan, indent=2) + '\n')
    print(json.dumps(plan, indent=2))
    if args.github_output:
        with args.github_output.open('a') as f:
            f.write('replay=' + str(plan['replay']).lower() + '\n')


if __name__ == '__main__':
    main()
