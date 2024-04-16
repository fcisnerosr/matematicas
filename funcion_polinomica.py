import matplotlib.pyplot as plt
import numpy as np

N = 100
x = np.linspace(-10, 10, num = N)

def f(x):
    # return 2*x**3 - x**1 + 4
    # return  2*x**3 + 2*x**2 + 2**x - 5 
    return  x**3

y = f(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.grid()
# plt.show()

plt.plot(x,y)
plt.grid()
plt.show()