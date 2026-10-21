"""Optional numerical physical parabolic gauge; zero-set preserving only.

For increasing alpha, beta, gamma in powers (-alpha-gamma, alpha-beta,
beta+gamma), all three physical pair matrices below are upper triangular.
"""
import numpy as np
from narrow_rectangle_balanced import covariance,positive_power,apply_axis


def pair(left,la,right,ra):
    g=covariance(left,la)
    h=covariance(right,ra).conj()
    gh=positive_power(g,0.5)
    gm=positive_power(g,-0.5)
    x=gm@positive_power(gh@h@gh,0.5)@gm
    x=positive_power((x+x.conj().T)/2,1)
    # G*G=X. Upper triangular Cholesky factors attain the same norm minimum
    # as the positive square-root factor, while preserving the full flag.
    transform=np.linalg.cholesky(x).conj().T
    return apply_axis(transform,left,la),apply_axis(np.linalg.inv(transform).T,right,ra)


def gauge(maps):
    a=maps[0].reshape(5,5,-1)
    b=maps[1].reshape(5,4,-1)
    c=maps[2].reshape(4,5,-1)
    for _ in range(2):
        a,b=pair(a,0,b,0)
        b,c=pair(b,1,c,0)
        a,c=pair(a,1,c,1)
    return [x.reshape(old.shape) for x,old in zip([a,b,c],maps)]
