import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

a = -1
b = 1
N = np.array([3, 6,  10, 11, 12, 20])
X = np.array([np.linspace(a,b,n) for n in N])

N_ref = 100
X_ref = np.linspace(a,b,N_ref)
runge_fnc = lambda x : 1.0 / (1 + 25 * x**2) 

fig, ax = plt.subplots()
plt.title('Runge Phenomenon')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(X_ref, runge_fnc(X_ref), '--', label='Runge Function')

for (i,n) in enumerate(N):
    p = lagrange(X[i], runge_fnc(X[i]))
    ax.plot(X_ref, np.array(list(map(p, X_ref))), label='N=%d'%n)
    ax.legend(loc='best')
    plt.savefig('runge%d.pdf'%(n))

