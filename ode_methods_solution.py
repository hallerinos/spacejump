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
    v0, s0 = 0, 1
    
    dveldt = lambda t,y : np.cos(t)

    h = 0.1
    t = np.linspace(0, 2*np.pi, int(round(2*np.pi/h)))
    
    lbl = ['Euler', 'RK4']
    for (idm,m) in enumerate([euler, rk4]):
        vel = np.zeros(t.shape)
        pos = np.zeros(t.shape)

        vel[0] = v0
        pos[0] = s0
        for (n, tn) in enumerate(t[:-1]):
            vel[n+1] = m(dveldt, tn, vel[n], h)
            dposdt = lambda t,y : -vel[n+1]
            pos[n+1] = m(dposdt, tn, pos[n], h)
        plt.scatter(t, vel, label=lbl[idm])
        plt.scatter(t, pos, label=lbl[idm])
    plt.plot(t, np.sin(t), label='sin(t)')
    plt.plot(t, np.cos(t), label='cos(t)')
    plt.legend()
    plt.show()