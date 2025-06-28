import numpy as np

def compute_pca(data):
    m = np.mean(data,axis=0)
    datac = np.array([obs - m for obs in data])
    T = np.dot(datac,datac.T)
    [u,s,v] = np.linalg.svd(T)

    pcs = [np.dot()]