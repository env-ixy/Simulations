import numpy as np
import matplotlib.pyplot as plt

xs = []  # x-positions
ys = []  # y-position
times = []
distance = []


def walk(n_steps):
    x = 0  # initial position-x
    y = 0  # initial position-y
    positions_x = []
    positions_y = []

    for _ in range(n_steps):
        direction = np.random.randint(4)
        if direction == 0:
            x += 1
        elif direction == 1:
            x -= 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            y -= 1

        positions_x.append(x)
        positions_y.append(y)

    return {
        "min_x": min(positions_x),
        "min_y": min(positions_y),
        "final_x": positions_x[-1],
        "final_y": positions_y[-1],
        "max_x": max(positions_x),
        "max_y": max(positions_y),
        "max_abs_x": np.max(np.abs(positions_x)),
        "max_abs_y": np.max(np.abs(positions_y)),
    }


with open("logs.txt", "w") as f:
    f.write(
        "| min_x | final_x | max_x | max_abs_x | min_y | final_y | max_y | max_abs_y |\n"
    )

    for sim in range(10000):
        result = walk(10000)

        f.write(
            f"| {result['min_x']} | "
            f"{result['final_x']} | "
            f"{result['max_x']} | "
            f"{result['max_abs_x']} | "
            f"{result['min_y']} | "
            f"{result['final_y']} | "
            f"{result['max_y']} | "
            f"{result['max_abs_y']} |\n"
        )

        xs.append(result["final_x"])
        ys.append(result["final_y"])
        times.append(sim)
        distance.append(np.sqrt(result["final_x"] ** 2 + result["final_y"] ** 2))

# plt.scatter(xs, ys, s=1)
plt.hist(distance)
plt.axis("equal")
plt.show()
