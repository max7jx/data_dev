import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)

n = 10000
r = np.linspace(2.5, 4.0, n)

iterations = 1000
last = 100

x = 1e-5 * np.ones(n)



fig, ax = plt.subplots(figsize=(8, 9),
                               sharex=True)
for i in range(iterations):
    x = logistic(r, x)
    
    if i >= (iterations - last):
        ax.plot(r, x, ',k', alpha=.25)
ax.set_xlim(2.5, 4)
ax.set_title("Bifurcation diagram")


plt.show()