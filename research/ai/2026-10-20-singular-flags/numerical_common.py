"""Optional numerical helpers; exact acceptance never depends on this module."""
import numpy as np


def transform(A,Y,Z):
    m,B=A.shape[1],Y.shape[1]
    result=np.zeros((A.shape[0],Y.shape[0],Z.shape[0]),dtype=np.result_type(A,Y,Z))
    for p in range(m):result+=A[:,p,None,None]*(Y@Z[:,p:p+B].T)[None,:,:]
    return result
