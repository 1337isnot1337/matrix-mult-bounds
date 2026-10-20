"""Complete integer backtracking for disjoint translated finite masks.

Options must be the complete translation orbit of each mask on an elementary
abelian 2-group. Simultaneously translating a packing normalizes its first
mask to the first listed option. No SAT solver or numerical arithmetic.
"""


def exact_pack(options):
    if not options or any(not row for row in options):raise ValueError('nonempty option families required')
    options=[tuple(sorted(set(row))) for row in options]
    if any(not isinstance(v,int) or v<0 for row in options for v in row):
        raise ValueError('nonnegative integer masks required')
    # Explicitly check the translation-orbit hypothesis used to fix row zero.
    width=max(v.bit_length() for row in options for v in row)
    order=1
    while order<width:order*=2
    for row in options:
        points=[h for h in range(order) if row[0]&(1<<h)]
        orbit={sum(1<<(v^h) for h in points) for v in range(order)}
        if set(row)!=orbit:raise ValueError('options are not a complete XOR translation orbit')
    failed=set();counts={'nodes':0,'branches':0,'memo_hits':0}
    def visit(remaining,used):
        counts['nodes']+=1
        if not remaining:return {}
        state=(remaining,used)
        if state in failed:counts['memo_hits']+=1;return None
        best=None;domain=None
        for i in remaining:
            candidates=[v for v in options[i] if not v&used]
            if not candidates:failed.add(state);return None
            if domain is None or len(candidates)<len(domain):best=i;domain=candidates
        rest=tuple(i for i in remaining if i!=best)
        for value in domain:
            counts['branches']+=1
            result=visit(rest,used|value)
            if result is not None:result[best]=value;return result
        failed.add(state);return None
    found=visit(tuple(range(1,len(options))),options[0][0])
    selected=None
    if found is not None:
        found[0]=options[0][0];selected=[found[i] for i in range(len(options))]
    return {'satisfiable':selected is not None,'selected_masks':selected,
            'search_counts':counts,'failed_states':len(failed),
            'method':'Complete exact backtracking with first-mask translation normalization'}
