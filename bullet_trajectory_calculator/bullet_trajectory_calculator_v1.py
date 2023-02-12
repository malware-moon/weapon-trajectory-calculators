# Bullet Trajectory Script
# This script uses the kinematic equation y = HEIGHT + velocity_y * time[i] - 0.5 * GRAVITY * time[i]^2 to calculate the height of the bullet at each time step.
# The trajectory is then plotted using matplotlib. This is a very basic example and the simulation can be improved and made more accurate with additional calculations and modifications.

# Import necessary libraries
import math
import numpy as np
import matplotlib.pyplot as plt

# Define constants
GRAVITY = 9.8 # m/s^2
ANGLE = 45.0 # Launch angle in degrees
VELOCITY = 100.0 # Initial velocity in m/s
HEIGHT = 1.0 # Initial height in meters

# Convert launch angle to radians
angle_rad = np.radians(ANGLE)

# Calculate the x and y components of the initial velocity
velocity_x = VELOCITY * np.cos(angle_rad)
velocity_y = VELOCITY * np.sin(angle_rad)

# Define the time step
dt = 0.1

# Initialize the time, x, and y arrays
time = np.arange(0.0, 10.0, dt)
x = np.zeros(len(time))
y = np.zeros(len(time))

# Calculate the trajectory
for i in range(len(time)):
    x[i] = velocity_x * time[i]
    y[i] = HEIGHT + velocity_y * time[i] - 0.5 * GRAVITY * time[i]**2

# Plot the trajectory
plt.plot(x, y)
plt.xlabel("X Distance (m)")
plt.ylabel("Y Height (m)")
plt.title("Bullet Trajectory")
plt.show()