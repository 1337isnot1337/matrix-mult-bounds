"""Report the full scaled-tensor error of a frozen complex numerical pilot.

This is a floating diagnostic, never a degeneration acceptance test.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import logsumexp
from numerical_common import transform


def evaluate(path):
    data = json.loads(path.read_text())
    m, B = data['m'], data['B']
    coordinates = [(a, degree-a) for degree in range(m) for a in range(degree+1)]
    eta, beta = data['eta'], data.get('beta', 1)
    wy = np.array([eta[a+b]-beta*a for a,b in coordinates])
    wz = np.array([-eta[m-1-c-d]-beta*c for c,d in coordinates])
    weights = beta*np.arange(m)[:, None, None]+wy[None, :, None]+wz[None, None, :]
    target = np.array([[[int(p==a+c and a+b+c+d==m-1) for c,d in coordinates]
                        for a,b in coordinates] for p in range(m)])
    denominator = np.sum(target**2)
    reports = []
    for report in data['reports']:
        matrices = [np.array(report[key+'_real'])+1j*np.array(report[key+'_imag'])
                    for key in ['A', 'B', 'C']]
        error = transform(*matrices)-target
        mask = np.abs(error)>0
        coefficients, powers = 2*np.log(np.abs(error[mask])), weights[mask]
        objective = lambda log_epsilon: logsumexp(coefficients+2*powers*log_epsilon)
        optimum = minimize_scalar(objective, bounds=(-10, 0), method='bounded')
        x = min([float(optimum.x), -10.0, 0.0], key=objective)
        reports.append({'index':report['index'], 'epsilon':float(np.exp(x)),
                        'log_epsilon_interval':[-10, 0],
                        'full_relative_error':float(np.exp((objective(x)-np.log(denominator))/2)),
                        'masked_relative_error':float(np.linalg.norm(error[weights<=0])/np.sqrt(denominator))})
    return {'input':path.name, 'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'scope':'Floating full-error diagnostic on a bounded log-parameter interval.',
            'reports':reports, 'certified_degeneration':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    text = json.dumps(evaluate(args.input), indent=2)+'\n'
    args.output.write_text(text)
    print(text, end='')
