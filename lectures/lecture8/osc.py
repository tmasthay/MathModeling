import numpy as np
import matplotlib.pyplot as plt

def ubar(t):
    return t

def p(epsilon):
    def f(t):
        return -epsilon * np.cos(t / epsilon) + epsilon
    return f

def u(epsilon):
    f = p(epsilon)
    def g(t):
       return f(t) + ubar(t)
    return g

eps_min = -3
eps_max = 1
epsilons = np.array([10**y for y in range(eps_min, eps_max)])

t0 = 0.0
t1 = 10.0
nt = 1000
t = np.linspace(t0,t1,nt)

funcs = [u(epsilon) for epsilon in epsilons]
funcs.append(ubar)

plots = [np.array(map(f, t)) for f in funcs]
keys = [epsilon for epsilon in epsilons]
keys.append('Averaged')

fig, ax = plt.subplots()

for (i,p) in enumerate(plots):
    ax.plot(t,p, label=keys[i])

plt.title('Averaging of Dynamical System')
plt.xlabel('t')
plt.ylabel('u')
plt.legend(loc='upper left')

plt.savefig('averaging.pdf')
    
