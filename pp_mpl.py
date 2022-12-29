import matplotlib.pyplot as plt
import numpy as np

from mpl_interactions import ipyplot as iplt

from scipy import integrate

fox = 5
rabbit = 10

t = np.linspace(0, 15, 1000)  # time
X0 = np.array([rabbit, fox])  # initials conditions: 10 rabbits and 5 foxes

# use `c_` instead of `c` because `c` is an argument to plt.scatter

# lotka-volttera differential equestion
def f(a, b, c_, d):
    def dX_dt(X, t=0):
        rabbits, foxes = X
        dRabbit_dt = a * rabbits - b * foxes * rabbits
        dFox_dt = -c_ * foxes + d * b * rabbits * foxes
        return [dRabbit_dt, dFox_dt]

    X, _ = integrate.odeint(dX_dt, X0, t, full_output=True)
    return X  # expects shape (N, 2)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 4.8))
controls = iplt.plot(f, ax=ax1, a=(0.5, 2), b=(0.1, 3), c_=(1, 3), d=(0.1, 2), parametric=True)
ax1.set_xlabel("rabbits")
ax1.set_ylabel("foxes")

iplt.plot(f, ax=ax2, controls=controls, label=["rabbits", "foxes"])
ax2.set_xlabel("time")
ax2.set_ylabel("population")
X = ax2.legend()

controls.use_cache = False
plt.show()