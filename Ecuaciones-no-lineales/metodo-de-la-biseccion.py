from numpy import sin
import numpy as np
import math
import matplotlib.pyplot as plt
eps = 10**(-10)
maxIter=1000
#Se define la función
def biseccion(f,a,b):
    fa=f(a)
    fb= f(b)
    i=0
    while i<maxIter and b-a>=eps:
        c=(a+b)/2
        fc=f(c)
        i+=1
        if fc==0:
            a=b=c
        elif fa*fc<0:
            b=c; fb=fc
        else:
            a=c; fa=fc
        print(f'iteración {i}: [a,b]=[{a},{b}]  \t f(a) = {f(a)}  \t f(b) = {f(b)}')
    if b-a>=eps:
        print(f'Método converge')
    else:
        print(f'Solución c = {c}  f(c) = {f(c)}')
biseccion(f = lambda x: x-math.sqrt(7),a=2,b=3)
'''
def h(x):
    return (np.exp(-x)-x)

x=np.linspace(-1,1,100)
plt.plot(x,h(x))
plt.show()'''
