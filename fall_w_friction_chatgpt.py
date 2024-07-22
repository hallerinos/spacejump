# Felix Baumgartner's Space Jump Analysis

## Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import pandas as pd

## Constants
# Extracted from the provided document
g = 9.80665  # Acceleration due to gravity (m/s^2)
Cd = 0.5
rho0 = 1.225  # Sea level air density (kg/m^3)
H = 8500  # Scale height (m)
mass = 110  # Mass of Felix Baumgartner with equipment (kg)
area = 1  # Cross-sectional area (m^2)
a = 343  # Speed of sound at sea level (m/s)

def drag_coefficient(v):
    vda = abs(v/a)
    c = Cd
    # if vda > 0.9:
    #     c = 2*Cd * vda
    return c

## Differential Equation
def equations(t, y):
    h, v = y
    rho = rho0 * np.exp(-h / H)  # Air density as a function of height
    dc = drag_coefficient(v)
    D = 0.5 * dc * rho * area * v**2  # Drag force
    dhdt = v
    dvdt = -g + D / mass
    return [dhdt, dvdt]

## Initial Conditions
h0 = 38969  # Initial height (m)
v0 = -6  # Initial velocity (m/s)
y0 = [h0, v0]
t_span = (0, 1000)  # Time span for the simulation (s)

## Solving the Differential Equations
solution = solve_ivp(equations, t_span, y0, method='RK45', dense_output=True)

## Plotting the Results
t = np.linspace(0, 1000, 1000)
z = solution.sol(t)
h, v = z

plt.figure(figsize=(10, 5))
plt.plot(h, v)
plt.xlabel('Altitude (m)')
plt.ylabel('Velocity (m/s)')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

data = pd.read_csv('velocity_data.csv')
print(data)
plt.plot(data['h']*1000, -data['v'])

plt.tight_layout()
plt.show()