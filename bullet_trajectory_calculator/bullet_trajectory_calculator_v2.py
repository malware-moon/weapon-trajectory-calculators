# Bullet Trajectory Script

# Import necessary libraries
import math
import numpy as np
import matplotlib.pyplot as plt

# Define constants
GRAVITY = 9.8 # m/s^2
ANGLE = 45.0 # Launch angle in degrees
VELOCITY = 100.0 # Initial velocity in m/s
HEIGHT = 1.0 # Initial height in meters
DRAG_COEFFICIENT = 0.47 # Drag coefficient of a sphere
AIR_DENSITY = 1.225 # Air density in kg/m^3
BULLET_RADIUS = 0.005 # Radius of the bullet in meters
BULLET_MASS = 0.01 # Mass of the bullet in kg

# Convert launch angle to radians
angle_rad = np.radians(ANGLE)

# Calculate the x and y components of the initial velocity
velocity_x = VELOCITY * np.cos(angle_rad)
velocity_y = VELOCITY * np.sin(angle_rad)

# Calculate the cross sectional area and the drag force
cross_sectional_area = math.pi * BULLET_RADIUS**2
drag_force = 0.5 * AIR_DENSITY * VELOCITY**2 * DRAG_COEFFICIENT * cross_sectional_area

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
    
    # Calculate the drag force
    drag_force = 0.5 * AIR_DENSITY * (velocity_x**2 + (velocity_y + GRAVITY * time[i])**2) * DRAG_COEFFICIENT * cross_sectional_area
    
    # Calculate the acceleration
    acceleration_x = -drag_force / BULLET_MASS * np.sign(velocity_x)
    acceleration_y = -drag_force / BULLET_MASS * np.sign(velocity_y + GRAVITY * time[i]) - GRAVITY
    
    # Update the velocity vector
    velocity_x += acceleration_x * dt
    velocity_y += acceleration_y * dt

# Plot the trajectory
plt.plot(x, y)
plt.xlabel("X Distance (m)")
plt.ylabel("Y Height (m)")
plt.title("Bullet Trajectory")
plt.show()
