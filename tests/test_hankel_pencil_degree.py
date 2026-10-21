"""Independent polynomial-kernel, assignment and frontier checks."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PACKAGE=ROOT/'research/ai/2026-10-21-hankel-pencil-degree'
RESULTS=ROOT/'results/hankel-pencil-degree-2026-10-21'


def load(name):
    spec=importlib.util.spec_from_file_location('test_pencil_'+name,PACKAGE/(name+'.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


v=load('verify');app=load('application')


def polynomial_kernel_dimension(H0,H1,degree):
    rows,columns=H0.shape
    block=sp.zeros(rows*(degree+2),columns*(degree+1))
    for j in range(degree+1):
        block[j*rows:(j+1)*rows,j*columns:(j+1)*columns]=H0
        block[(j+1)*rows:(j+2)*rows,j*columns:(j+1)*columns]=H1
    return block.cols-block.rank()


def assignment_dimension(r,d,exponents):
    p=len(exponents);rows=[]
    for i,j in itertools.combinations_with_replacement(range(p),2):
        for k in range(d-r+1):
            row=[0]*(p*(d+1))
            row[i*(d+1)+k+exponents[j]]+=1
            row[j*(d+1)+k+exponents[i]]+=1
            rows.append(row)
    M=sp.Matrix(rows)
    return M.cols-M.rank()


class HankelPencilDegreeTests(unittest.TestCase):
    def test_saved_controls_and_all_splittings(self):
        report=v.report();self.assertEqual(report,json.loads((RESULTS/'controls.json').read_text()))
        self.assertEqual(report['splittings']['counts'][1],6)
        general=report['general_splitting_controls']
        self.assertEqual(general['splitting_cases_checked'],96760)
        for row in general['parameters']:
            self.assertLessEqual(row['nonconstant_ruling_image_cap'],row['k']**2)
        self.assertFalse(report['independent_review']);self.assertFalse(report['improves_omega'])

    def test_strict_theorem_hypotheses_and_new_boundaries(self):
        self.assertEqual(v.symbol_cap(8,8,6),9)
        self.assertEqual(v.symbol_cap(9,9,7),9)
        self.assertEqual(v.symbol_cap(10,10,7),7)
        self.assertEqual(v.symbol_cap(4,4,3),4)
        self.assertEqual(v.symbol_cap(11,12,9),16)
        self.assertIsNone(v.symbol_cap(10,10,8))  # 5r=2(a+b), not strict.
        self.assertIsNone(v.symbol_cap(8,8,7))
        self.assertIsNone(v.symbol_cap(6,8,6))  # Rank must be strictly below both sides.
        self.assertIsNone(v.symbol_cap(8,8,0))

    def test_minimal_kernel_degrees_by_coefficient_linear_systems(self):
        # A line in the moving 3-space: two right minimal indices are one.
        h0=[0]*15;h1=[0]*15
        for h,u in [(h0,[1,2,4]),(h1,[1,3,5])]:h[5]=u[2];h[10]=-u[1];h[11]=-u[0]
        A=sp.Matrix(8,8,lambda i,j:h0[i+j]);B=sp.Matrix(8,8,lambda i,j:h1[i+j])
        self.assertEqual([polynomial_kernel_dimension(A,B,j) for j in range(3)],[0,2,4])
        # Outside the hypothesis the unique right minimal index is two.
        A=sp.Matrix(8,8,lambda i,j:int(i+j==5));B=sp.Matrix(8,8,lambda i,j:int(i+j==8))
        self.assertEqual([polynomial_kernel_dimension(A,B,j) for j in range(4)],[0,0,1,2])

    def test_assignment_spaces_by_direct_convolution_constraints(self):
        cases=[(6,14,[0,6],0,3),(6,14,[1,6],1,1),
               (6,14,[0,1,6],0,1),(6,14,[0,2,6],0,0),
               (6,14,[0,1,2],4,0),
               (7,16,[0,7],0,4),(7,16,[1,7],1,2),(7,16,[0,1,7],0,2)]
        for r,d,exponents,c,expected in cases:
            with self.subTest(r=r,exponents=exponents):
                # Removing p copies of the fixed S_g leaves the quotient assignment space.
                self.assertEqual(assignment_dimension(r,d,exponents)-len(exponents)*c,expected)

    def test_all_parameter_controls_and_corruption(self):
        u0,u1=sp.symbols('u0 u1');w=sp.symbols('w0:4');h=[0]*17
        for j,c in zip(range(3,7),w):h[j]=u1*c;h[j+7]=-u0*c
        H=sp.Matrix(9,9,lambda i,j:h[i+j]);q=sp.zeros(9,2)
        q[0,0]=u0;q[7,0]=u1;q[1,1]=u0;q[8,1]=u1
        self.assertEqual(sp.simplify(H*q),sp.zeros(9,2))
        coefficient=sp.Matrix([[sp.expand(x).coeff(a*b) for a in [u0,u1] for b in w] for x in h])
        self.assertEqual(coefficient.rank(),8)  # A cap of seven would be false.
        h[0]=1
        with self.assertRaises(ArithmeticError):v.annihilation(h,[u0]+[0]*6+[u1])

    def test_every_new_rectangular_exclusion_and_complete_replay(self):
        current=json.loads((RESULTS/'rectangular.json').read_text())
        prior=json.loads((ROOT/'results/rectangular-ordinary-frontier-2026-10-21/frontier.json').read_text())
        self.assertEqual(current,app.rectangular_report())
        self.assertEqual((current['complete_improving_sorted_shapes'],current['complete_excluded_shapes']),(5139,4645))
        changed=0
        for source,old in zip(current['sources'],prior['sources']):
            self.assertEqual(source['a'],old['a']);a=source['a'];N=a*a*(2*a-1)
            for row,previous in zip(source['records'],old['records']):
                self.assertEqual(row['shape'],previous['shape'])
                if previous['excluded']:
                    self.assertEqual(row,previous);continue
                if not row['excluded']:continue
                changed+=1;w=row['witness'];r=w['symbol_rank'];cap=w['symbol_image_cap']
                x,y=w['matrix_parameter_dimensions'];z=w['slice_rank']
                self.assertEqual(sorted([x,y,z]),row['shape'])
                self.assertLess(5*r,4*a);self.assertLess(r,a)
                t=3*r-(2*a-1);k=max(1,(t+3)//2)
                self.assertEqual(cap,max(r,k*k));self.assertGreater(x*y,cap*a*a)
                self.assertEqual(w['lift_rank_upper_bound'],z+(N-x*z)+(N-y*z))
                self.assertLess(w['lift_rank_upper_bound'],(r+1)*a*a)
            if a<=9:self.assertEqual(source['survivors'],[])
        self.assertEqual(changed,453)
        self.assertEqual([len(s['survivors']) for s in current['sources'] if s['a']>=10],[53,129,312])
        self.assertFalse(current['singular_degenerations_excluded'])

    def test_square_partitions_replay_and_honest_remaining_candidate(self):
        saved=json.loads((RESULTS/'squares.json').read_text());self.assertEqual(saved,app.square_report())
        a8,a9=saved['sources'];maximum=a8['maximum']
        self.assertTrue(a8['all_partitions_below_critical_score'])
        self.assertEqual(maximum['upper_score_numerator'],95171566351)
        self.assertLess(maximum['upper_score_numerator'],a8['critical_score_threshold']*10**6)
        self.assertFalse(a9['all_partitions_below_critical_score'])
        self.assertGreater(a9['maximum']['lower_score_numerator_of_saved_partition'],a9['critical_score_threshold']*10**6)
        self.assertEqual(a9['maximum']['maximizing_relaxed_partition'],[32,6,3])
        for source in [a8,a9]:
            a=source['a'];N=source['source_leg_dimension']
            for row in source['dimension_frontier']:
                D=row['target_leg_dimension'];shape=row['maximizing_relaxed_partition']
                if shape is None:continue
                self.assertEqual(sum(n*n for n in shape),D)
                score=sum(app.squares.score_interval(n)[1] for n in shape)
                self.assertEqual(score,row['upper_score_numerator'])
                for n in row['allowed_nonscalar_sizes']:
                    for r in range(1,a):
                        if 5*r>=4*a:continue
                        k=max(1,(3*r-2*a+4)//2);cap=max(r,k*k)
                        self.assertFalse(n*n>cap*a*a and n+2*(N-D)<(r+1)*a*a)
        # A8's old two-block candidate is now excluded by a strict witness.
        D=27**2+7**2
        allowed,_,_=app.extended_allowed_blocks(8,8,D)
        self.assertNotIn(27,allowed)


if __name__=='__main__':unittest.main()
