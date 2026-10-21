"""Standard-library exact full-flag orientation and parabolic controls."""
import importlib
from itertools import product
from pathlib import Path
import sys
import unittest

RESEARCH=Path(__file__).resolve().parents[1]/'research/ai/2026-10-20-paired-direct-sums'
sys.path.insert(0,str(RESEARCH))
control=importlib.import_module('q64_parabolic_exact_control')
replay=importlib.import_module('q64_experiment_replay')
operator=importlib.import_module('q64_operator_diagnostics')
sys.path.pop(0)


class FullFlagControls(unittest.TestCase):
    def test_all_zero_degree_positions_are_exactly_the_target(self):
        target_positions={((5*i+k)*20+4*i+j)*20+5*j+k for i,j,k in product(range(5),range(4),range(5))}
        for grading in ['lexicographic','refined']:
            degree=replay.degrees(control.powers(grading))
            self.assertEqual({i for i,d in enumerate(degree) if d==0},target_positions)
            self.assertEqual(sum(d<0 for d in degree),4950)
            self.assertEqual(sum(d>0 for d in degree),4950)

    def test_operator_weight_difference_includes_the_middle_sign(self):
        for grading in ['lexicographic','refined']:
            alpha=[20*i for i in range(5)];beta=[5*j for j in range(4)];gamma=list(range(5))
            if grading=='refined':alpha[-1]+=1000;gamma[-1]+=1000
            h=[-alpha[i]-beta[j]+gamma[k] for i,j,k in product(range(5),range(4),range(5))]
            self.assertEqual(len(set(h)),100)
            actual=operator.as_operator(replay.degrees(control.powers(grading)))
            self.assertEqual(actual,[[a-b for b in h] for a in h])

    def test_upper_parabolic_controls_and_opposite_shears(self):
        result=control.exact_controls()
        self.assertTrue(result['upper_triangular_physical_shears_preserve_exact_acceptance'])
        self.assertEqual(result['scalar_cost'],103)
        self.assertEqual(result['opposite_shear_nonpositive_failure_counts'],{'i':5,'j':4,'k':3})
        self.assertEqual(result['all_target_positions_checked_per_control'],10000)


if __name__=='__main__':unittest.main()
