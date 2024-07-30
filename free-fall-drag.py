import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)



# Constants
g = 9.81       # acceleration due to gravity (m/s^2)
Cd = 0.47      # drag coefficient (dimensionless)
rho = 1.225    # air density (kg/m^3)
A = 0.1        # cross-sectional area (m^2)
m = 70         # mass of the object (kg)
t_max = 50     # maximum time (s)
dt = 0.01      # time step (s)

# Time array
t = np.arange(0, t_max, dt)


# Initial conditions
v0 = 0  # initial velocity (m/s)
s0 = 0  # initial position (m)

# Equations of motion
a_t = g  # acceleration is constant
v_t = v0 + g * t  # velocity as a function of time
s_t = s0 + v0 * t + 0.5 * g * t**2  # position as a function of time



# Initialize arrays for velocity, position, and acceleration
v = np.zeros_like(t)
s = np.zeros_like(t)
a = np.zeros_like(t)


# Initial conditions
v[0] = 0  # initial velocity (m/s)
s[0] = 0  # initial position (m)


# Numerical solution using Euler's method
for i in range(1, len(t)):
    # Calculate drag force
    F_d = 0.5 * Cd * rho * A * v[i-1]**2
    
    # Calculate acceleration
    a[i-1] = g - (F_d / m)
    
    # Update velocity and position
    v[i] = v[i-1] + a[i-1] * dt
    s[i] = s[i-1] + v[i-1] * dt

# Final acceleration
a[-1] = g - (0.5 * Cd * rho * A * v[-1]**2) / m



# Plotting
plt.figure(figsize=(14, 10))



# Acceleration
plt.figure(figsize=(14, 10))
plt.plot(t, a_t * np.ones_like(t), 'orange', lw=3, label='free fall')
plt.plot(t, a * np.ones_like(t), 'r', lw=3, label='free fall + drag')

plt.grid(True)
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('acceleration $a$ [$m/s^2$]')
plt.show()


# Velocity
plt.figure(figsize=(14, 10))
plt.plot(t, v_t * np.ones_like(t), 'lime', lw=3, label='free fall')
plt.plot(t, v * np.ones_like(t), 'g', lw=3, label='free fall + drag')

plt.grid(True)
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('velocity $v$ [$m/s$]')
plt.show()


# Displacement
plt.figure(figsize=(14, 10))
plt.plot(t, s_t * np.ones_like(t), 'deepskyblue', lw=3, label='free fall')
plt.plot(t, s * np.ones_like(t), 'b', lw=3, label='free fall + drag')

plt.grid(True)
plt.legend()
plt.xlabel('Time [s]')
plt.ylabel('displacement $d$ [$m$]')
plt.show()



