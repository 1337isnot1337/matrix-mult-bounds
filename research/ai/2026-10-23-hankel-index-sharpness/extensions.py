"""Exact common-tangent and residue-block certificates for the fixed pencil."""
import argparse
import json
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


def certificate(epsilon,p,q):
    s=p+q; r=epsilon*s; a=r+p; b=r+q; moments=a+b-1
    equations=[]
    for i in range(p):
        for j in range(q):
            rows=[[0]*moments for _ in range(2*epsilon+1)]
            for k in range(epsilon+1):
                for ell in range(epsilon+1):
                    rows[k+ell][s*(k+ell)+i+j]+=(-1)**(2*epsilon-k-ell)
            equations.extend(rows)
    operator=sp.Matrix(equations)
    rank=DomainMatrix.from_Matrix(operator).convert_to(sp.QQ).rank()
    support=[j*s-1 for j in range(1,2*epsilon+1)]
    actual_support=[i for i in range(moments) if not any(operator[:,i])]
    if actual_support!=support or moments-rank!=2*epsilon:
        raise ArithmeticError('common tangent space failed')
    # Check the complete coefficient map, rather than a sampled matrix.
    row_groups=[[i for i in range(a) if i%s==alpha] for alpha in range(s)]
    column_groups=[[j for j in range(b) if j%s==s-1-alpha] for alpha in range(s)]
    checked=0
    for alpha,rows in enumerate(row_groups):
        expected=(epsilon+1,epsilon) if alpha<p else (epsilon,epsilon+1)
        if (len(rows),len(column_groups[alpha]))!=expected:
            raise ArithmeticError('wrong residue block shape')
        for beta,columns in enumerate(column_groups):
            for ii,i in enumerate(rows):
                for jj,j in enumerate(columns):
                    coefficient=(i+j in support)
                    if coefficient!=(alpha==beta):
                        raise ArithmeticError('residue coefficient support failed')
                    if alpha==beta and i+j!=s*(ii+jj+1)-1:
                        raise ArithmeticError('residue Hankel block failed')
                    checked+=1
    if checked!=a*b:
        raise ArithmeticError('incomplete permutation check')
    return {'epsilon':epsilon,'left_nullity':p,'right_nullity':q,
            'shape':[a,b],'rank_ceiling':r,'moment_space_dimension':moments,
            'common_tangent_rank':rank,'maximal_extension_dimension':2*epsilon,
            'allowed_moment_indices':support,'coefficient_entries_checked':checked,
            'block_shapes':[[len(rows),len(columns)] for rows,columns in zip(row_groups,column_groups)]}


def report():
    records=[certificate(e,p,q) for e in range(1,5) for p in range(1,4) for q in range(1,4)]
    return {'scope':'Exact fixed-pencil linear-extension certificates supporting a written characteristic-zero theorem.',
            'epsilon_range':[1,4],'left_and_right_nullity_range':[1,3],
            'families_checked':len(records),'records':records,
            'arbitrary_quadratic_pencils_classified':False,
            'independent_review':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args(); result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f"Verified common tangent spaces and every residue coefficient for {result['families_checked']} families.")
