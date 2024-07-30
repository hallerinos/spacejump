import numpy as np
import matplotlib.pyplot as plt

def euler(f, t, y, h):
    fnext = y + f(t,y)*h
    return fnext

def rk4(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h*k1/2)
    k3 = f(t + h/2, y + h*k2/2)
    k4 = f(t + h, y + h*k3)

    return y + h/6*(k1 + 2*k2 + 2*k3 + k4)

if __name__ == "__main__":
    0   # implement example for Euler