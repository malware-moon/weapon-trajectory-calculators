# Bullet Trajectory Script with Wind

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
TEMPERATURE = 293.15 # Temperature in Kelvin
PRESSURE = 101325.0 # Pressure in Pa
LAPSE_RATE = -0.0065 # Lapse rate in K/m
GAS_CONSTANT = 287.0 # Gas constant for air in J/(kg*K)
BULLET_RADIUS = 0.005 # Radius of the bullet in meters
BULLET_MASS = 0.01 # Mass of the bullet in kg
WIND_SPEED = 10.0 # Speed of wind in m/s
WIND_DIRECTION = 90.0 # Direction of wind in degrees

# Convert launch angle and wind direction to radians
angle_rad = np.radians(ANGLE)
wind_direction_rad = np.radians(WIND_DIRECTION)

# Calculate the x and y components of the initial velocity
velocity_x = VELOCITY * np.cos(angle_rad)
velocity_y = VELOCITY * np.sin(angle_rad)

# Calculate the x and y components of the wind velocity
wind_velocity_x = WIND_SPEED * np.cos(wind_direction_rad)
wind_velocity_y = WIND_SPEED * np.sin(wind_direction_rad)

# Define the time step
dt = 0.1

# Initialize the time, x, and y arrays
time = np.arange(0.0, 10.0, dt)
x = np.zeros(len(time))
y = np.zeros(len(time))

# Calculate the trajectory
for i in range(len(time)):
    x[i] = velocity_x * time[i] + wind_velocity_x * time[i]
    y[i] = HEIGHT + velocity_y * time[i] - 0.5 * GRAVITY * time[i]**2 + wind_velocity_y * time[i]
    
    # Calculate the air density
    altitude = y[i]
    temperature = TEMPERATURE + LAPSE_RATE * altitude
    air_density = PRESSURE / (GAS_CONSTANT * temperature)
    
    # Calculate the cross sectional area and the drag force
    cross_sectional_area = math.pi * BULLET_RADIUS**2
    drag_force = 0.5 * air_density * ((velocity_x + wind_velocity_x)**2 + (velocity_y + wind_velocity_y)**2) * DRAG_COEFFICIENT * cross_sectional_area
    
    # Plot the trajectory
    # Update the velocity vector
    velocity_x = velocity_x - (drag_force / BULLET_MASS) * np.cos(angle_rad) * dt
    velocity_y = velocity_y - GRAVITY * dt - (drag_force / BULLET_MASS) * np.sin(angle_rad) * dt
    
plt.plot(x, y)
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.title('Bullet Trajectory with Wind')
plt.grid(True)
plt.show()