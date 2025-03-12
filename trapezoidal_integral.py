from math import sin
from math import pi
from math import exp

def trape_inte(f,a = 0, b = 1, n = 100):
    h = (b - a) / n
    S = 0
    k = 1
    for k in range(n + 1):
        S += (h/2) * (f(a + (k - 1) * h) + f(a + k * h))
    return S

def f(x):
    return sin(x)
print(trape_inte(f,0,pi/2,50))

def f(x):
    return 4 / (1 + x**2)
print(trape_inte(f,0,1,100))

def f(x):
    return pi**(1/2) * exp(-x**2)
print(trape_inte(f,-100,100,1000))