import numpy as np
import matplotlib.pyplot as plt

x = 0 # initial position
ys = [] # positions
xs = [] # time


def walk(n_steps=1000):
    x = 0
    positions = []

    for _ in range(n_steps):
        step = np.random.choice([-1, 1])
        x += step
        positions.append(x)

    return {
        "min": min(positions),
        "final": positions[-1],
        "max": max(positions),
        "max_abs": np.max(np.abs(positions)),
    }


with open("logs.txt", "w") as f:
    f.write("| min | final | max | max abs |\n")

    for sim in range(4000):

        result = walk(4000)
        ys.append(result['final'])
        xs.append(sim)
        f.write(
            f"| {result['min']} | "
            f"{result['final']} | "
            f"{result['max']} | "
            f"{result['max_abs']} |\n"
        )

plt.hist(ys)
plt.show()
print(np.mean(ys))
print(np.std(ys))
