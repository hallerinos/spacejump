import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from ode_methods_solution import euler, rk4
import pandas as pd

gr = 1.61803398875
s = 4
mpl.rcParams['text.usetex'] = True
mpl.rcParams['figure.figsize'] = (gr*s, s)

# Constants
g = -9.81  # Acceleration due to gravity (m/s^2)
m = 127  # Mass of Baumgartner with equipment (kg)
rho = 1.2  # Air density at sea level (kg/m^3)
Cd = 1  # Drag coefficient (dimensionless)

# Initial conditions
initial_altitude = 39000  # Initial altitude (m)
initial_velocity = 0  # Initial velocity (m/s)

# Create the plot
fig, ax = plt.subplots()

dt = 1
lbls = ['Euler', 'RK4']
mkrs = ['x', 'o']
for A in [0.8]:
    for H in [7000]:
        for (integrate, lbl, mkr) in zip([euler, rk4], lbls, mkrs):
            t = np.arange(0, 600, dt)

            # Arrays to store results
            altitude = np.zeros_like(t)
            velocity = np.zeros_like(t)

            # Set initial conditions
            altitude[0] = initial_altitude
            velocity[0] = initial_velocity

            # Simulation loop
            for i in range(1, len(t)):
                # Calculate air density
                rho_h = rho * np.exp(-altitude[i-1] / H)

                # Define the force functions
                F_drag = lambda t,y : 0.5 * rho_h * Cd * A * y**2
                F_g = lambda t,y : m*g
                a_tot = lambda t,y : (F_drag(t,y) + F_g(t,y))/m
                
                # Update velocity and position using Euler/RK4 method
                velocity[i] = integrate(a_tot, t[i-1], velocity[i-1], dt)
                v_tot = lambda t,y : velocity[i]
                altitude[i] = integrate(v_tot, t[i-1], altitude[i-1], dt)
                
                # Stop the simulation if we reach the ground
                if altitude[i] <= 0:
                    altitude[i] = 0
                    break

            ax.set_xlabel('$d\\ {\\rm [km]}$')
            ax.set_ylabel('$v\\ {\\rm [m/s]}$')
            ax.plot(altitude/1000, velocity, label=lbl)

# compare with actual data
trajectory = pd.read_csv('velocity_data.csv')
ax.scatter(trajectory['h'], -trajectory['v'], zorder=0, label="Baumgartner's trajectory", color='black', marker='x')

ax.set_xlim([0, initial_altitude/1000])

# Set title and display the plot
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.legend()
plt.title("Felix Baumgartner's Space Jump")
fig.tight_layout()
plt.show()