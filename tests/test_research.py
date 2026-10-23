"""Regression checks for the imported mathematics and repository evidence."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'research' / 'ai' / '2026-10-20'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


search = load('archived_search', ARCHIVE / 'search_degenerations.py')
replay = load('replay', ROOT / 'tools' / 'replay.py')


def independent_profile(a, b):
    m, n = sorted((a, b))
    value = Fraction(2*n+m-1, 2)
    for k in range(1, m):
        value *= Fraction(3*k+1, 3*k)
    return value


class ProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h = search.slopes(300)

    def test_closed_product_matches_recurrence(self):
        for a, b in product(range(1, 25), repeat=2):
            self.assertEqual(search.profile(a, b, self.h), independent_profile(a, b))

    def test_normalization(self):
        for a in range(1, 100):
            self.assertEqual(search.profile(1, a, self.h), a)
            self.assertEqual(search.profile(a, 1, self.h), a)

    def test_concavity_identity(self):
        for a in range(3, 30):
            for b in range(2, a):
                slack = 2*search.profile(a,b,self.h)-search.profile(a,b-1,self.h)-search.profile(a,b+1,self.h)
                self.assertEqual(slack, 2*self.h[b]*Fraction(a-b, 3*b*(3*b-2)))

    def test_diagonal_join(self):
        for a in range(2, 100):
            self.assertEqual(2*search.profile(a,a,self.h),
                             search.profile(a,a-1,self.h)+search.profile(a,a+1,self.h))

    def test_tripling_equality_above_diagonal(self):
        for a in range(1, 25):
            for b in range(a, 30):
                self.assertEqual(search.profile(a,3*b+a-1,self.h), 3*search.profile(a,b,self.h))

    def test_exact_rank_bound(self):
        for a, b in product(range(1, 25), repeat=2):
            self.assertLessEqual(search.profile(a,b,self.h)**3, (a+b-1)**4)

    def test_replication(self):
        for a, b, q in product(range(1, 10), range(1, 10), range(1, 9)):
            self.assertGreaterEqual(search.profile(q*a,q*b,self.h)**3,
                                    q**4 * search.profile(a,b,self.h)**3)

    def test_conditional_numeric_example(self):
        eta = Fraction(1, 1000)
        self.assertEqual(9/(4+2*eta), Fraction(1500, 667))
        self.assertLess(Fraction(1500, 667), Fraction(9, 4))


class SupportTests(unittest.TestCase):
    def test_nonnegative_weights_and_exact_zero_support(self):
        for wx in product((0,1), repeat=2):
            for wy in product((0,1), repeat=4):
                groups, wz = search.components(wx, wy)
                actual = {term for group in groups for term in group}
                expected = set()
                for i, j in product(range(2), range(4)):
                    weight = wx[i]+wy[j]+wz[i+j]
                    self.assertGreaterEqual(weight, 0)
                    if weight == 0:
                        expected.add((i,j,i+j))
                self.assertEqual(actual, expected)

    def test_nonshared_legs_are_disjoint(self):
        groups, _ = search.components((0,1), (0,1,0,1))
        for left in range(len(groups)):
            for right in range(left):
                for leg in (1,2):
                    self.assertTrue({t[leg] for t in groups[left]}.isdisjoint(
                                    {t[leg] for t in groups[right]}))

    def test_full_convolution_recognition(self):
        for a,b in product(range(1,6), repeat=2):
            terms=[(i,j,i+j) for i in range(a) for j in range(b)]
            result=search.recognize(terms)
            self.assertEqual(result['kind'], 'convolution')
            self.assertEqual(sorted((result['a'],result['b'])), sorted((a,b)))

    def test_recorded_witness_scores_are_exact(self):
        h=search.slopes(100)
        for name in ('binary_search.json','ternary_search.json','random_search.json'):
            report=json.loads((ARCHIVE/name).read_text())
            for key in ('best','best_nontrivial'):
                rec=report[key]
                actual=search.inspect(tuple(rec['x_weights']),tuple(rec['y_weights']),None,h)
                self.assertEqual(actual['source_exact'],rec['source_exact'])
                self.assertEqual(actual['target_exact'],rec['target_exact'])
                self.assertFalse(actual['violation_exact'])


class RepositoryTests(unittest.TestCase):
    def test_archive_manifest(self):
        self.assertEqual(len(replay.check_manifest()),10)

    def assert_claim_evidence(self, claim):
        allowed={'proof-written-unreviewed','derivation-unreviewed','conditional-implication','finite-experiment','lean-formalized-lemma'}
        self.assertIn(claim['status'],allowed)
        self.assertFalse(claim['improves_omega'])
        evidence=ROOT/claim['evidence']
        self.assertTrue(evidence.is_file())
        if claim['status']=='lean-formalized-lemma':
            self.assertIs(claim.get('lean_formalized'),True)
            self.assertEqual(evidence.suffix,'.lean')

    def test_claim_ledger_status(self):
        claims=json.loads((ROOT/'research/claims.json').read_text())['claims']
        self.assertEqual(len(claims),len({c['id'] for c in claims}))
        for claim in claims:
            self.assert_claim_evidence(claim)

    def test_formalized_claim_requires_lean_evidence(self):
        claims=json.loads((ROOT/'research/claims.json').read_text())['claims']
        claim=next(c for c in claims if c['id']=='AI-SCALAR-FINITE-SLOPE-001')
        self.assert_claim_evidence(claim)
        for update in ({'lean_formalized':False}, {'lean_formalized':1},
                       {'evidence':'README.md'},
                       {'evidence':'formal/scalar-profile/Missing.lean'},
                       {'status':'unrecognized-status'}, {'improves_omega':True}):
            with self.subTest(update=update), self.assertRaises(AssertionError):
                self.assert_claim_evidence({**claim,**update})
        missing_flag=dict(claim)
        del missing_flag['lean_formalized']
        with self.assertRaises(AssertionError):
            self.assert_claim_evidence(missing_flag)

    def test_source_registry(self):
        sources=json.loads((ROOT/'references/sources.json').read_text())['sources']
        self.assertEqual(len(sources),50)
        self.assertTrue({'PETROV20','SAWIN18','CVZ19','AVZ20','PASS26','AVZ26','DO01'} <= {s['id'] for s in sources})
        self.assertEqual(len(sources),len({s['id'] for s in sources}))
        for source in sources:
            self.assertTrue(source['url'].startswith('https://'))
            self.assertTrue(source['inspection'])
            self.assertFalse(source['proof_rebuilt_locally'])

    def test_replayed_coverage(self):
        summary=json.loads((ROOT/'results/bootstrap-2026-10-20/summary.json').read_text())
        self.assertEqual(summary['status'],'passed')
        self.assertEqual(summary['total_weight_candidates'],242668)
        self.assertEqual(len(summary['runs']),5)

    def test_replay_child_keeps_assertions_with_inherited_optimization(self):
        with tempfile.TemporaryDirectory() as directory:
            archive=Path(directory)/'archive'
            archive.mkdir()
            report=json.dumps({'checks':1,'elapsed_seconds':0})
            (archive/'checks.json').write_text(report)
            (archive/'check.py').write_text(
                "from pathlib import Path\n"
                "assert False, 'archived assertion must run'\n"
                f"Path('checks.json').write_text({report!r})\n")
            manifest={name:hashlib.sha256((archive/name).read_bytes()).hexdigest()
                      for name in ('check.py','checks.json')}
            (archive/'manifest.json').write_text(json.dumps({'sha256':manifest}))
            output=Path(directory)/'output'
            # An unoptimized parent can inherit this value when started with -E.
            with patch.dict('os.environ',{'PYTHONOPTIMIZE':'1'}), patch.multiple(
                    replay,ARCHIVE=archive,
                    RUNS=[('checks.json',['check.py'],'checks',1)]):
                with self.assertRaisesRegex(
                        RuntimeError,'AssertionError: archived assertion must run'):
                    replay.run(output,30)
            self.assertFalse((output/'summary.json').exists())

    def test_normalization_retains_exact_evidence(self):
        value={'ratio_float':1.0,'elapsed_seconds':2,'exact':'4/3','violation_exact':False}
        self.assertEqual(replay.exact_payload(value),{'exact':'4/3','violation_exact':False})

    def test_relative_markdown_links(self):
        for path in ROOT.rglob('*.md'):
            if ARCHIVE in path.parents:
                continue
            text=path.read_text()
            for target in re.findall(r'\]\(([^)]+)\)',text):
                if '://' in target or target.startswith('#'):
                    continue
                local=target.split('#',1)[0]
                self.assertTrue((path.parent/local).resolve().exists(),f'{path}: {target}')


if __name__ == '__main__':
    unittest.main()
