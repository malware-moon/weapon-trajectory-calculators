# Ballistic Missile Guidance Script

# Import necessary libraries
import math
import numpy as np

# Define constants
GRAVITY = 9.8 # m/s^2
TARGET_LAT = 47.6062 # Target latitude in decimal degrees
TARGET_LONG = 122.3321 # Target longitude in decimal degrees
TARGET_ALT = 100.0 # Target altitude in meters
INITIAL_LAT = 37.7749 # Initial latitude in decimal degrees
INITIAL_LONG = -122.4194 # Initial longitude in decimal degrees
INITIAL_ALT = 10.0 # Initial altitude in meters
INITIAL_VELOCITY = 200.0 # Initial velocity in m/s

# Convert latitude and longitude to radians
target_lat_rad = np.radians(TARGET_LAT)
target_long_rad = np.radians(TARGET_LONG)
initial_lat_rad = np.radians(INITIAL_LAT)
initial_long_rad = np.radians(INITIAL_LONG)

# Calculate target position in 3D Cartesian coordinates
target_x = TARGET_ALT * math.cos(target_lat_rad) * math.cos(target_long_rad)
target_y = TARGET_ALT * math.cos(target_lat_rad) * math.sin(target_long_rad)
target_z = TARGET_ALT * math.sin(target_lat_rad)

# Calculate initial position in 3D Cartesian coordinates
initial_x = INITIAL_ALT * math.cos(initial_lat_rad) * math.cos(initial_long_rad)
initial_y = INITIAL_ALT * math.cos(initial_lat_rad) * math.sin(initial_long_rad)
initial_z = INITIAL_ALT * math.sin(initial_lat_rad)

# Calculate the initial velocity vector
initial_velocity_x = INITIAL_VELOCITY * (target_x - initial_x) / np.linalg.norm([target_x - initial_x, target_y - initial_y, target_z - initial_z])
initial_velocity_y = INITIAL_VELOCITY * (target_y - initial_y) / np.linalg.norm([target_x - initial_x, target_y - initial_y, target_z - initial_z])
initial_velocity_z = INITIAL_VELOCITY * (target_z - initial_z) / np.linalg.norm([target_x - initial_x, target_y - initial_y, target_z - initial_z])

# Simulation loop
time = 0.0
dt = 0.1
while np.linalg.norm([target_x - initial_x, target_y - initial_y, target_z - initial_z]) >= 1.0:
    # Calculate the acceleration vector
    acceleration_x = -GRAVITY * (initial_x - target_x) / np.linalg.norm([initial_x - target_x, initial_y - target_y, initial_z - target_z])**3
    acceleration_y = -GRAVITY * (initial_y - target_y) / np.linalg.norm([initial_x - target_x, initial_y - target_y, initial_z - target_z])**3
    acceleration_z = -GRAVITY * (initial_z - target_z) / np.linalg.norm([initial_x - target_x, initial_y - target_y, initial_z - target_z])**3
    # Update the velocity vector
    initial_velocity_x += acceleration_x * dt
    initial_velocity_y += acceleration_y * dt
    initial_velocity_z += acceleration_z * dt

    # Update the position vector
    initial_x += initial_velocity_x * dt
    initial_y += initial_velocity_y * dt
    initial_z += initial_velocity_z * dt

    # Update the time
    time += dt
    
print("Final Position: ({:.2f}, {:.2f}, {:.2f})".format(initial_x, initial_y, initial_z))
print("Final Velocity: ({:.2f}, {:.2f}, {:.2f})".format(initial_velocity_x, initial_velocity_y, initial_velocity_z))