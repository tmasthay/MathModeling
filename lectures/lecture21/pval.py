import numpy as np
import itertools
import scipy

def generate_model(x):
    alpha = 0.0
    beta = 2.0
    return alpha + beta * x

def generate_noise(N):
    mu = 0.0
    sig = 1.0
    return np.random.normal(mu, sig, (N,))

def go():
    p = 2
   
    #define grid 
    a = 0.0
    b = 1.0
    n_pts = 100
    x = np.linspace(a,b,n_pts)

    f = generate_model(x)
    eta = generate_noise(len(x))
    obs = f + eta

    all_indices = set(range(n_pts))
    indices = set(itertools.combinations(all_indices, p))

    cross_loss = 0.0

    for idx in indices:
        train_idx = list(all_indices.difference(idx))
        res = np.polyfit(x[train_idx], obs[train_idx], 1)
        print(np.array(res))
        cross_loss += sum( \
            (res[1] + res[0] * x[idx] - obs[idx])**2)

    print('cross = %.4f'%cross_loss)
        
go() 
