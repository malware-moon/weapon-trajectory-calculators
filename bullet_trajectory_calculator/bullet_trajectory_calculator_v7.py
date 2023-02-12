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

def bullet_trajectory(v0, h0, theta, m, r, T, p, lapse_rate, gas_constant_air):
    """
    Calculates the bullet trajectory based on the given parameters:
    v0: initial velocity (m/s)
    h0: initial height (m)
    theta: launch angle (rad)
    m: bullet mass (kg)
    r: bullet radius (m)
    T: temperature (K)
    p: pressure (Pa)
    lapse_rate: atmospheric temperature lapse rate (K/m)
    gas_constant_air: gas constant for air (J/(kg*K))
    """
    # Constants
    g = 9.8  # acceleration due to gravity (m/s^2)
    Cd = 0.5  # drag coefficient for a sphere
    rho = atm_density(h0, T, p, lapse_rate, gas_constant_air)  # atmospheric density (kg/m^3)

    # Initial conditions
    vx = v0 * np.cos(theta)  # initial x velocity (m/s)
    vy = v0 * np.sin(theta)  # initial y velocity (m/s)
    x = [0]  # initial x position (m)
    y = [h0]  # initial y position (m)
    t = 0  # initial time (s)

    # Time step (s)
    dt = 0.01

    # Calculate bullet trajectory
    while y[-1] >= 0:
        A = np.pi * r**2  # cross-sectional area (m^2)
        v = np.sqrt(vx**2 + vy**2)  # velocity magnitude (m/s)
        F_drag = 0.5 * Cd * A * rho * v**2  # drag force (N)
        ax = -F_drag * vx / m  # x acceleration (m/s^2)
        ay = F_drag * vy / m - g  # y acceleration (m/s^2)
        vx = vx + ax * dt  # updated x velocity (m/s)
        vy = vy + ay * dt  # updated y velocity (m/s)
        x.append(x[-1] + vx * dt)  # updated x position (m)
        y.append(y[-1] + vy * dt)  # updated y position (m)
        t = t + dt  # updated time (s)
    return x
