import matplotlib.pyplot as plt; import numpy as np

# Desplazamientos horizontales y verticales
# def f(x):
#     return x**2

# x = np.linspace(-50, 70, num = 1000)
# c = -50

# y = f(x + c) + c

# fig, ax = plt.subplots()
# ax.plot(x,y)
# ax.grid()
# ax.axhline(y = 0, color = 'r')
# ax.axvline(x = 0, color = 'r')
# plt.show()

# Alargamientos y compresiones
# def f(x):
#     return np.sin(x)

# x = np.linspace(-15, 15, num = 1000)
# c = 7
# y = f(1/c*x)

# fig, ax = plt.subplots()
# ax.plot(x,y)
# ax.grid()
# ax.axhline(y = 0, color = 'r')
# ax.axvline(x = 0, color = 'r')
# plt.show()

# Reflexiones
def f(x):
    return x**3

x = np.linspace(-10, 10, num = 1000)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y = 0, color = 'r')
ax.axvline(x = 0, color = 'r')
plt.show()