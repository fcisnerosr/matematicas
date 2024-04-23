from funciones import funcion_lineal
import os
os.system('clear')
        
def run():        
    lim_inf = -10
    lim_sup = 10
    N = 10
    b = 3
    x1 = -2
    y1 = 3
    x2 = 2
    y2 = -1

    funcion1 = funcion_lineal(lim_inf, lim_sup, N, b, x1, y1, x2, y2)
    # funcion1.graficar()
    funcion2 = funcion_polinomial(lim_inf, lim_sup, N, b, x1, y1, x2, y2)
    funcion2.graficar()
    

if __name__ == '__main__':
    run()