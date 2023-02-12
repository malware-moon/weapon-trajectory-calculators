import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8  # acceleration due to gravity (m/s^2)
C_d = 0.5  # drag coefficient (dimensionless)
rho_0 = 1.225  # air density at sea level (kg/m^3)
T_0 = 288.15  # temperature at sea level (K)
P_0 = 101325.0  # pressure at sea level (Pa)
R = 287.05  # gas constant for air (J/kg-K)
L = -0.0065  # atmospheric lapse rate (K/m)

def air_density(h):
    """Calculate air density based on altitude"""
    T = T_0 + L * h  # temperature at altitude h
    P = P_0 * (T / T_0)**(-g / (R * L))  # pressure at altitude h
    rho = P / (R * T)  # air density at altitude h
    return rho

def air_drag_force(v, rho, A, m):
    """Calculate air drag force"""
    F_drag = 0.5 * rho * v**2 * C_d * A  # air drag force
    return -F_drag

def bullet_trajectory(v0, h0, angle, bullet_mass, bullet_radius):
    """Calculate bullet trajectory"""
    x0 = 0.0  # initial x position (m)
    y0 = h0  # initial y position (m)
    v0x = v0 * np.cos(angle)  # initial x velocity (m/s)
    v0y = v0 * np.sin(angle)  # initial y velocity (m/s)
    t = 0.0  # initial time (s)
    dt = 0.01  # time step (s)
    x = [x0]  # list to store x positions
    y = [y0]  # list to store y positions
    vx = v0x  # initial x velocity (m/s)
    vy = v0y  # initial y velocity (m/s)
    while y[-1] >= 0:
        rho = air_density(y[-1])  # air density at current altitude
        A = np.pi * bullet_radius**2  # bullet cross-sectional area
        m = bullet_mass  # bullet mass (kg)
        F_drag = air_drag_force(np.sqrt(vx**2 + vy**2), rho, A, m)  # air drag force
        ax = F_drag * vx / m  # x acceleration (m/s^2
        ay = F_drag * vy / m - g  # y acceleration (m/s^2)
        vx = vx + ax * dt  # updated x velocity (m/s)
        vy = vy + ay * dt  # updated y velocity (m/s)
        x.append(x[-1] + vx * dt)  # updated x position (m)
        y.append(y[-1] + vy * dt)  # updated y position (m)
        t = t + dt  # updated time (s)
    return x, y

# Test the function with initial velocity = 800 m/s, initial height = 0 m, angle = 45 degrees,
# bullet mass = 0.01 kg, and bullet radius = 0.005 m
x, y = bullet_trajectory(800, 0, np.deg2rad(45), 0.01, 0.005)

# Plot the trajectory
plt.plot(x, y)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Bullet Trajectory")
plt.show()
