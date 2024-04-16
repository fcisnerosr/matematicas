import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 2560, num = 10000)

def f(x):
    # return np.cos(x)
    # return np.exp(x)
    return np.log2(x)

y = f(x)

plt.plot(x,y)
plt.grid()
plt.show()