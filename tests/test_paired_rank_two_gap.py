"""Replay the exact rank-two paired-source finite receipt."""
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'research/ai/2026-10-23-paired-rank-two-gap/verify.py'
CERT = ROOT / 'results/paired-rank-two-gap-2026-10-23/certificate.json'
spec = importlib.util.spec_from_file_location('paired_rank_two_gap', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class PairedRankTwoGapTests(unittest.TestCase):
    def test_replay_certificate(self):
        self.assertEqual(module.verify(), json.loads(CERT.read_text(encoding='utf-8')))

    def test_block_sharp_rectangular(self):
        for e in range(1, 8):
            for d in range(1, 8):
                block = module.pencil_pair_block(e, d)
                self.assertEqual(module.field_rank(block, 2), e*d + min(e,d))

    def test_diagnostic_tamper(self):
        data = json.loads(CERT.read_text(encoding='utf-8'))
        data['rank_two_gf2_censuses'][0]['ranks']['6'] = 999
        self.assertNotEqual(module.verify(), data)

if __name__ == '__main__':
    unittest.main()
