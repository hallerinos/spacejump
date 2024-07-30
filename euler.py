import numpy as np
import matplotlib.pyplot as plt

# Define the range for the exact function and Euler's method
x_exact = np.linspace(0, np.pi, 1000)
y_exact = np.sin(x_exact)

# Parameters for Euler's method
x_start = 0  # Starting x value
x_end = np.pi  # Ending x value
h = 0.1  # Step size
n_steps = int((x_end - x_start) / h)

# Arrays to store the x and y values of the Euler's method approximation
x_euler = np.zeros(n_steps + 1)
y_euler = np.zeros(n_steps + 1)

# Initial condition
x_euler[0] = x_start
y_euler[0] = 0  # sin(0) = 0

# Euler's method loop
for i in range(n_steps):
    x_euler[i + 1] = x_euler[i] + h
    y_euler[i + 1] = y_euler[i] + h * np.cos(x_euler[i])  # y' = cos(x)

# Plotting
plt.plot(x_exact, y_exact, label='sin(x)', color='blue')
plt.scatter(x_euler, y_euler, label="Euler's Method Approximation", color='red')#, linestyle='--')
plt.xlabel('t')
plt.ylabel('y')
#plt.title("y(t)=sin(t) and its Euler's Method Approximation")

plt.xlim([0,np.pi])
plt.legend()
plt.grid(True)
plt.show()
