import numpy as np
import matplotlib.pyplot as plt

x = 0 # initial position
ys = [] # positions
xs = [] # time

def move():
    a = round(np.random.rand()) 
    global x
    if a == 0:
        x -= 1 # move left
    else:
        x += 1 # move right
    return x
    
for i in range(100):
    ys.append(move())
    xs.append(i) # time
    
plt.plot(xs, ys)
plt.show()

with open("logs.txt", "a") as f:
    f.write(f"| {max(ys)} | ") # record highest position
    f.write(f"| {ys[-1]} | ") # record final position
    f.write(f"| {np.mean(ys)} | ") # record mean position
    f.write("\n")