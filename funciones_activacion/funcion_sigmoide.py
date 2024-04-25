import matplotlib.pyplot as plt; import numpy as np; import os
os.system('clear')

def f(x):
    return 1/(1+np.exp(-x))

x = np.linspace(-7.5, 7.5, num = 1000)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y = 0, color = 'r')
ax.axvline(x = 0, color = 'r')
plt.show()
