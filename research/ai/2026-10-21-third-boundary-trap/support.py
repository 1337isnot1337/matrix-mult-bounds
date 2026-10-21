"""A sharp small control for the matrix-target support ceiling."""
import sympy as sp


def report():
    originals=[]
    for row in range(2):
        x=sp.zeros(2,1);x[row,0]=1
        originals.append(sp.kronecker_product(x,sp.eye(11)))
    retained_rows=[i for i in range(22) if i not in [4,5,6,7]]
    retained_columns=list(range(4,11))
    projected=[M.extract(retained_rows,retained_columns) for M in originals]
    first=sp.Matrix.vstack(*(sp.Matrix(1,M.rows*M.cols,list(M)) for M in projected))
    return {'outer_dimensions':[2,1],'inner_dimension':11,
            'projection_kernel_dimensions':[4,4],
            'original_matrix_ranks':[M.rank() for M in originals],
            'projected_matrix_ranks':[M.rank() for M in projected],
            'projected_first_rank':first.rank(),
            'projected_joint_column_dimension':sp.Matrix.hstack(*projected).rank(),
            'projected_joint_row_dimension':sp.Matrix.vstack(*projected).rank(),
            'target_first_rank_ceiling_under_twelve_dimensional_supports':2,
            'scope':'Target-subspace geometry control only, not a source degeneration.'}
