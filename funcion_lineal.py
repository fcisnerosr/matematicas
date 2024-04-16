# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt # librería para graficar
import numpy as np              # librería para manejo de vectores

N = 10

m = -1
b = 3

def f(x):
    return m*x + b

x = np.linspace(-10, 10, num = N)
# print(x)
# print(x.shape)  # número de valores de x
# print(len(x))   # long de x

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
plt.show()