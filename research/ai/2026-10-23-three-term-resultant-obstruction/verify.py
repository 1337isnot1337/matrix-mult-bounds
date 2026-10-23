"""Independent integer certificate for a (3,3) three-coefficient biform slice.

No symbolic-algebra dependency.  The 16-by-16 integer grid certifies a
polynomial identity because each determinant has degree <= 15 in each
of c and t.  This is not a matrix multiplication exponent certificate.
"""
import json

A = 3
B = 3
M = A + B - 1


def matrix(c, t, b=B):
    """Literal R_(3,3): rows (j,L), columns (H,r)."""
    m = A + b - 1
    f = ((0, 0, 1), (1, 0, 1), (1, t, c))
    return [
        [f[L-r][H-j] if 0 <= L-r < 3 and 0 <= H-j < A else 0
         for r in range(A) for H in range(m)]
        for L in range(A + 2) for j in range(b)
    ]


def det_integer(rows):
    """Fraction-free exact Bareiss determinant with row pivoting."""
    m = [list(row) for row in rows]
    n = len(m)
    assert all(len(row) == n for row in m)
    if not n:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        p = next((i for i in range(k, n) if m[i][k] != 0), None)
        if p is None:
            return 0
        if p != k:
            m[k], m[p] = m[p], m[k]
            sign *= -1
        pivot = m[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = pivot*m[i][j] - m[i][k]*m[k][j]
                assert numerator % previous == 0
                m[i][j] = numerator // previous
            m[i][k] = 0
        previous = pivot
    return sign*m[n-1][n-1]


def rank_mod(rows, p):
    m = [[v % p for v in row] for row in rows]
    ncols = len(m[0])
    r = 0
    for j in range(ncols):
        pivot = next((i for i in range(r, len(m)) if m[i][j]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        inverse = pow(m[r][j], -1, p)
        for i in range(r+1, len(m)):
            if m[i][j]:
                scalar = m[i][j] * inverse % p
                for k in range(j, ncols):
                    m[i][k] = (m[i][k] - scalar*m[r][k]) % p
        r += 1
        if r == len(m):
            break
    return r


def polynomial(c, t):
    return t * (2*c**3 - 2*c*t**2 + t**4)


def verify():
    # Each entry is 0, 1, c, or t. Thus the determinant is in Z[c,t]
    # and has degree <= 15 in EACH indeterminate. Comparing it on a
    # 16-by-16 integer grid proves equality as a polynomial identity.
    points = 0
    for c in range(16):
        for t in range(16):
            assert det_integer(matrix(c,t)) == polynomial(c,t), (c,t)
            points += 1

    f0, f1 = matrix(2,0), matrix(1,1)
    assert det_integer(f0) == 0
    assert det_integer(f1) == 1

    # Complete nonzero left-kernel vector over Z: lambda_L coefficients.
    lambdas = ((3,0,5),(1,0,1),(-1,0,-3),(1,0,1),(-1,0,1))
    flat = [v for poly in lambdas for v in poly]
    assert any(flat)
    assert all(sum(flat[i]*f0[i][j] for i in range(15)) == 0
               for j in range(15))
    # Row 3 = (j=0,L=1); column 1 = (H=1,r=0).
    minor = [[f0[i][j] for j in range(15) if j != 1]
             for i in range(15) if i != 3]
    assert det_integer(minor) == -4

    for p in (2,3,5,7,11,101):
        assert rank_mod(f0,p) == (12 if p == 2 else 14)
        assert rank_mod(f1,p) == 15

    # Exact modular witnesses imply full column rank over Q for these
    # six finite rectangular cases, without any universal-b claim.
    for b in range(4,10):
        for c,t in ((2,0),(1,1)):
            assert rank_mod(matrix(c,t,b),101) == A*(A+b-1)

    # Res(u,v)=Res(u,w)=1 and Res(v,w)=(1-c)^2+t^2.
    assert all((1-c)**2+t*t == 1 for c,t in ((2,0),(1,1)))
    return {'status':'pass','integer_grid_points':points,
            'parameters':{'rank14':{'c':2,'t':0},
                          'rank15':{'c':1,'t':1}},
            'det_rank15':1,'rank14_minor':-4,
            'characteristics_checked':[2,3,5,7,11,101],
            'larger_b_checked':list(range(4,10)),
            'scope':'Exact degree-bounded determinant certificate; rank contrast for fields of characteristic !=2; no exponent implication'}

if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, sort_keys=True))
