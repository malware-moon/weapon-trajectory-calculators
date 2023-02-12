import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the submarine's location data
submarine_data = pd.read_csv("submarine_location.csv")
df = pd.DataFrame(submarine_data)

# Add a column for the velocity of the submarine
df['velocity'] = df['speed'].diff()

# Add a column for the direction of the submarine's movement
df['direction'] = np.arctan2(df['velocity'], df['speed'])

# Add a column for the water temperature
df['water_temp'] = pd.read_csv("water_temperature.csv")

# Add a column for the water pressure
df['water_pressure'] = pd.read_csv("water_pressure.csv")

# Add a column for the water salinity
df['water_salinity'] = pd.read_csv("water_salinity.csv")

# Define the submarine characteristics
submarine_mass = 10000  # kg
submarine_drag_coefficient = 0.5
submarine_cross_sectional_area = 20  # m^2

# Calculate the water density
water_density = 1000 * (1 - (0.01 * df['water_salinity']) + (0.0066 * df['water_temp']))  # kg/m^3

# Calculate the drag force on the submarine
drag_force = 0.5 * submarine_drag_coefficient * water_density * df['speed']**2 * submarine_cross_sectional_area

# Calculate the buoyancy force on the submarine
submarine_volume = submarine_mass / water_density
buoyancy_force = water_density * submarine_volume * 9.8  # N

# Calculate the net force on the submarine
net_force = submarine_mass * df['acceleration'] + drag_force - buoyancy_force

# Plot the submarine's location and velocity
plt.figure(figsize=(15,5))
plt.subplot(121)
plt.plot(df['timestamp'], df['latitude'], label='Latitude')
plt.plot(df['timestamp'], df['longitude'], label='Longitude')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Latitude/Longitude')

plt.subplot(122)
plt.plot(df['timestamp'], df['velocity'], label='Velocity')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Velocity (m/s)')

plt.show()

# Plot the water temperature and pressure
plt.figure(figsize=(15,5))
plt.subplot(121)
plt.plot(df['timestamp'], df['water_temp'], label='Water Temperature')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Temperature (C)')

plt.subplot(122)
plt.plot(df['timestamp'], df['water_pressure'], label='Water Pressure')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Pressure (Pa)')

plt.show()

# Plot the net force on the submarine

plt.figure(figsize=(15,5))
plt.plot(df['timestamp'], net_force, label='Net Force')
plt.legend()
plt.xlabel('Timestamp')
plt.ylabel('Force (N)')

plt.show()