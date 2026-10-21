"""Independent rational reconstruction of the printed endpoint matrices."""
from fractions import Fraction as F
from itertools import product


def matrix(rows):
    return [[F(value) for value in row] for row in rows]


def zeros(rows, columns):
    return [[F(0) for _ in range(columns)] for _ in range(rows)]


def transpose(rows):
    return [list(row) for row in zip(*rows)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def rank(rows):
    rows = [row[:] for row in rows]
    pivot_row = 0
    for column in range(len(rows[0])):
        candidates = [i for i in range(pivot_row, len(rows)) if rows[i][column]]
        if not candidates:
            continue
        selected = candidates[0]
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [x / pivot for x in rows[pivot_row]]
        for i in range(len(rows)):
            if i == pivot_row:
                continue
            scale = rows[i][column]
            rows[i] = [x - scale * y for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def contracted_cw(q, bar):
    out = zeros(q + 2, q + 2)
    out[0][0] = F(bar[-1])
    for i in range(1, q + 1):
        out[i][i] = F(bar[0])
        out[0][i] = out[i][0] = F(bar[i])
    out[0][q + 1] = out[q + 1][0] = F(bar[0])
    return out


def block_sum(a, b):
    n, m = len(a), len(b)
    out = zeros(n + m, n + m)
    for i in range(n):
        out[i][:n] = a[i]
    for i in range(m):
        out[n + i][n:] = b[i]
    return out


BARS = {
    6: ([-1, 1, -1, 3], [0, -1, -1, -1]),
    7: ([-1, 1, -1, -1, 4], [0, -1, -1, -1]),
    10: ([-1, 1, -1, 2], [0, -1, 0, -1]),
    11: ([-1, 1, -1, -1, 3], [0, -1, -1, -1])}
LEFT = {
    6: [[-F(1,3),1,0,0,0,0,0,0], [F(1,3),0,1,0,0,0,0,0], [F(1,3),0,0,1,0,0,0,0]],
    7: [[-F(1,4),1,0,0,0,0,0,0,0], [F(1,4),0,1,0,0,0,0,0,0], [F(1,4),0,0,1,0,0,0,0,0], [F(1,4),0,0,0,1,0,0,0,0]],
    10: [[-F(1,2),1,0,0,0,0,0,0], [F(1,2),0,1,0,0,0,0,0], [F(1,2),0,0,1,0,0,0,0]],
    11: [[-F(1,3),1,0,0,0,0,0,0,0], [F(1,3),0,1,0,0,0,0,0,0], [F(1,3),0,0,1,0,0,0,0,0], [F(1,3),0,0,0,1,0,0,0,0]]}
RIGHT = {
    6: [[F(1,2),-1,0,-1,F(3,2),0,0,0], [0,0,-1,1,0,0,0,0], [-1,-1,1,-5,0,0,0,0]],
    7: [[1,-1,0,0,-1,2,0,0,0], [0,0,-1,0,1,0,0,0,0], [0,0,0,-1,1,0,0,0,0], [-1,-1,1,1,-7,0,0,0,0]],
    10: [[1,-1,0,-1,2,0,0,0], [0,0,-1,1,0,0,0,0], [-1,-1,1,-4,0,0,0,0]],
    11: [[F(1,2),-1,0,0,-1,F(3,2),0,0,0], [0,0,-1,0,1,0,0,0,0], [0,0,0,-1,1,0,0,0,0], [-1,-1,1,1,-6,0,0,0,0]]}


def endpoint_audit():
    records = []
    for character in (6, 7, 10, 11):
        first, second = BARS[character]
        q, n1 = len(first) - 2, len(first)
        n = n1 + 4
        K = block_sum(contracted_cw(q, first), contracted_cw(2, second))
        EL, ER = matrix(LEFT[character]), matrix(RIGHT[character])
        DR = zeros(2, n)
        DR[0][0] = F(1)
        for i in (0, 1, 2):
            DR[0][n1 + i] = F(1)
        DR[1][n1 + 3] = F(1)
        DL = zeros(3 if character in (6, 7) else 4, n)
        DL[0][0] = DL[0][n1] = DL[1][1] = DL[1][n1 + 1] = F(1)
        if character in (6, 7):
            DL[2][n1 + 3] = F(1)
            if character == 7:
                DL[0][n1 + 2] = F(1)
        else:
            DL[3][n1 + 3] = F(1)
            if character == 10:
                DL[2][n1 + 2] = F(1)
        maps = [multiply(multiply(EL, K), transpose(ER)),
                multiply(multiply(EL, K), transpose(DR)),
                multiply(multiply(DL, K), transpose(ER)),
                multiply(multiply(DL, K), transpose(DR))]
        expected = [identity(len(EL)), zeros(len(EL), len(DR)),
                    zeros(len(DL), len(ER)), zeros(len(DL), len(DR))]
        records.append({
            'character': character,
            'endpoint_pairing_identity': maps[0] == expected[0],
            'cross_pairings_zero': [maps[i] == expected[i] for i in (1, 2, 3)],
            'clean_dimensions': [n - rank(multiply(K, transpose(DR))),
                                 n - rank(multiply(DL, K))],
            'dense_maps': {'left': [[int(x) for x in row] for row in DL],
                           'right': [[int(x) for x in row] for row in DR]}})
    return records


def crossed_group_audit():
    B = matrix([[0,1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0], [2,0,0,0,0,-1,1,0,0,0],
                [2,0,0,0,0,-1,0,1,0,0], [2,0,0,0,0,-1,0,0,1,0],
                [2,0,0,0,0,-1,0,0,0,1]])
    D = matrix([[0,0,0,0,0,0,1,0,0,-1], [0,0,0,0,0,0,0,1,0,-1],
                [0,0,0,0,0,0,0,0,1,-1], [0,1,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0], [0,0,0,1,0,0,0,0,0,0],
                [-F(1,2),-1,-1,-1,0,F(1,4),0,0,0,-F(1,4)]])
    J = zeros(10, 10)
    for i in range(5):
        J[i][i + 5] = J[i + 5][i] = F(1)
    characters = [0, 3, 4, 9, 12] * 2
    matrices = []
    for delta in range(16):
        weighted = [[value * (-1) ** ((characters[j] & delta).bit_count())
                     for j, value in enumerate(row)] for row in B]
        matrices.append(multiply(multiply(weighted, J), transpose(D)))
    failures = [[a, b] for a, b in product(range(16), repeat=2)
                if multiply(matrices[a], matrices[b]) != matrices[a ^ b]]
    return {'checked_group_laws': 256, 'failures': failures}
