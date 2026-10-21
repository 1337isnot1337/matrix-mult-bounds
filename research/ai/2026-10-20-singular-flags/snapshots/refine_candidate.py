import hashlib
import json
from pathlib import Path
import numpy as np
import refine_core

source = Path('/home/cinna/matrix-mult-schur-20261020/results/mixed-restrictions-2026-10-20/border-fit-m4.json')
data=json.loads(source.read_text())
best=min(data['reports'],key=lambda r:r['best']['relative_residual'])
report=refine_core.fit(4,10,best['order'],3000,best['seed'],ridge=1e-14,start=best['best'])
report['input_report_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
report['input_best_residual']=best['best']['relative_residual']
report['numpy_version']=np.__version__
report['discovery_only']=True
Path('/tmp/matrix-mult-source-20261020/refined-m4.json').write_text(json.dumps(report,indent=2)+'\n')
print('best',report['best']['relative_residual'],flush=True)
