from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

class Bhaskara:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.arrow_fmt = None
        self.fig = None
                
    def calcular_bhaskara(self):
        delta = (self.b ** 2) - 4 * self.a * self.c
        xv = -self.b / (2 * self.a)
        yv = -delta / (4 * self.a)

        if delta > 0:
            x1 = (self.b - sqrt(delta)) / (2 * self.a)
            x2 = (self.b + sqrt(delta)) / (2 * self.a)

            return delta, x1, x2, xv, yv

        if delta == 0:
            x = -self.b / (2 * self.a)
            return delta, x, x, xv, yv
        
        if delta < 0:
            return None
        
    def results(self):
        
        resultado = self.calcular_bhaskara()
        
        if resultado is not None:
            delta, x1, x2, xv, yv = resultado
            
            print("\n--------------------------------")
            print(f"Valor de Delta: {delta:.2f}")
        
            if delta == 0:
                print("--------------------------------")
                print(f"Valor de X: {x1:.2f}")
                print("--------------------------------")
        
            if delta > 0:
                print("--------------------------------")
                print(f"Valor de X¹: {x1:.2f}")
                print(f"Valor de X²: {x2:.2f}")
                print("--------------------------------")
                
            if xv is not None and yv is not None:
                print(f"Valor de Xvértice: {xv:.2f}")
                print(f"Valor de Yvértice: {yv:.2f}")
                print("--------------------------------")

        else:
            delta = resultado
            print("\n--------------------------------")
            print("A equação não possui raizes reais! (Delta < 0)")
            print("Como é possível ver no gráfico, a parábola não passa pelo eixo X")
            print("--------------------------------\n")
            
    def graph(self, a, b, c):
        
        
        xmin, xmax, ymin, ymax = -10, 11, -10, 11
        ticks_frequency = 1

        def func(a,b,c,x):
            return a*x**2 + b*x + c

        fig, ax = plt.subplots(figsize=(10, 10))

        x = np.linspace(-5, 10, 100)
        y = func(a,b,c,x)

        plt.plot(x, y, 'b', linewidth=2)
        plt.ylim(ymin=0)

        ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_xlabel('$X$', size=16, labelpad=-24, x=1.03)
        ax.set_ylabel('$Y$', size=16, labelpad=-21, y=1.02, rotation=0)

        plt.text(0.5, 0.5, r"$O$", ha='right', va='top',
            transform=ax.transAxes,
                horizontalalignment='center', fontsize=12)

        x_ticks = np.arange(xmin, xmax, ticks_frequency)
        y_ticks = np.arange(ymin, ymax, ticks_frequency)
        ax.set_xticks(x_ticks[x_ticks != 0])
        ax.set_yticks(y_ticks[y_ticks != 0])
        ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
        ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

        arrow_fmt = dict(markersize=4, color='black', clip_on=False)

        plt.show()
        exit()    