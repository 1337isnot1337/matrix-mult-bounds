"""Standard-library guarded lexicographic CNF for search symmetry leaders."""


def lex_geq(left,right,guard,new_variable):
    if len(left)!=len(right):raise ValueError('equal vector lengths required')
    clauses=[];prefix=guard
    different=[(x,y) for x,y in zip(left,right) if x!=y]
    for pos,(x,y) in enumerate(different):
        clauses.append([-prefix,x,-y])
        if pos+1==len(different):break
        nxt=new_variable()
        # nxt iff prefix and (x iff y).
        clauses.extend([[-nxt,prefix],[-nxt,-x,y],[-nxt,x,-y],
                        [-prefix,-x,-y,nxt],[-prefix,x,y,nxt]])
        prefix=nxt
    return clauses
