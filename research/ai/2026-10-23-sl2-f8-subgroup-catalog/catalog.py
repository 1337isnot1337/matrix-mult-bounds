"""Discover the complete SL(2,F8) subgroup/averaging-ideal catalog.

The lattice construction follows the credited central-cover catalog.
Acceptance is separate: integer central projections and modular minors.
"""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]
PRIOR=PACKAGE.parent/'2026-10-21-sl2-f8-ideals/sl2_f8_ideal_certificate.py'
spec=importlib.util.spec_from_file_location('f8_catalog_projection',PRIOR)
projection=importlib.util.module_from_spec(spec);spec.loader.exec_module(projection)


def closure(G,generators):
    members={0};queue=[0]
    for x in queue:
        for g in generators:
            y=G['mul'][x][g]
            if y not in members:members.add(y);queue.append(y)
    return tuple(sorted(members))


def lattice(G):
    found={(0,):()};queue=[(0,)]
    for H in queue:
        covered=set(H)
        for g in range(504):
            if g in covered:continue
            covered.update(G['mul'][h][g] for h in H)
            generators=found[H]+(g,);K=closure(G,generators)
            if K not in found:found[K]=generators;queue.append(K)
    return [{'members':list(H),'generators':list(gens)}
            for H,gens in sorted(found.items(),key=lambda row:(len(row[0]),row[0]))]


def conjugates_and_cosets(G,H):
    table=G['mul'];inverse=G['inv']
    conjugates=sorted({tuple(sorted(table[table[g][h]][inverse[g]] for h in H)) for g in range(504)})
    cosets=sorted({tuple(sorted(table[g][h] for h in K)) for K in conjugates for g in range(504)})
    return conjugates,cosets


def rank_witness(rows,ceiling,prime=1009):
    basis=[];chosen=[]
    for i,row in enumerate(rows):
        vector={j:1 for j in row}
        for pivot,previous in basis:
            factor=vector.get(pivot,0)
            if not factor:continue
            for j,value in previous.items():
                entry=(vector.get(j,0)-factor*value)%prime
                if entry:vector[j]=entry
                else:vector.pop(j,None)
        if vector:
            pivot=min(vector);scale=pow(vector[pivot],-1,prime)
            basis.append((pivot,{j:x*scale%prime for j,x in vector.items()}));chosen.append(i)
        if len(basis)==ceiling:break
    if len(basis)!=ceiling:raise ValueError('could not match the projection upper rank')
    return chosen,[p for p,_ in basis]


def minimal_summary(G,records,shape):
    classes=[]
    for record in records:
        conjugates,cosets=conjugates_and_cosets(G,record['subgroup'])
        classes.append((record,conjugates,len(cosets)))
    result=[]
    for leg in range(3):
        other=shape[(leg+1)%3]*shape[(leg+2)%3]
        eligible=[r for r,_,_ in classes if len(r['subgroup'])<=shape[leg] and r['ideal_dimension']<other]
        minimal=[]
        for record,conjugates,count in classes:
            if record not in eligible:continue
            H=set(record['subgroup'])
            proper=[r for r in eligible if len(r['subgroup'])<len(H)]
            if any(set(K)<=H for r in proper for K in conjugates_and_cosets(G,r['subgroup'])[0]):continue
            minimal.append({'subgroup_order':len(H),'ideal_dimension':record['ideal_dimension'],
                            'conjugate_subgroups':len(conjugates),'cosets':count})
        result.append(minimal)
    return result


def derive():
    G=projection.group();subgroups=lattice(G)
    source=json.loads((ROOT/'results/semisimple-koszul-2026-10-21/sl2-f8-source.json').read_text())
    _,labels,_=projection.class_data();remaining={tuple(r['members']) for r in subgroups};records=[]
    while remaining:
        H=min(remaining,key=lambda H:(len(H),H));conjugates,cosets=conjugates_and_cosets(G,H)
        remaining.difference_update(conjugates)
        z=[Fraction(0)]*9
        for row in source['rational_central_blocks']:
            e=list(map(Fraction,row['central_idempotent']))
            if any(sum((e[labels[G['mul'][g][G['inv'][h]]]] for h in H),Fraction(0)) for g in range(504)):
                z=[a+b for a,b in zip(z,e)]
        upper=504*z[0]
        if upper.denominator!=1:raise ValueError('nonintegral proposed projection rank')
        projection.verify_projection(list(H),list(map(str,z)),int(upper))
        selected,columns=rank_witness(cosets,int(upper))
        records.append({'subgroup':list(H),'ideal_dimension':int(upper),
                        'central_projection':list(map(str,z)),
                        'lower_minor_cosets':selected,'lower_minor_columns':columns})
        print('class',len(records),'order',len(H),'conjugates',len(conjugates),
              'cosets',len(cosets),'exact ideal',int(upper),flush=True)
    frontier=json.loads((ROOT/'results/semisimple-koszul-2026-10-21/frontiers.json').read_text())['sources'][1]
    shapes=frontier['koszul_surviving_shapes']
    H14=next(r['subgroup'] for r in records if len(r['subgroup'])==14)
    control=sorted(H14+[g for g in range(504) if g not in H14][:4])
    return {'schema':'sl2-f8-subgroup-ideal-catalog-v1','group':'SL(2,F8)','prime':1009,
            'subgroups':subgroups,'ideal_classes':records,
            'formats':[{'shape':s,'minimal_cuts':minimal_summary(G,records,s)} for s in shapes],
            'new_cut_control':{'shape':[18,18,25],'leg':0,'vertex_set':control},
            'general_complex_maps_excluded':False,'all_coordinate_targets_excluded':False,
            'independent_review':False,'lean_formalized':False,'improves_omega':False}


if __name__=='__main__':
    import argparse,gzip
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    report=derive();args.output.parent.mkdir(parents=True,exist_ok=True)
    with gzip.GzipFile(args.output,'wb',mtime=0) as handle:handle.write(json.dumps(report,separators=(',',':')).encode())
