# Creación de clase
import matplotlib.pyplot as plt; import numpy as np

class funcion_lineal:
    def __init__(self, lim_inf, lim_sup, N, b, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.N = N
        self.b = b
        
    def graficar(self):
        m = (self.y2 - self.y1) / (self.x2 - self.x1)
        x = np.linspace(self.lim_inf, self.lim_sup, self.N)
        y = [x_i*m + self.b  for x_i in x]
        # print(y)
        plt.plot(x,y)
        plt.grid()
        plt.show()
        
class funcion_polinomial(funcion_lineal):
    def __init__(self, lim_inf, lim_sup, N, b, x1, y1, x2, y2, pot):
        super().__init__(lim_inf, lim_sup, N, b, x1, y1, x2, y2)
        self.pot = pot
    def graficar(self):
        x = np.linspace(self.lim_inf, self.lim_sup, self.N)
        y = [x_i**self.pot for x_i in x]
        plt.plot(x,y)
        plt.grid()
        plt.show()
        
lim_inf = -10
lim_sup = 10
N = 1000
b = 3
x1 = -2
y1 = 3
x2 = 2
y2 = -1
pot = 2

if __name__ == '__main__':
    # funcion1 = funcion_lineal(lim_inf, lim_sup, N, b, x1, y1, x2, y2)
    # funcion1.graficar()
    
    funcion2 = funcion_polinomial(lim_inf, lim_sup, N, b, x1, y1, x2, y2, pot)
    funcion2.graficar()