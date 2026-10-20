"""Exact offset gauges for constant direction planes in F8^2:C7."""
from octal_group import inverse,scale


def normalize(base,offsets):
    right=[row[1] for row in offsets]
    shifted=[{a:v^scale(a,right[f]) for a,v in row.items()} for f,row in enumerate(offsets)]
    # In characteristic two, 1-2=1+2=3 in the chosen field labels.
    conjugator=scale(inverse(3),shifted[0][2])
    result=[{a:v^scale(1^a,conjugator) for a,v in row.items()} for row in shifted]
    for f in range(3):
        u=base[2*f];bit=u&-u
        for a in [6,7]:
            if result[f][a]&bit:result[f][a]^=u
    return {'offsets':result,'right_translation_vectors':right,
            'common_translation_conjugator':conjugator}


def point_sets(base,offsets):
    return [[(a-1)*64+(v^offsets[f][a])
             for a in range(1,8)
             for v in ([0,*base[2*f:2*f+2]] if a<6 else [0,base[2*f]])]
            for f in range(3)]
