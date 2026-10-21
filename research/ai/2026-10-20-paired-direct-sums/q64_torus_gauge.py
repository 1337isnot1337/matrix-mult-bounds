"""Optional minimum-norm representative for the physical diagonal target gauge.

The 14 physical diagonal parameters have one kernel; z_4=0 leaves 13.
At a stationary point the three complete map norms are equal, and the
derivative along every physical diagonal gauge, including the Laurent
grading, vanishes. This gauge does not establish any coefficient identity.
"""
import numpy as np


def characters():
    q=[]
    for i in range(5):
        for k in range(5):
            row=np.zeros(13);row[i]=1
            if k<4:row[9+k]=1
            q.append(row)
    for i in range(5):
        for j in range(4):
            row=np.zeros(13);row[i]=-1;row[5+j]=1;q.append(row)
    for j in range(4):
        for k in range(5):
            row=np.zeros(13);row[5+j]=-1
            if k<4:row[9+k]=-1
            q.append(row)
    return np.array(q)


Q=characters()


def normalize(maps,tolerance=1e-13):
    raw=np.concatenate(maps,axis=0)
    energy=np.sum(np.abs(raw)**2,axis=1)
    if np.any(energy==0):
        raise ValueError('This normalization requires every target row to be nonzero.')
    s=np.zeros(13)
    for iteration in range(100):
        weighted=energy*np.exp(2*(Q@s))
        objective=float(np.sum(weighted))
        d=Q.T@weighted
        h=Q.T@(weighted[:,None]*Q)
        stationarity=float(np.max(np.abs(d))/objective)
        if stationarity<tolerance:
            break
        step=-0.5*np.linalg.solve(h,d)
        derivative=float(2*d@step)
        fraction=1.0
        for _ in range(60):
            trial=s+fraction*step
            value=float(np.sum(energy*np.exp(2*(Q@trial))))
            if np.isfinite(value) and value<=objective+1e-4*fraction*derivative:
                s=trial
                break
            fraction*=0.5
        else:
            if stationarity<1e-11:
                break
            raise ArithmeticError('The convex torus normalization did not descend.')
    else:
        raise ArithmeticError('The convex torus normalization did not converge.')
    scaling=np.exp(Q@s)
    normalized=raw*scaling[:,None]
    final_energy=np.sum(np.abs(normalized)**2,axis=1)
    h=Q.T@(final_energy[:,None]*Q)
    stationarity=float(np.max(np.abs(Q.T@final_energy))/np.sum(final_energy))
    pieces=[normalized[:25],normalized[25:45],normalized[45:]]
    return pieces,{'scaling':scaling,'normalized':normalized,'moment_gram':h,
                   'log_gauge_parameters':s,'iterations':iteration,
                   'relative_stationarity':stationarity,
                   'norm_before':float(np.linalg.norm(raw)),
                   'norm_after':float(np.linalg.norm(normalized))}


def pullback(gradients,data):
    g=np.concatenate(gradients,axis=0)
    n=data['normalized']
    row_inner=np.sum((g.conj()*n).real,axis=1)
    multiplier=np.linalg.solve(data['moment_gram'],Q.T@row_inner)
    pulled=data['scaling'][:,None]*(g-(Q@multiplier)[:,None]*n)
    return [pulled[:25],pulled[25:45],pulled[45:]]
