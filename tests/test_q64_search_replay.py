"""Controls for complete coefficients, Laurent powers, and regrouping."""
import importlib
from itertools import product
from pathlib import Path
import sys
import unittest

RESEARCH=Path(__file__).resolve().parents[1]/'research/ai/2026-10-20-paired-direct-sums'
sys.path.insert(0,str(RESEARCH))
replay=importlib.import_module('q64_experiment_replay')
operator=importlib.import_module('q64_operator_diagnostics')
sys.path.pop(0)


def matrix_product(left,right):
    result=[[0]*len(right[0]) for _ in left]
    for i,row in enumerate(left):
        for k,a in enumerate(row):
            if a:
                for j,b in enumerate(right[k]):
                    if b:
                        result[i][j]+=a*b
    return result


class Q64SearchControls(unittest.TestCase):
    def test_integer_base_control(self):
        report=replay.integer_control()
        self.assertTrue(report['exact_positive_control_passed'])
        self.assertTrue(report['deliberate_sign_error_detected'])
        self.assertEqual(report['all_integer_positions_checked'],64)

    def test_exact_positive_and_negative_laurent_controls(self):
        report=replay.exact_controls()
        self.assertTrue(report['negative_power_error_detected'])
        self.assertTrue(report['nonzero_positive_power_permitted'])
        self.assertEqual(report['laurent_control_scalar_cost'],101)
        powers=replay.degrees(replay.row_powers())
        self.assertEqual([powers.count(k) for k in range(-2,3)],
                         [256,2176,5136,2176,256])

    def test_operator_identity_and_non_nilpotent_error(self):
        target=[0]*10000
        for i,j,k in product(range(5),range(4),range(5)):
            target[((5*i+k)*20+4*i+j)*20+5*j+k]=1
        identity=[[int(i==j) for j in range(100)] for i in range(100)]
        self.assertEqual(operator.as_operator(target),identity)
        target[16*20]+=1
        error=operator.as_operator(target)
        for i in range(100):
            error[i][i]-=1
        self.assertTrue(any(any(row) for row in error))
        self.assertFalse(any(any(row) for row in matrix_product(error,error)))
        target[20*400]+=1
        bad=operator.as_operator(target)
        for i in range(100):
            bad[i][i]-=1
        square=matrix_product(bad,bad)
        self.assertEqual(sum(square[i][i] for i in range(100)),2)


if __name__=='__main__':
    unittest.main()
