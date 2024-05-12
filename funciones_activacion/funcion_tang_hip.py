import matplotlib.pyplot as plt; import numpy as np; import os
os.system('clear')

def f(x):
    return np.tanh(x)

x = np.linspace(-4, 4, num = 1000)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axvline(x = 0, color = 'r')
ax.axhline(y = 0, color = 'r')
plt.show()
