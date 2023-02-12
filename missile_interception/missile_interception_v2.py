"""
In this updated version of the script, the physical properties of the rockets such as their mass, size, shape, and aerodynamics have been incorporated into the calculation. The drag force is calculated using the drag coefficient (`Cd`), the surface area (`area`), and the atmospheric density (`rho`). The initial conditions and the time parameters have also been specified.

The `interceptor_dynamics` and `target_dynamics` functions now include the drag force in the calculation of the acceleration, which affects the motion of the rockets. The rest of the script remains unchanged and integrates the equations of motion using the `euler_integration` function. Finally, the position of the interceptor and the target are plotted over time.
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

def interceptor_dynamics(y, t, mass, Cd, area, rho):
    x = y[0]
    v = y[1]
    Fd = 0.5 * Cd * rho * v**2 * area
    a = -10.0 * x - v - Fd / mass
    return np.array([v, a])

def target_dynamics(y, t, mass, Cd, area, rho):
    x = y[0]
    v = y[1]
    Fd = 0.5 * Cd * rho * v**2 * area
    a = -10.0 * x + 0.1 * np.sin(2 * np.pi * t) - Fd / mass
    return np.array([v, a])

# Physical properties of the rockets
mass_interceptor = 1000.0 # kg
Cd_interceptor = 0.5 # drag coefficient
area_interceptor = 20.0 # m^2
mass_target = 500.0 # kg
Cd_target = 0.3 # drag coefficient
area_target = 10.0 # m^2
rho = 1.2 # kg/m^3

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
t_interceptor, y_interceptor = euler_integration(y0_interceptor, t0, tf, dt, 
                                                lambda y, t: interceptor_dynamics(y, t, mass_interceptor, Cd_interceptor, area_interceptor, rho))
t_target, y_target = euler_integration(y0_target, t0, tf, dt, 
                                       lambda y, t: target_dynamics(y, t, mass_target, Cd_target, area_target, rho))

# Plot the results
plt.plot(t_interceptor, y_interceptor[:,0], label='Interceptor')
plt.plot(t_target, y_target[:,0], label='Target')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()
plt.show()
