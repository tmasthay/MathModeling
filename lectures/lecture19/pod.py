import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'text.usetex': True
})

N = 100
a = 0.0
b = 10.0
x = np.linspace(a,b,N)

f = np.array([1,2,3])

fig,ax = plt.subplots()

plt.title('POD Example')
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')

ax.plot(x, x, '--', label=r'Line $x_2 = x_1$')

for ff in f:
    ax.plot(x, x + np.sin(ff*x), label='j=%d'%ff)

ax.legend(loc='upper left')

plt.savefig('pod.pdf')



