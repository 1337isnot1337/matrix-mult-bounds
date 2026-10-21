"""Integer incidence data for the diagonal orbit of the twenty T4 terms."""
import sympy as sp


def incidence_data(system):
    targets = sorted((p,y,z) for rows in system.constraints.values()
                     for p,y,z,wanted in rows if wanted)
    matrix = sp.zeros(len(targets),24)
    for row,(p,y,z) in enumerate(targets):
        for column in (p,4+y,14+z):
            matrix[row,column] = 1
    columns = list(matrix.rref()[1])
    return targets,matrix,columns,matrix.T.nullspace()
