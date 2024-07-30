import numpy as np
import matplotlib
import matplotlib.pyplot as plt


font = {'family' : 'normal',
        #'weight' : 'bold',
        'size'   : 22}
matplotlib.rc('font', **font)

# Define the range of x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Compute the corresponding y values for sin(x)
y = np.sin(x)

# Define the first point of tangency at x = pi
x_tangent_1 = np.pi
y_tangent_1 = np.sin(x_tangent_1)
slope_1 = np.cos(x_tangent_1)
tangent_line_1 = slope_1 * (x - x_tangent_1) + y_tangent_1

# Define the second point of tangency at x = -pi/2
x_tangent_2 = np.pi / 2
y_tangent_2 = np.sin(x_tangent_2)
slope_2 = np.cos(x_tangent_2)
tangent_line_2 = slope_2 * (x - x_tangent_2) + y_tangent_2

# Create the plot
plt.plot(x, y, label='sin(x)', lw=3)
plt.plot(x, tangent_line_1, label=f'Tangent at $x=\pi$', linestyle='--', color='red', lw=3)
plt.plot(x, tangent_line_2, label=f'Tangent at $x=\pi/2$', linestyle='--', color='blue', lw=3)

# Plot the points of tangency
plt.plot(x_tangent_1, y_tangent_1, 'ro')  # Red dot at the first tangent point
plt.plot(x_tangent_2, y_tangent_2, 'bo')  # Blue dot at the second tangent point

# Add labels and a title
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 3*np.pi/2)
plt.ylim(-1.2, 1.2)
#plt.title('Plot of the sin(x) function with tangent lines at x = π and x = π/2')

# Add a legend
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
