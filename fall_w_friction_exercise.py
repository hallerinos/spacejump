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

# Time array
dt = 0.1
A = 1
H = 6700

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
    rho_h = 0  # MODIFY!

    # Define the force functions
    F_drag = lambda t,y : 0  # MODIFY!
    F_g = lambda t,y : 0  # MODIFY!
    a_tot = lambda t,y : 0  # MODIFY!
    
    # Update velocity and position using Euler/RK4 method
    velocity[i] = euler(a_tot, t[i-1], velocity[i-1], dt)
    v_tot = lambda t,y : velocity[i]
    altitude[i] = euler(v_tot, t[i-1], altitude[i-1], dt)
    
    # Stop the simulation if we reach the ground
    if altitude[i] <= 0:
        altitude[i] = 0
        break

ax.set_xlabel('$d\\ {\\rm [km]}$')
ax.set_ylabel('$v\\ {\\rm [m/s]}$')
ax.plot(altitude/1000, velocity, color='black', label='Numerical Integration')

# compare with actual data
trajectory = pd.read_csv('velocity_data.csv')
ax.scatter(trajectory['h'], -trajectory['v'], zorder=0, label="Baumgartner's trajectory")

ax.set_xlim([0, initial_altitude/1000])

# Set title and display the plot
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.legend()
plt.title("Felix Baumgartner's Space Jump")
fig.tight_layout()
plt.show()