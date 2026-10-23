from pathlib import Path
from datetime import datetime,timezone
from copy import deepcopy
import argparse,hashlib,json,subprocess,sys
P=Path(__file__).resolve().parent;BASE='6b57043164f7d534b858507a37f64fdfda38f29f';MAIN='a510bec4627043b35bac0ad4b19bb617446e8949';PREFIX='docs/consolidation/2026-10-23/'
SELF={PREFIX+n for n in ['central_resolution_manifest.json','preservation_report.json','packaged_evidence_index.json']}
sha=lambda b:hashlib.sha256(b).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
a=argparse.ArgumentParser();a.add_argument('--repo',default=str(P/'concurrent_wave_repo'));a.add_argument('--commit',required=True);a.add_argument('--superseding-report',action='append',default=[]);args=a.parse_args()
def git(*x):return subprocess.check_output(['git','-C',args.repo,*x])
old=git('show',BASE+':'+PREFIX+'central_resolution_manifest.json');prior=json.loads(old);outputs={x['path']:deepcopy(x) for x in prior['outputs']};superseded=deepcopy(prior['superseded_outputs']);conflicts=set(prior['covered_conflicts']);decisions={x['path']:deepcopy(x) for x in prior['conflict_decisions']};inputs={'git:'+BASE+':'+PREFIX+'central_resolution_manifest.json':sha(old)}
logs=['merge_log.json','catchup_merge_log.json','final_catchup_merge_log.json','late_merge_log.json','receipt_merge_log.json','postvalidation_merge_log.json','closure_merge_log.json','nextwave_merge_log.json','nextwave_concurrent_merge_log.json','main_advance_merge_log.json','concurrent_434_merge_log.json','live_catchup_merge_log.json','main_advance_6e11f7c1_merge_log.json','quadratic_followup_merge_log.json','structural_followup_merge_log.json','balanced_followup_merge_log.json','concurrent_wave_merge_log.json']
for n in logs:
 raw=(P/n).read_bytes();inputs[n]=sha(raw)
 for row in json.loads(raw):conflicts.update(row.get('provisional_conflicts',row.get('conflicts',[])))
reports=['concurrent_wave_source_resolution.json','concurrent_wave_docs_resolution.json','concurrent_wave_integration_resolution.json']+args.superseding_report
for name in reports:
 raw=(P/name).read_bytes();inputs[name]=sha(raw)
 for r in json.loads(raw)['output_files']:
  row=deepcopy(r);path=row['path'];assert row['reason'];decisions[path]={'path':path,'resolution_report':name,'decision':row['reason']}
  if path in SELF:continue
  oldrow=outputs.get(path)
  if oldrow and oldrow['sha256']!=row['sha256']:superseded.append({'path':path,'previous_sha256':oldrow['sha256'],'previous_report':oldrow.get('report'),'final_sha256':row['sha256'],'final_report':name,'reason':row['reason']})
  row['report']=name;row['origins']=(oldrow or {}).get('origins',[])+[{k:row[k] for k in ['source_commit','source_path','report','reason'] if k in row}];outputs[path]=row
claimpath=P/'concurrent_wave_claims_output/resolution_report.json';inputs[str(claimpath)]=sha(claimpath.read_bytes());heads=json.loads((P/'concurrent_wave_heads.json').read_bytes())
manifest=deepcopy(prior);manifest.update(assembled_at=datetime.now(timezone.utc).isoformat(),prior_reviewed_union=BASE,current_main=MAIN,latest_sources=[h['sha'] for h in heads],topic_source_snapshots=176,topic_branch_names=142,outputs=[outputs[p] for p in sorted(outputs)],covered_conflicts=sorted(conflicts),superseded_outputs=superseded,inputs=inputs,method='Preserve every earlier source and resolution; apply78 exact authored leaf paths, four independently reviewed shared narratives, five exact unreviewed claims and two authored limitations revisions. All614 existing status flags remain unchanged; imported older variants do not replace current corrections.')
manifest['conflict_decisions']=[decisions[p] for p in sorted(conflicts)];write(P/'concurrent_wave_resolution_manifest.json',manifest)
archive=json.loads((P/'archive_concurrent_wave_tags.json').read_bytes());assert archive['verified'];write(P/'archive_concurrent_wave_tags.normalized.json',archive['archives'])
plans=['catchup_plan.json','final_catchup_plan.json','supplemental_catchup_plan.json','late_catchup_plan.json','receipt_catchup_plan.json','claims_output/postvalidation_plan.json','claims_output/closure_plan.json','nextwave_plan.json','live_catchup_plan.json','quadratic_followup_plan.json','structural_followup_plan.json','balanced_followup_plan.json','concurrent_wave_plan.json']
archives=['archive_tags.json','archive_update_tags.json','archive_final_tags.json','archive_shift_window_tags.json','archive_late_tags.json','archive_receipt_tags.json','archive_postvalidation_tags.normalized.json','archive_closure_tags.normalized.json','archive_nextwave_tags.normalized.json','archive_live_catchup_tags.normalized.json','archive_quadratic_c7.normalized.json','archive_quadratic_80bd.normalized.json','archive_quadratic_f006.normalized.json','archive_concurrent_wave_tags.normalized.json']
out=P/'concurrent_wave_preservation_report.json';cmd=[sys.executable,str(P/'claims_output/audit_preservation.py'),'--repo',args.repo,'--commit',args.commit,'--snapshot',str(P/'snapshot.json'),'--claims-report',str(claimpath),'--resolutions',str(P/'concurrent_wave_resolution_manifest.json'),'--conflicts',str(P/'provisional_conflicts.json'),'--output',str(out)]
for opt,names in [('--catchup',plans),('--archive-tags',archives),('--merge-log',logs)]:
 for n in names:cmd += [opt,str(P/n)]
subprocess.run(cmd,check=True);audit=json.loads(out.read_bytes());assert audit['status']=='passed' and audit['archive_tag_receipts_checked']==176 and audit['final_claim_ids']==619
for c in [BASE,MAIN]+[h['sha'] for h in heads]:git('merge-base','--is-ancestor',c,args.commit)
final=git('show',args.commit+':research/claims.json');assert final==(P/'concurrent_wave_claims_output/claims.json').read_bytes();before={r['id']:r for r in json.loads(git('show',BASE+':research/claims.json'))['claims']};after={r['id']:r for r in json.loads(final)['claims']};assert len(before)==614 and len(after)==619
changed={k for k in before if before[k]!=after[k]};assert changed=={'AI-A4-TWOSIDED-LOWRANK-003','AI-A4-TWOSIDED-RANKLOSS-001'}
for cid in before:
 for k in ['status','evidence','independent_review','lean_formalized','improves_omega']:assert before[cid].get(k)==after[cid].get(k),(cid,k)
write(P/'concurrent_wave_history_receipt.json',{'status':'passed','head':args.commit,'baseline':BASE,'current_main':MAIN,'source_heads':[h['sha'] for h in heads],'all_source_histories_are_ancestors':True,'source_snapshots':176,'topic_branch_names':142,'claim_records':619,'unchanged_existing_records':612,'new_claims':sorted(set(after)-set(before)),'revised_existing_ids':sorted(changed),'all_existing_status_flags_preserved':True,'source_exact_leaf_outputs':78,'new_merge_conflict_events':7,'unique_conflict_paths_covered':len(conflicts),'preservation_report_sha256':sha(out.read_bytes()),'recorded_at':datetime.now(timezone.utc).isoformat()})
print(json.dumps({'status':'passed','head':args.commit,'snapshots':176,'claims':619,'outputs':len(outputs)}))
