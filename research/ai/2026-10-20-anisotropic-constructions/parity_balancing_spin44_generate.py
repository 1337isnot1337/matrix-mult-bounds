"""Optional rational reconstruction of the balanced eight-channel spin module."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'results/anisotropic-constructions-2026-10-20'


def generate():
    import sympy as sp
    data = json.loads((DIRECTORY/'parity_balancing_spin44_candidate.json').read_text())
    J, K = [], []
    for shift in range(2):
        first, second = sp.zeros(20,16), sp.zeros(16,20)
        for a in range(4):
            for j in range(4):
                first[4*(a+shift)+j,4*a+j] = 1
                second[4*a+j,5*a+j+shift] = 1
        J.append(first)
        K.append(second)
    columns = []
    for length, generator in zip(data['profile'],data['generators']):
        for shift in range(length):
            column = sp.zeros(16,1)
            for a,row in enumerate(generator):
                for j,value in enumerate(row):
                    column[4*(a+shift)+j] = value
            columns.append(column)
    U = sp.Matrix.hstack(*columns)
    Q = sp.Matrix.hstack(*U.T.nullspace()).T
    q0,q1 = Q*K[0], Q*K[1]
    zero = sp.zeros(Q.rows,20)
    constraints = sp.Matrix.vstack(sp.Matrix.hstack(q1,zero),sp.Matrix.hstack(zero,q0),sp.Matrix.hstack(q0,-q1))
    D = sp.Matrix.hstack(*constraints.nullspace())
    selected = D*sp.Matrix(data['D_subspace_matrix'])
    plus,minus = selected[:20,:],selected[20:,:]
    V = K[0]*plus
    L = []
    for p,s in ((0,0),(0,1),(1,0),(1,1)):
        matrix = sp.zeros(40,16)
        matrix[20*p:20*(p+1),:] = J[s]
        L.append(matrix)
    Wfull = sp.Matrix.hstack(*[a*U for a in L])
    W = Wfull[:,data['W_basis_column_indices']]
    LP = [L[1],(L[0]-L[3])/2,L[2]]
    B = sp.Matrix.hstack(W,*[a*V for a in LP])
    determinant = B.det(method='domain-ge')
    if B.shape != (40,40) or not determinant:
        raise ArithmeticError('The exact balanced join is not invertible')
    Y = B.inv(method='DM')[16:,:]
    Z = sp.Matrix.hstack(sp.Matrix.vstack(sp.zeros(20,8),plus),
                         sp.Matrix.vstack(plus/2,-minus/2),
                         sp.Matrix.vstack(minus,sp.zeros(20,8))).T
    old = json.loads((DIRECTORY/'spin-module14-witness.json').read_text())['X']
    X = sp.zeros(9,12)
    for r,c,v in old['entries']:
        X[r,c] = sp.Rational(v,old['denominator'])

    def pack(matrix):
        denominator = int(sp.ilcm(*[v.q for v in matrix]))
        return {'shape':[matrix.rows,matrix.cols],'denominator':denominator,
                'entries':[[i,j,int(matrix[i,j]*denominator)] for i in range(matrix.rows)
                           for j in range(matrix.cols) if matrix[i,j]]}

    witness = {'source_parameters':[2,4,4],'source_format':[12,40,40],
               'target':[3,3,8],'target_format':[9,24,24],'field':'Q',
               'profile':data['profile'],'generators':data['generators'],
               'U_left_annihilator':pack(Q),'W_basis_column_indices':data['W_basis_column_indices'],
               'D_subspace_matrix':data['D_subspace_matrix'],
               'U_dimension':U.cols,'W_dimension':W.cols,'D_dimension':D.cols,
               'join_dimension':40,'join_determinant':str(determinant),
               'X':pack(X),'Y':pack(Y),'Z':pack(Z),'new_exponent_established':False}
    path = DIRECTORY/'parity_balancing_spin44_witness.json'
    path.write_text(json.dumps(witness,indent=2)+'\n')
    print(json.dumps({'saved':str(path),'determinant':str(determinant),
                      'denominators':[witness[k]['denominator'] for k in 'XYZ'],
                      'nonzeros':[len(witness[k]['entries']) for k in 'XYZ']}),flush=True)
    return witness


if __name__ == '__main__':
    generate()
