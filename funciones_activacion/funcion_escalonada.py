import matplotlib.pyplot as plt; import numpy as np; import os
os.system('clear')

def H(x):
    Y = np.zeros(len(x))
    for idx,x in enumerate(x):
        if x >= 0:
            Y[idx] = 1
    return Y

x = np.linspace(-10, 10, num = 1000)
y = H(x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
# ax.axhline(y = 0, color = 'r')
# ax.axvline(x = 0, color = 'r')
plt.show()