"""Independent dual-number and minor controls for first-jet obstructions."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-20-quantum-jet-filtration'
RESULTS=ROOT/'results/quantum-jet-filtration-2026-10-20'
spec=importlib.util.spec_from_file_location('quantum_jets',PACKAGE/'jets.py')
jets=importlib.util.module_from_spec(spec);spec.loader.exec_module(jets)
one=jets.m


def evaluate_dual(poly,root):
    """Horner evaluation in F_p[epsilon]/epsilon^2, without differentiation."""
    constant=linear=0;p=one.PRIME
    for exponent in range(poly.degree(),-1,-1):
        c=poly.get((exponent,),one.qmod.QQ.zero)
        value=int(c.numerator)*pow(int(c.denominator),-1,p)%p
        constant,linear=(constant*root+value)%p,(linear*root+constant)%p
    return constant,linear


class QuantumJetFiltrationTests(unittest.TestCase):
    def test_all_first_derivatives_match_independent_dual_number_evaluation(self):
        for phase in [(6,1),(3,1),(3,2),(6,5)]:
            _,phi,minimum,_=one.leading_parts(4,phase[0])
            metadata,_=one.root_map(4,*phase);root=metadata['root'];p=one.PRIME
            _,entries=one.local_matrix(4);actual=jets.first_jet(4,*phase)
            scalar=one.qmod.K(phi)**(-minimum)
            for key,value in entries.items():
                normalized=value*scalar
                n0,n1=evaluate_dual(normalized.numer,root)
                d0,d1=evaluate_dual(normalized.denom,root)
                self.assertNotEqual(d0,0)
                expected=(n1*d0-n0*d1)*pow(d0,-2,p)%p
                self.assertEqual(actual.get(key,0),expected,(phase,key))

    def test_saved_minor_certificates_replay(self):
        actual=jets.report();saved=json.loads((RESULTS/'first-jet-certificates.json').read_text())
        self.assertEqual(actual,saved)
        self.assertEqual(len(actual['records']),32)
        self.assertEqual(len(actual['leading_rank_controls']),4)
        for control in actual['leading_rank_controls']:
            self.assertEqual(control['rank_lower_bound'],4)
            self.assertEqual(control['row_support_upper_bound'],4)
            self.assertNotEqual(control['minor_determinant_mod_prime'],0)
        for record in actual['records']:
            self.assertEqual(record['partial_saturation_rank_lower_bound'],64)
            self.assertEqual(record['slice_rank_upper_bound'],56)
            self.assertGreater(record['nonzero_rate_monomial_exponent'],0)
            self.assertEqual(record['slice_ceiling_after_constant_output_codimensions_at_most_two'],94)
            self.assertEqual([c['inactive_grade'] for c in record['inactive_slice_minors']],[4,5,7,8])
            for control in record['inactive_slice_minors']:
                self.assertEqual(control['rank_lower_bound'],28)
                self.assertNotEqual(control['minor_determinant_mod_prime'],0)

    def test_rate_dependence_is_exact_column_scaling_in_every_case(self):
        saved=json.loads((RESULTS/'first-jet-certificates.json').read_text())
        for record in saved['records']:
            left=tuple(record['left_phase']);right=tuple(record['right_phase'])
            metaB,B0=one.root_map(4,*left);metaC,C0=one.root_map(4,*right)
            side=record['varying_leg'];phase=left if side=='left' else right
            support=set(metaB['row_labels'] if side=='left' else metaC['row_labels'])
            derivative={key:value for key,value in jets.first_jet(4,*phase).items() if key[0] not in support}
            for rate in [2,one.PRIME-1]:
                scaled={key:value*rate%one.PRIME for key,value in derivative.items()}
                B={**B0,**scaled} if side=='left' else B0
                C={**C0,**scaled} if side=='right' else C0
                rows=one.projected_source(4,B,C)
                minor=[[rows[i].get(j,0) for j in record['minor_columns']] for i in record['minor_rows']]
                expected=record['minor_determinant_mod_prime']*pow(rate,record['nonzero_rate_monomial_exponent'],one.PRIME)%one.PRIME
                self.assertEqual(one.determinant_mod(minor),expected)
                for control in record['inactive_slice_minors']:
                    coordinate=control['inactive_coordinate']
                    sliced=[{(col//112 if side=='left' else col%112):value
                             for col,value in row.items()
                             if (col%112 if side=='left' else col//112)==coordinate}
                            for row in rows]
                    minor=[[sliced[i].get(j,0) for j in control['minor_columns']] for i in control['minor_rows']]
                    expected=control['minor_determinant_mod_prime']*pow(rate,control['nonzero_rate_monomial_exponent'],one.PRIME)%one.PRIME
                    self.assertEqual(one.determinant_mod(minor),expected)

    def test_zero_rate_cannot_supply_the_certified_first_jet_minor(self):
        record=json.loads((RESULTS/'first-jet-certificates.json').read_text())['records'][0]
        _,B0=one.root_map(4,*record['left_phase']);_,C0=one.root_map(4,*record['right_phase'])
        rows=one.projected_source(4,B0,C0)
        minor=[[rows[i].get(j,0) for j in record['minor_columns']] for i in record['minor_rows']]
        self.assertEqual(one.determinant_mod(minor),0)


if __name__=='__main__':unittest.main()
