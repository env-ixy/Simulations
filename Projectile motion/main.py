import numpy as np
import matplotlib.pyplot as plt

# CONSTANTS
g = -9.8 # (-ve since going up)
dt = 0.01  
theta = np.pi / 4  # 45deg in radians
v0 = 20  

# INITIAL TIME
t = 0

# INITIAL POSITION
x = 0
y = 0

# INITIAL VELOCITIES
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)

# ARRAYS FOR PLOTTING
xs = []
ys = []

while y >= 0:
    vy += g*dt # v_t' = v_t + gdt
    x += vx*dt # change horizontal position
    y += vy*dt # change veritical position 
    xs.append(x)
    ys.append(y)
    t+=dt # update time

plt.plot(xs, ys)
plt.show()