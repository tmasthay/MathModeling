import numpy as np
import itertools
import scipy
import matplotlib.pyplot as plt
def generate_model(x):
    alpha = 0.0
    beta = 2.0
    return alpha + beta * x

def generate_noise(N):
    mu = 0.0
    sig = 0.02
    return np.random.normal(mu, sig, (N,))

def run_case(x, f, indices):
    n_pts = len(x)
    eta = generate_noise(n_pts)
    obs = f + eta


    cross_loss = 0.0

    avg_training_loss = 0.0

    all_indices = set(range(n_pts))
    for idx in indices:
        train_idx = list(all_indices.difference(idx))
        res = np.polyfit(x[train_idx], obs[train_idx], 1)
        cross_loss += sum( \
            (res[1] + res[0] * x[idx] - obs[idx])**2) / len(idx)
        avg_training_loss += sum( \
            (res[1] + res[0] * x[train_idx] - obs[train_idx])**2) \
                / len(train_idx)

    return cross_loss / len(indices), avg_training_loss / len(indices)

def go(num_cases):
    p = 2
   
    #define grid 
    a = 0.0
    b = 1.0
    n_pts = 100
    x = np.linspace(a,b,n_pts)

    f = generate_model(x)
    
    cross_losses = np.zeros(num_cases)
    training_loss = np.zeros(num_cases)

    all_indices = set(range(n_pts))
    indices = [list(idx) for idx in itertools.combinations(all_indices, p)]

    for i in range(num_cases):
        cross_losses[i], training_loss[i] = run_case(x,f,indices)

    fig, ax = plt.subplots() 
    ax.plot(range(num_cases), cross_losses, 'ob', label='Crossval loss')
    ax.plot(range(num_cases), training_loss, label='Training loss')
    ax.plot(range(num_cases), 
        float(n_pts + p + 1) / (n_pts - p - 1) * training_loss, 
        '*r', 
        label='Theoretical Crossval loss')
    ax.legend(loc='best')
    plt.savefig('linreg-crossval.pdf')

go(20) 
