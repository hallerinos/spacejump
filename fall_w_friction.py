import matplotlib.pyplot as plt
import numpy as np

# Constants
g = 9.8  # Acceleration due to gravity (m/s^2)
m = 118  # Mass of Baumgartner with equipment (kg)
rho = 1.2  # Air density at sea level (kg/m^3)
A = 0.9  # Approximate frontal area (m^2)
Cd = 0.7  # Drag coefficient (dimensionless)

# Initial conditions
initial_altitude = 39000  # Initial altitude (m)
initial_velocity = 0  # Initial velocity (m/s)

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Time array
dt = 4  # Time step (s)
for dt in [0.1, 0.5, 1, 2]:
    t = np.arange(0, 300, dt)  # Time array from 0 to 600 seconds

    # Arrays to store results
    altitude = np.zeros_like(t)
    velocity = np.zeros_like(t)

    # Set initial conditions
    altitude[0] = initial_altitude
    velocity[0] = initial_velocity

    # Simulation loop
    for i in range(1, len(t)):
        # Calculate air density at current altitude (simplified model)
        rho_h = rho * np.exp(-altitude[i-1] / 7500)
        
        # Calculate drag force
        F_drag = 0.5 * rho_h * Cd * A * velocity[i-1]**2
        
        # Calculate acceleration
        a = g - (F_drag / m)
        
        # Update velocity and position using Euler method
        velocity[i] = velocity[i-1] + a * dt
        altitude[i] = altitude[i-1] - velocity[i] * dt
        
        # Stop the simulation if we reach the ground
        if altitude[i] <= 0:
            altitude[i] = 0
            break

    # Convert velocity to km/h
    velocity_kmh = velocity * 3.6

    # Plot altitude
    # color = 'tab:blue'
    ax1.set_xlabel('Time (seconds)')
    # ax1.set_ylabel('Altitude (meters)', color=color)
    ax1.set_ylabel('Altitude (meters)')
    ax1.plot(altitude, velocity)
    # ax1.tick_params(axis='y', labelcolor=color)

    # Create a secondary y-axis for velocity
    # ax2 = ax1.twinx()
    # color = 'tab:red'
    # ax2.set_ylabel('Velocity (km/h)')
    # ax2.plot(t, velocity_kmh, color=color)
    # ax2.plot(t, velocity_kmh)
    # ax2.tick_params(axis='y', labelcolor=color)

# Set title and display the plot
plt.gca().invert_xaxis()
plt.title("Felix Baumgartner's Space Jump: Altitude and Velocity vs Time (with Air Resistance)")
fig.tight_layout()
plt.show()