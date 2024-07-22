import matplotlib.pyplot as plt
import numpy as np

# Data approximation for Felix Baumgartner's space jump
time = np.linspace(0, 600, 1000)  # 0 to 600 seconds
initial_altitude = 39000  # meters
max_velocity = 1357.6  # km/h (equivalent to Mach 1.25)

# Altitude calculation (simplified model)
altitude = initial_altitude - (0.5 * 9.8 * time**2)
altitude = np.maximum(altitude, 0)  # Ensure altitude doesn't go below 0

# Velocity calculation (simplified model)
velocity = 9.8 * time
velocity = np.minimum(velocity * 3.6, max_velocity)  # Convert to km/h and cap at max velocity

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot altitude
color = 'tab:blue'
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Altitude (meters)', color=color)
ax1.plot(time, altitude, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a secondary y-axis for velocity
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Velocity (km/h)', color=color)
ax2.plot(time, velocity, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Set title and display the plot
plt.title("Felix Baumgartner's Space Jump: Altitude and Velocity vs Time")
fig.tight_layout()
plt.show()