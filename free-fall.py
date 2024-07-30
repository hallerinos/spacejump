import numpy as np
import matplotlib
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
t = np.linspace(0, 5, 500)  # time from 0 to 5 seconds

# Initial conditions
v0 = 0  # initial velocity (m/s)
s0 = 0  # initial position (m)

# Equations of motion
a_t = g  # acceleration is constant
v_t = v0 + g * t  # velocity as a function of time
s_t = s0 + v0 * t + 0.5 * g * t**2  # position as a function of time

# Plotting
plt.figure(figsize=(14, 10))

# Acceleration
#plt.subplot(3, 1, 1)
plt.plot(t, a_t * np.ones_like(t), 'r')
plt.fill_between(t, 0, a_t * np.ones_like(t), color='r', alpha=0.3, label='acceleration $a$')
plt.grid(True)

# Velocity
#plt.subplot(3, 1, 2)
plt.plot(t, v_t, 'g')
plt.fill_between(t, 0, v_t, color='g', alpha=0.3, label='velocity $v$')
plt.title('Velocity vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)

# Displacement
#plt.subplot(3, 1, 3)
plt.plot(t, s_t, 'b')
plt.fill_between(t, 0, s_t, color='b', alpha=0.3, label='displacement $d$')
plt.title('Displacement vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)

# Layout and display
plt.tight_layout()
plt.xlim(0,4)
plt.ylim(0,80)
plt.title('Free Fall in Vacuum')
plt.xlabel('Time [s]')
plt.ylabel('[arb. units]')

plt.legend()
plt.show()
