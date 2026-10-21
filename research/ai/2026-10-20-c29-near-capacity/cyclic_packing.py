"""Complete cyclic-translation mask packing, with exact orbit normalization."""


def rotate(mask, shift, order):
    shift %= order
    return ((mask << shift) | (mask >> (order-shift))) & ((1 << order)-1)


def options(points, order):
    if len(set(points)) != len(points):
        raise ValueError('distinct residue points required')
    if any(not isinstance(v,int) or not 0 <= v < order for v in points):
        raise ValueError('invalid residue')
    mask = sum(1 << v for v in points)
    return sorted({rotate(mask,t,order) for t in range(order)})


def pack(rows, order):
    if order < 1 or not rows or any(not row for row in rows):
        raise ValueError('nonempty domains and positive cyclic order required')
    rows = [sorted(set(row)) for row in rows]
    limit = 1 << order
    for row in rows:
        if any(not isinstance(v,int) or not 0 <= v < limit for v in row):
            raise ValueError('invalid mask')
        if set(row) != {rotate(row[0],t,order) for t in range(order)}:
            raise ValueError('complete cyclic translation orbit required')
    failed = set()
    nodes = 0

    def visit(remaining, used):
        nonlocal nodes
        nodes += 1
        if not remaining:
            return {}
        state = remaining,used
        if state in failed:
            return None
        domains = [(i,[v for v in rows[i] if not v & used]) for i in remaining]
        i,domain = min(domains,key=lambda pair:len(pair[1]))
        for value in domain:
            result = visit(tuple(j for j in remaining if j != i),used | value)
            if result is not None:
                result[i] = value
                return result
        failed.add(state)
        return None

    selected = visit(tuple(range(1,len(rows))),rows[0][0])
    if selected is not None:
        selected[0] = rows[0][0]
    return {'satisfiable':selected is not None,
            'selected_masks':[selected[i] for i in range(len(rows))] if selected is not None else None,
            'search_nodes':nodes}
