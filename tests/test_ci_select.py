import importlib.util
from pathlib import Path
import tempfile
import unittest
P=Path(__file__).resolve().parents[1]/'tools/ci_select.py'
S=importlib.util.spec_from_file_location('ci_select',P);v=importlib.util.module_from_spec(S);S.loader.exec_module(v)
class SelectionTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
  files={'tests/test_research.py':'','tests/test_a.py':"P='research/ai/pkg-a/a.py'",'tests/test_b.py':"P='research/ai/pkg-b/b.py'",'research/ai/pkg-a/a.py':"from shared import f\nDATA='results/cert-a/proof.json'",'research/ai/pkg-b/b.py':'','research/ai/pkg-c/shared.py':'def f(): pass'}
  for path,text in files.items():
   p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
 def test_docs_only(self):
  r=v.select(self.root,['README.md']);self.assertEqual(r['tests'],['test_research.py']);self.assertFalse(r['replay'])
 def test_transitive_source(self):
  r=v.select(self.root,['research/ai/pkg-c/shared.py']);self.assertEqual(r['tests'],['test_a.py','test_research.py']);self.assertFalse(r['full'])
 def test_saved_certificate(self):
  self.assertIn('test_a.py',v.select(self.root,['results/cert-a/proof.json'])['tests'])
 def test_unknown_code_falls_back(self):
  self.assertTrue(v.select(self.root,['new_code.py'])['full'])
 def test_deleted_test_falls_back(self):
  self.assertTrue(v.select(self.root,['tests/test_deleted.py'])['full'])
 def test_archive_replays(self):
  r=v.select(self.root,['research/ai/2026-10-20/a.py']);self.assertTrue(r['full']);self.assertTrue(r['replay'])
 def test_tooling_replays(self):
  r=v.select(self.root,['tools/ci_select.py']);self.assertTrue(r['full']);self.assertTrue(r['replay'])
 def test_schedule_full(self):
  r=v.select(self.root,[],True);self.assertEqual(len(r['tests']),3);self.assertTrue(r['replay'])
 def test_modified_test_selected(self):
  self.assertIn('test_b.py',v.select(self.root,['tests/test_b.py'])['tests'])

 def test_package_deletion_still_finds_consumers(self):
  self.assertIn('test_a.py',v.select(self.root,['research/ai/pkg-a/deleted.py'])['tests'])
 def test_config_requires_tests_not_archive(self):
  r=v.select(self.root,['.github/workflows/verify.yml']);self.assertTrue(r['full']);self.assertFalse(r['replay'])
 def test_dependency_requires_archive(self):
  self.assertTrue(v.select(self.root,['requirements.txt'])['replay'])
