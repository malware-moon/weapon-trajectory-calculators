"""
In this script, the submarine's location data is loaded into a Pandas DataFrame, and columns are added for the velocity, direction, water temperature, and water pressure. The submarine's location and velocity are then plotted using Matplotlib, and the water temperature and pressure are also plotted.

Note that this is a simplified example and is not representative of a complete submarine tracking system. In a real-world system, much more data processing, analysis, and modeling would be required to account for all of the variables and considerations involved in tracking a submarine.
"""

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
