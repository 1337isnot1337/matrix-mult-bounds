"""Exact group F8^2 semidirect F8*, of order 448, over complex group algebra."""


def fm(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&8:a^=11
    return out


def inverse(a):
    if not 1<=a<8:raise ValueError('nonzero F8 element required')
    a2=fm(a,a);return fm(fm(a2,a2),a2)


def scale(a,v):
    out=0;j=0
    while v:
        out|=fm(a,v&7)<<(3*j);v>>=3;j+=1
    return out


def group():
    elements=[(a,v) for a in range(1,8) for v in range(64)]
    index={x:i for i,x in enumerate(elements)}
    table=[[index[(fm(a,b),v^scale(a,w))] for b,w in elements] for a,v in elements]
    inverses=[index[(inverse(a),scale(inverse(a),v))] for a,v in elements]
    return {'name':'F8^2:C7','matrices':elements,'mul':table,'inv':inverses,
            'normal_order':64,'index':7,'identity':0,
            'irreducible_degrees':[1]*7+[7]*9}


class ProductRow:
    def __init__(self,a,v,order,scales,scalars):
        self.a=a;self.v=v;self.order=order;self.scales=scales;self.scalars=scalars

    def __getitem__(self,index):
        b,w=divmod(index,self.order)
        return (self.scalars[self.a][b+1]-1)*self.order+(self.v^self.scales[self.a][w])


def cubic_group():
    """Lazy exact multiplication table avoids 12.8 million stored entries."""
    order=512
    elements=[(a,v) for a in range(1,8) for v in range(order)]
    scalars=[[fm(a,b) for b in range(8)] for a in range(8)]
    scales=[[scale(a,v) for v in range(order)] for a in range(8)]
    table=[ProductRow(a,v,order,scales,scalars) for a,v in elements]
    inverses=[(inverse(a)-1)*order+scale(inverse(a),v) for a,v in elements]
    return {'name':'F8^3:C7','matrices':elements,'mul':table,'inv':inverses,
            'normal_order':order,'index':7,'identity':0,
            'irreducible_degrees':[1]*7+[7]*73}


def cubic_parent(G):
    """Three pair-injective 56-point sets, before selecting holes."""
    index={x:i for i,x in enumerate(G['matrices'])};sets=[[],[],[]]
    for a in range(1,8):
        a2=fm(a,a)
        for x in range(8):
            sets[0].append(index[(a,x|(a2<<3))])
            sets[1].append(index[(a,(x<<3)|(a2<<6))])
            sets[2].append(index[(a,a2|(x<<6))])
    return sets
