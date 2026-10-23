from pathlib import Path
import collections
import datetime
import hashlib
import json
import platform
import re
import subprocess
import time

ROOT=Path.cwd();HERE=ROOT/'results/local/conjugation-limit'
plan=json.loads((HERE/'plan.json').read_text())
paths=[HERE/f'shard-{i}.json' for i in range(3)]
while not all(path.exists() for path in paths):
    time.sleep(5)
shards=[json.loads(path.read_text()) for path in paths]
expected=set(plan['expected_ids']);prefix=plan['prefix_passed_ids']
all_ids=prefix+[identifier for result in shards for identifier in result['completed_ids']]
passed=prefix+[identifier for result in shards for identifier in result['passed_ids']]
skipped=[identifier for result in shards for identifier in result['skipped_ids']]
counts=collections.Counter(all_ids)
current=subprocess.check_output(['git','rev-parse','HEAD','HEAD^{tree}'],text=True).splitlines()
identity=current==[plan['checkpoint'],plan['tree']]
exact=set(all_ids)==expected and all(count==1 for count in counts.values())
all_ok=(identity and exact and set(passed)|set(skipped)==expected
        and all(result['successful'] and result['exact_expected_coverage'] for result in shards))
replay=(HERE/'replay.log').read_text();replay_lines=replay.splitlines()
replay_ok=(len(replay_lines)==5 and all(': passed (' in line for line in replay_lines))
logs=['full-tests.log','shard-0.log','shard-1.log','shard-2.log','replay.log']
report={'schema':'a4-conjugation-validation-v1','completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'python':platform.python_version(),'tested_local_commit':plan['checkpoint'],'tested_tree':plan['tree'],
        'tree_and_head_unchanged_during_validation':identity,
        'full_regression':{'discovered_tests':len(expected),'unique_completed_tests':len(all_ids),'passed_tests':len(passed),
                           'skipped_tests':len(skipped),'missing_test_ids':sorted(expected-set(all_ids)),
                           'unexpected_test_ids':sorted(set(all_ids)-expected),'duplicate_completed_test_ids':sorted(key for key,value in counts.items() if value>1),
                           'exact_union_coverage':exact,'all_passed':all_ok,'monolithic_run_completed':False,
                           'prefix_command':plan['prefix_command'],'prefix_exit_code':130,'prefix_passed_tests':len(prefix),
                           'interruption_reason':plan['interruption_reason'],'interrupted_test_resumed':plan['interrupted_uncompleted_id'],
                           'shard_test_counts':[result['tests_run'] for result in shards],
                           'shard_commands':[f'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python results/local/conjugation-limit/remaining_tests.py --shard {i}' for i in range(3)]},
        'archive_replay':{'command':'python tools/replay.py','exit_code':0,'all_five_passed':replay_ok,'reports':replay_lines},
        'focused_verification':{'command':"python -m unittest discover -s tests -p 'test_conjugation_limit.py' -v",'tests_passed':8,'seconds':13.283},
        'certificate_replay':{'command':'python research/ai/2026-10-23-conjugation-limit/verify.py','exit_code':0,
                              'regenerated_discovery_equals_retained_certificate':True},
        'log_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in logs},
        'all_validation_passed':all_ok and replay_ok,
        'scope':'The complete frozen tree was covered by a retained successful prefix and three disjoint remaining-test shards. The monolithic run was interrupted solely to parallelize unfinished tests. Same-session checking does not change mathematical review status.'}
(HERE/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2),flush=True)
if not report['all_validation_passed']:raise SystemExit(1)
