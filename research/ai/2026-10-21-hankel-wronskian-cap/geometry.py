"""Exact controls and arithmetic for two written Hankel dimension refinements."""
import argparse
from math import comb
from pathlib import Path
import importlib.util
import sympy as sp


def crossed_dimension_cap(a,b,R,parameter_span):
    N=a*b*(a+b-1)
    if not (a>=1 and b>=1 and R>=1 and 0<=parameter_span<=N):
        raise ValueError('Invalid crossed-rank or parameter-span range')
    original=min(N,(a+b)*R+(a-b)**2//4)
    proper=parameter_span<N
    return original-int(proper),original,proper


def crossed_matrix(blocks,p,q):
    return sp.Matrix(p*q,p*q,lambda row,col:blocks[row//p+col//q][row%p,col%q])


def action_controls():
    records=[]
    for p in range(1,6):
        for q in range(1,6):
            d=p+q-2;lam=2
            blocks=[sp.Matrix(p,q,lambda i,j:(k+2)*(i+3)-(j+1)*(k+1)**2) for k in range(d+1)]
            A=sp.eye(p);B=sp.eye(q)
            if p>1:A[0,1]=2
            if q>1:B[q-1,0]=-1
            Sa=sp.Matrix(q,q,lambda i,j:comb(q-1-i,j-i)*lam**(j-i) if j>=i else 0)
            Sb=sp.Matrix(p,p,lambda i,j:comb(p-1-i,j-i)*lam**(j-i) if j>=i else 0)
            changed=[sum((comb(d-k,l-k)*lam**(l-k)*(A*blocks[l]*B.T) for l in range(k,d+1)),sp.zeros(p,q)) for k in range(d+1)]
            H=crossed_matrix(blocks,p,q);Hp=crossed_matrix(changed,p,q)
            left=sp.kronecker_product(Sa,A);right=sp.kronecker_product(Sb,B)
            assert Hp==left*H*right.T
            Jq=sp.Matrix(q,q,lambda i,j:int(i+j==q-1));Jp=sp.Matrix(p,p,lambda i,j:int(i+j==p-1))
            assert crossed_matrix(list(reversed(blocks)),p,q)==sp.kronecker_product(Jq,sp.eye(p))*H*sp.kronecker_product(Jp,sp.eye(q))
            assert A.det()==B.det()==Sa.det()==Sb.det()==1
            labels={(i,j,k) for i in range(p) for j in range(q) for k in range(d+1)}
            reached={(0,0,0)};queue=[(0,0,0)]
            while queue:
                i,j,k=queue.pop()
                neighbors=[(i+1,j,k),(i-1,j,k),(i,j+1,k),(i,j-1,k),(i,j,k+1),(i,j,k-1)]
                for vertex in neighbors:
                    if vertex in labels and vertex not in reached:reached.add(vertex);queue.append(vertex)
            assert reached==labels
            records.append({'p':p,'q':q,'coefficient_dimension':p*q*(d+1),
                            'crossed_matrix_dimension':p*q,'action_identity_verified':True,'binary_reversal_identity_verified':True,
                            'basis_action_graph_reachable':len(reached)})
    return records


def boundary_controls():
    cases=[]
    for k in range(2,11,2):
        r=k*(k+2)//2;m=2*r+1
        assert m==(k+1)**2 and r>k
        anti=sp.Matrix(r,r,lambda i,j:int(i+j==r-1))
        cofactor=int(anti.to_DM().det());assert cofactor in [-1,1]
        h=[0]*m;h[r-1]=1
        H=sp.Matrix(r+1,r+1,lambda i,j:h[i+j]);assert H.to_DM().rank()==r
        cases.append({'input_rank':k,'hankel_rank':r,'ambient_dimension':m,
                      'target_dimension':2*r,'rank_parameter_hypersurface_dimension':k*(k+2),
                      'matrix_determinant_degree':k+1,'hankel_determinant_degree':r+1,
                      'nonzero_hankel_determinant_derivative':cofactor})
    return cases


def report():
    a,b,c,d=sp.symbols('a b c d');det=sp.Matrix([[a,b],[c,d]]).det()
    assert sp.expand(det-(a*d-b*c))==0 and det.subs({c:0,d:0})==0
    assert crossed_dimension_cap(1,2,1,2)==(2,3,True)
    assert crossed_dimension_cap(1,2,1,4)==(3,3,False)
    assert crossed_dimension_cap(12,12,16,2500)==(383,384,True)
    return {'scope':'Exact controls for written, unreviewed geometric arguments; not finite proofs of their general claims.',
            'crossed_action_controls':action_controls(),'hankel_boundary_degree_controls':boundary_controls(),
            'proper_section_sharp_control':{'p':1,'q':2,'rank_bound':1,'ambient_dimension':4,
                'rank_cone_dimension':3,'proper_linear_space_dimension':2,'intersection_dimension':2,
                'determinant':str(det),'proper_space':'second row zero'},
            'full_ambient_countercontrol':{'parameter_span':4,'dimension_bound':3,'one_dimensional_loss_allowed':False},
            'reducible_representation_countercontrol':{'variety':'x*y=0','connected_group':'diagonal torus',
                'ambient_dimension':2,'component_span_dimension':1,'component_stability_alone_suffices':False},
            'a12_boundary_application':{'source_dimension':3312,'block_dimension':2500,
                'crossed_rank':16,'old_dimension_bound':384,'proper_section_bound':383,
                'rank_four_parameter_dimension':384,'ordinary_block_at_total_dimension':2546,
                'excluded_by_proper_section':True},
            'independent_review':False,'improves_omega':False}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();args.output.parent.mkdir(parents=True,exist_ok=True)
    spec=importlib.util.spec_from_file_location('geometry_formatter',Path(__file__).with_name('verify.py'))
    formatter=importlib.util.module_from_spec(spec);spec.loader.exec_module(formatter)
    formatter.write_json(args.output,report());print('Crossed-action, proper-section and boundary-degree controls passed.')
