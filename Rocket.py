import numpy as np
import matplotlib.pyplot as plt

# Corners were cut in this project, esspecially in calculating the drag coefficient
# This is not a "professional" simulation and this is assuming a rocket would go "straight" up

# Setup

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

dt = 0.1
total_time = 360 # second

gravity = 9.8 # Newtons

empty_mass = 500 # kg
fuel_mass = 1000 # kg
thrust = 15000 # Newtons
burn_rate = 4
diameter = 0.5 # meters
Cd = 0.5 # Coefficent
radius = diameter / 2
area = np.pi * radius**2



rho = 1.225 #kg/m**3 while under 5500


drag = 0.5

# Start Conditions

height = 0
velocity = 0

time_list = []
height_list = []
velocity_list = []

t = 0

while t < total_time:

    mass = empty_mass + fuel_mass

    # Check if there is fuel left
    if fuel_mass > 0:
        fuel_mass -= burn_rate * dt
        fuel_mass = max(fuel_mass, 0)
    else:
        thrust = 0
    # Setup for drag coefficient

    if height < 5500:
        rho = 1.225 # kg/m**3
    elif height > 5500 and height < 11000:
        rho = 0.736 # kg/m**3
    elif height > 11000 and height < 50000:
        rho = 0.336 # kg/m**3
    elif height > 50000:
        rho = 0.001

    # Drag coefficient
    drag_force = -0.5 * rho * velocity * abs(velocity) * Cd * area

    # Forces
    weight = mass * gravity
    force = thrust - weight + drag_force

    # physics
    acceleration = force / mass
    velocity += acceleration * dt
    height += velocity * dt

    if height < 0:
        height = 0
        velocity = 0

    # Convert into numpy arrays

    time_list.append(t)
    height_list.append(height)
    velocity_list.append(velocity)

    time_array = np.array(time_list)
    height_array = np.array(height_list)
    velocity_array = np.array(velocity_list)

    t += dt

# Plotting

axes[0].plot(time_array,velocity_array)
axes[0].set_title("Velocity")
axes[0].set_xlabel("Time (s)")
axes[0].set_ylabel("Velocity (m/s)")
axes[0].grid(True)

axes[1].plot(time_array,height_array)
axes[1].set_title("Height")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Height (m)")
axes[1].grid(True)

# AI was used for minor debugging.

plt.tight_layout()
plt.show()
