"""
This script calculates the bullet trajectory based on all the specified parameters, 
and plots the result using the matplotlib library. Note that the wind direction,
bullet spin, and cross-sectional area are all given in SI units.
"""
import numpy as np
import matplotlib.pyplot as plt

def atm_density(altitude, temperature, pressure, lapse_rate, gas_constant_air):
    """
    Returns the atmospheric density at a given altitude based on the temperature, pressure, lapse rate,
    and gas constant for air.
    """
    temperature = temperature - lapse_rate * altitude
    density = pressure / (gas_constant_air * temperature)
    return density

def bullet_trajectory(v0, h0, theta, m, r, Cd, T, p, lapse_rate, gas_constant_air, wind_speed, wind_direction, bullet_spin, earth_radius, cross_section_area):
    """
    Calculates the bullet trajectory based on the given parameters:
    v0: initial velocity (m/s)
    h0: initial height (m)
    theta: launch angle (rad)
    m: bullet mass (kg)
    r: bullet radius (m)
    Cd: drag coefficient
    T: temperature (K)
    p: pressure (Pa)
    lapse_rate: atmospheric temperature lapse rate (K/m)
    gas_constant_air: gas constant for air (J/(kg*K))
    wind_speed: wind speed (m/s)
    wind_direction: wind direction (rad)
    bullet_spin: bullet spin rate (rad/s)
    earth_radius: radius of the Earth (m)
    cross_section_area: cross-sectional area of the bullet (m^2)
    """
    # Constants
    g = 9.8  # acceleration due to gravity (m/s^2)

    # Calculate wind velocity
    wind_vx = wind_speed * np.cos(wind_direction)
    wind_vy = wind_speed * np.sin(wind_direction)

    # Calculate atmospheric density
    rho = atm_density(h0, T, p, lapse_rate, gas_constant_air)  # atmospheric density (kg/m^3)

    # Initial conditions
    vx = v0 * np.cos(theta) + wind_vx  # initial x velocity (m/s)
    vy = v0 * np.sin(theta) + wind_vy  # initial y velocity (m/s)
    x = [0]  # initial x position (m)
    y = [h0]  # initial y position (m)
    t = 0  # initial time (s)

    # Time step (s)
    dt = 0.01

    # Calculate bullet trajectory
    while y[-1] >= earth_radius:
        A = cross_section_area  # cross-sectional area (m^2)
        v = np.sqrt(vx**2 + vy**2)  # velocity magnitude (m/s)
        F_drag = 0.5 * Cd * A * rho * v**2  # drag force (N)
        ax = -F_drag * vx / m  # x acceleration (m/s^2)
        ay = -F_drag * vy / m - g  #
        # Calculate coriolis force
        omega = 2 * np.pi / (24 * 60 * 60)  # angular velocity of the Earth (rad/s)
        lat = np.arctan2(y[-1], np.sqrt(x[-1]**2 + (earth_radius + y[-1])**2))  # latitude (rad)
        F_coriolis = 2 * m * omega * vy * np.cos(lat)  # coriolis force (N)
        ax += -F_coriolis / m * np.sin(lat)

        # Calculate bullet spin effect
        F_spin = r * bullet_spin**2 * np.sin(2 * lat)  # spin force (N)
        ay += -F_spin / m

        # Update velocity and position
        vx += ax * dt
        vy += ay * dt
        x.append(x[-1] + vx * dt)
        y.append(y[-1] + vy * dt)
        t += dt

    # Plot bullet trajectory
    plt.plot(x, y)
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Altitude (m)')
    plt.title('Bullet Trajectory')
    plt.show()

# Example Usage
bullet_trajectory(800, 0, np.deg2rad(45), 0.05, 0.005, 0.47, 288, 101325, -0.0065, 287, 5, np.deg2rad(90), 0, 6.37e6, np.pi * 0.005**2)