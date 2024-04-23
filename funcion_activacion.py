import matplotlib.pyplot as plt; import numpy as np; import os
os.system('clear')

def f(x):
    return x

x = np.linspace(-10, 10, num = 1000)
m = 1
b = 0
y = m*f(x) + b

fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y = 0, color = 'r')
ax.axvline(x = 0, color = 'r')
plt.show()