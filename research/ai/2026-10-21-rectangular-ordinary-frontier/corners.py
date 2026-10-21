"""Coordinate certificates for the nested corner minor in the alternative proof."""
from itertools import combinations,product


def check(a,b,P,Q):
    rho=len(P)
    if not rho or len(Q)!=rho or len(set(P))!=rho or len(set(Q))!=rho:
        raise ValueError('Need distinct row and column indices of equal positive size')
    if any(not 0<=p<a for p in P) or any(not 0<=q<b for q in Q):raise ValueError('Hankel index outside source')
    m=a+b-1
    rows=[(j,p,r+b-1) for j in range(b) for r in range(a) for p in P]
    columns=[(j+a-1,q,r) for j in range(b) for r in range(a) for q in Q]
    if len(set(rows))!=a*b*rho or len(set(columns))!=a*b*rho:raise ArithmeticError('Repeated source index')
    if any(not(0<=j<b and 0<=p<a and 0<=L<m) for j,p,L in rows):raise ArithmeticError('Source row outside range')
    if any(not(0<=H<m and 0<=q<b and 0<=r<a) for H,q,r in columns):raise ArithmeticError('Source column outside range')
    zeros=0;diagonal=0
    # Check only the entries required for the two levels of block triangularity.
    for j,r,p,jp,rp,q in product(range(b),range(a),P,range(b),range(a),Q):
        i=a-1+jp-j;s=b-1+r-rp
        if jp>j or jp==j and r>rp:
            if 0<=i<a and 0<=s<b:raise ArithmeticError('A required block zero is a source coefficient')
            zeros+=1
        if jp==j and r==rp:
            if (i,s)!=(a-1,b-1) or not 0<=p+q<m:raise ArithmeticError('Diagonal block is not the Hankel minor')
            diagonal+=1
    return {'a':a,'b':b,'rho':rho,'P':list(P),'Q':list(Q),
            'source_minor_size':a*b*rho,'required_zero_entries':zeros,
            'repeated_diagonal_entries':diagonal,'determinant_power':a*b}


def report():
    cases=[]
    for a in range(2,6):
        for b in range(2,6):
            for P in combinations(range(a),2):
                for Q in combinations(range(b),2):cases.append(check(a,b,P,Q))
    for a,b in [(2,7),(7,2),(3,6),(6,3),(6,6),(8,8)]:
        for rho in [1,min(a,b)]:cases.append(check(a,b,range(rho),range(rho)))
    return {'scope':'Finite coordinate identities for the general written corner proof; all2-by2 Hankel minors for a,b2..5 and selected full-rank endpoints.',
            'cases_checked':len(cases),'required_zero_entries_checked':sum(c['required_zero_entries'] for c in cases),
            'repeated_diagonal_entries_checked':sum(c['repeated_diagonal_entries'] for c in cases),
            'cases':cases,'new_rank_inequality_claimed':False}
