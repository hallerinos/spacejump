import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from euler import integrate_euler
import pandas as pd

gr = 1.61803398875
s = 4
mpl.rcParams['text.usetex'] = True
mpl.rcParams['figure.figsize'] = (gr*s, s)
# plt.rc('text.latex', preamble=r'\usepackage{bm,braket}')

# Constants
g = -9.8  # Acceleration due to gravity (m/s^2)
m = 118  # Mass of Baumgartner with equipment (kg)
rho = 1.2  # Air density at sea level (kg/m^3)
A = 0.9  # Approximate frontal area (m^2)
Cd = 1  # Drag coefficient (dimensionless)

# Initial conditions
initial_altitude = 39000  # Initial altitude (m)
initial_velocity = 0  # Initial velocity (m/s)

# Create the plot
fig, ax = plt.subplots()

trajectory = pd.read_csv('velocity_data.csv')

# Time array
dt = 0.1
for A in np.linspace(0, 4, 10):
    for H in np.linspace(1000,10000,10):
        t = np.arange(0, 500, dt)  # Time array from 0 to 600 seconds

        # Arrays to store results
        altitude = np.zeros_like(t)
        velocity = np.zeros_like(t)

        # Set initial conditions
        altitude[0] = initial_altitude
        velocity[0] = initial_velocity

        # Simulation loop
        for i in range(1, len(t)):
            # Calculate air density at current altitude (simplified model)
            rho_h = rho * np.exp(-altitude[i-1] / H)
            
            # Calculate drag force
            F_drag = 0.5 * rho_h * Cd * A * (velocity[i-1]**2)
            
            # Calculate acceleration
            a = g - (F_drag / m)*np.sign(velocity[i-1])
            
            # Update velocity and position using Euler method
            velocity[i] = integrate_euler(velocity[i-1], a, dt)
            altitude[i] = integrate_euler(altitude[i-1], velocity[i], dt)
            
            # Stop the simulation if we reach the ground
            if altitude[i] <= 0:
                altitude[i] = 0
                break

        # Convert velocity to km/h
        velocity_kmh = velocity * 3.6

        ax.set_xlabel('$h\\ {\\rm [km]}$')
        ax.set_ylabel('$v\\ {\\rm [m/s]}$')
        ax.plot(altitude/1000, velocity)

ax.scatter(trajectory['h'], -trajectory['v'], zorder=0)

ax.set_xlim([0, initial_altitude/1000])
# Set title and display the plot
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.title("Felix Baumgartner's Space Jump")
fig.tight_layout()
plt.show()