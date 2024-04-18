import matplotlib.pyplot as plt; import numpy as np

N = 1000

x = np.linspace(-10, 10, num = N)

def g(x):
    return np.cos(x)

def f(x):
    # return np.sin(x)
    return x**3

# y = g(x)
f_o_g = f(g(x))

plt.plot(x,f_o_g)
plt.grid()
plt.show()