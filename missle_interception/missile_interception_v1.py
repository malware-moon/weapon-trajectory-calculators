"""
This script implements a simple simulation of two rockets: an interceptor and a target.
The target rocket has a sinusoidal acceleration, while the interceptor rocket has a constant acceleration towards the target.
The simulation uses the Euler method for numerical integration of the equations of motion.
The resulting positions of the interceptor and target rockets are plotted against time.
"""

import numpy as np
import matplotlib.pyplot as plt

def euler_integration(y0, t0, tf, dt, f):
    t = np.arange(t0, tf, dt)
    y = np.zeros((len(t), len(y0)))
    y[0,:] = y0
    for i in range(1, len(t)):
        y[i,:] = y[i-1,:] + dt * f(y[i-1,:], t[i-1])
    return t, y

def interceptor_dynamics(y, t):
    x = y[0]
    v = y[1]
    a = -10.0 * x - v
    return np.array([v, a])

def target_dynamics(y, t):
    x = y[0]
    v = y[1]
    a = -10.0 * x + 0.1 * np.sin(2 * np.pi * t)
    return np.array([v, a])

# Initial conditions
x0_interceptor = 0.0
v0_interceptor = 20.0
x0_target = 50.0
v0_target = 0.0
y0_interceptor = np.array([x0_interceptor, v0_interceptor])
y0_target = np.array([x0_target, v0_target])

# Time parameters
t0 = 0.0
tf = 20.0
dt = 0.01

# Integrate the equations of motion
t_interceptor, y_interceptor = euler_integration(y0_interceptor, t0, tf, dt, interceptor_dynamics)
t_target, y_target = euler_integration(y0_target, t0, tf, dt, target_dynamics)

# Plot the results
plt.plot(t_interceptor, y_interceptor[:,0], label='Interceptor')
plt.plot(t_target, y_target[:,0], label='Target')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()
plt.show()