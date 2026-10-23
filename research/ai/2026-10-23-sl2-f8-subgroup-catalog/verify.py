"""Independent completeness, integer upper bounds and nonzero-minor replay."""
import argparse
from collections import Counter
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]
spec=importlib.util.spec_from_file_location('f8_catalog_helpers',PACKAGE/'catalog.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)


def verify_lattice(G,rows):
    table=G['mul'];listed={tuple(r['members']) for r in rows}
    if len(listed)!=len(rows) or (0,) not in listed:raise ValueError('duplicate or missing subgroup')
    # Discovery multiplies on the right; acceptance closes on the left.
    def generated(generators):
        points={0};queue=[0]
        for x in queue:
            for g in generators:
                y=table[g][x]
                if y not in points:points.add(y);queue.append(y)
        return tuple(sorted(points))
    for row in rows:
        H,gens=row['members'],row['generators']
        if (H!=sorted(set(H)) or not H or H[0]!=0 or
                any(type(g) is not int or not 0<=g<504 for g in H+gens)
                or generated(gens)!=tuple(H)):
            raise ValueError('invalid subgroup generation witness')
        covered=set(H)
        for g in range(504):
            if g in covered:continue
            covered.update(table[g][h] for h in H)
            if generated(gens+[g]) not in listed:raise ValueError('missing generated extension')
    return listed


def verify_minor(cosets,selected,columns,dimension):
    if (len(selected)!=dimension or len(set(selected))!=dimension or
            len(columns)!=dimension or len(set(columns))!=dimension or
            any(type(i) is not int or not 0<=i<len(cosets) for i in selected) or
            any(type(j) is not int or not 0<=j<504 for j in columns)):
        raise ValueError('invalid lower-rank minor indices')
    positions={column:j for j,column in enumerate(columns)};basis={};prime=1009
    for i in selected:
        vector={positions[g]:1 for g in cosets[i] if g in positions}
        while vector:
            pivot=min(vector);coefficient=vector[pivot]
            if pivot not in basis:
                inverse=pow(coefficient,-1,prime)
                basis[pivot]={j:x*inverse%prime for j,x in vector.items()};break
            for j,value in basis[pivot].items():
                entry=(vector.get(j,0)-coefficient*value)%prime
                if entry:vector[j]=entry
                else:vector.pop(j,None)
        if not vector:raise ValueError('singular lower-rank minor')
    if len(basis)!=dimension:raise ValueError('incomplete lower rank')


def verify_dihedral14(G,H):
    table=G['mul'];inverse=G['inv']
    def powers(g):
        points=[0];x=g
        while x:
            points.append(x);x=table[x][g]
        return points
    torus=next((powers(g) for g in H if len(powers(g))==7),None)
    if torus is None:raise ValueError('order14 subgroup has no order7 torus')
    normalizer=sorted(g for g in range(504) if all(table[table[g][h]][inverse[g]] in torus for h in torus))
    if normalizer!=H:raise ValueError('order14 subgroup is not the full torus normalizer')
    generator=torus[1]
    reflection=next((g for g in H if g not in torus and table[g][g]==0
                     and table[table[g][generator]][inverse[g]]==inverse[generator]),None)
    if reflection is None:raise ValueError('missing dihedral reflection relation')
    return {'torus_order':7,'normalizer_order':14,'dihedral_relation_verified':True}


def verify_minimal_summaries(classes,shape,saved):
    if len(saved)!=3:raise ValueError('three target legs required')
    totals=[];new_totals=[]
    for leg,entries in enumerate(saved):
        other=shape[(leg+1)%3]*shape[(leg+2)%3]
        eligible=[r for r in classes if r['order']<=shape[leg] and r['dimension']<other]
        selected=[]
        for item in entries:
            matches=[r for r in eligible if
                     item=={'subgroup_order':r['order'],'ideal_dimension':r['dimension'],
                            'conjugate_subgroups':len(r['conjugates']),'cosets':len(r['cosets'])}]
            if len(matches)!=1 or matches[0] in selected:raise ValueError('invalid minimal class')
            selected.append(matches[0])
        # Containment is tested independently of discovery's filtering order.
        # A coset of a proper subgroup fits inside H iff a conjugate subgroup
        # fits inside H; all conjugates occur in the completed class catalog.
        for r in selected:
            if any(set(K)<=set(r['subgroup']) for q in eligible if q['order']<r['order']
                   for K in q['conjugates']):raise ValueError('nonminimal reported class')
        for r in eligible:
            if r in selected:continue
            if not any(set(K)<=set(r['subgroup']) for q in selected if q['order']<r['order']
                       for K in q['conjugates']):raise ValueError('missing minimal class')
        totals.append(sum(len(r['cosets']) for r in selected))
        new_totals.append(sum(len(r['cosets']) for r in selected if r['order'] not in [8,9,18]))
    return {'shape':shape,'minimal_cosets_per_leg':totals,'new_cosets_per_leg':new_totals}


def check_sources():
    pins=json.loads((PACKAGE/'sources.json').read_text())
    for row in pins['sources']:
        if hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()!=row['sha256']:
            raise ValueError('adopted source pin changed')


def verify_new_cut_control(classes,control):
    if control['shape']!=[18,18,25] or control['leg']!=0:
        raise ValueError('wrong control target')
    points=control['vertex_set']
    if (len(points)!=18 or points!=sorted(set(points)) or
            any(type(g) is not int or not 0<=g<504 for g in points)):
        raise ValueError('invalid control vertex set')
    points=set(points)
    if any(set(C)<=points for r in classes if r['order'] in [8,9,18] for C in r['cosets']):
        raise ValueError('control already violates a prior full-coset filter')
    if not any(set(C)<=points for r in classes if r['order']==14 for C in r['cosets']):
        raise ValueError('control does not exhibit the new dihedral cut')
    return {'prior_8_9_18_coset_filters_pass':True,'new_order14_filter_rejects':True,
            'scope':'one vertex-set filter control; no pair-injective target construction'}


def verify(report):
    check_sources()
    contract={'schema':'sl2-f8-subgroup-ideal-catalog-v1','group':'SL(2,F8)','prime':1009,
              'general_complex_maps_excluded':False,'all_coordinate_targets_excluded':False,
              'independent_review':False,'lean_formalized':False,'improves_omega':False}
    if (set(report)!=set(contract)|{'subgroups','ideal_classes','formats','new_cut_control'} or
            any(report[k]!=v for k,v in contract.items())):raise ValueError('source or scope contract changed')
    shapes=json.loads((ROOT/'results/semisimple-koszul-2026-10-21/frontiers.json').read_text())['sources'][1]['koszul_surviving_shapes']
    if [r['shape'] for r in report['formats']]!=shapes:raise ValueError('target frontier incomplete or changed')
    G=helper.projection.group();listed=verify_lattice(G,report['subgroups'])
    assigned=set();classes=[]
    for record in report['ideal_classes']:
        H=record['subgroup'];dimension=record['ideal_dimension']
        receipt=helper.projection.verify_projection(H,record['central_projection'],dimension)
        conjugates,cosets=helper.conjugates_and_cosets(G,H)
        members=set(conjugates)
        if members&assigned or not members<=listed:raise ValueError('duplicate or unlisted subgroup class')
        assigned.update(members)
        verify_minor(cosets,record['lower_minor_cosets'],record['lower_minor_columns'],dimension)
        classes.append({'subgroup':H,'order':len(H),'dimension':receipt['ideal_dimension_upper_bound'],
                        'conjugates':conjugates,'cosets':cosets})
    dihedral=verify_dihedral14(G,next(r['subgroup'] for r in classes if r['order']==14))
    if assigned!=listed:raise ValueError('classes omit part of the subgroup lattice')
    summaries=[verify_minimal_summaries(classes,r['shape'],r['minimal_cuts']) for r in report['formats']]
    control=verify_new_cut_control(classes,report['new_cut_control'])
    return {'verified':True,'group':'SL(2,F8)','subgroups':len(listed),'conjugacy_classes':len(classes),
            'order_histogram':dict(sorted(Counter(len(H) for H in listed).items())),
            'class_dimensions':[{'subgroup_order':r['order'],'ideal_dimension':r['dimension'],
                                 'conjugates':len(r['conjugates']),'cosets':len(r['cosets'])} for r in classes],
            'target_formats':len(summaries),'formats':summaries,
            'new_cut_control':control,
            'dihedral14_structure':dihedral,
            'general_complex_maps_excluded':False,'all_coordinate_targets_excluded':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate',type=Path);parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    with gzip.open(args.certificate,'rt') as handle:report=json.load(handle)
    receipt=verify(report);text=json.dumps(receipt,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')
