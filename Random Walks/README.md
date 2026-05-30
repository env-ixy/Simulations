# Rules
Start at position $x\in\mathbb{Z}$. With equal probablity:
- move left ($+1$)
- move right ($-1$)

# Use cases
Random walk-adjacent patterns are seen in:
- pollen in water
- diffusion
- Brownian motion
- ants
- stock prices

For a simple 1D walk, i can do:
$$
x = 
\begin{cases}
    x+1, & \text{if}\ a = 1\\
    x-1, & \text{if}\ a = 0\\
\end{cases}
$$

where $a = 0 \text{ OR } a = 1$ because numpy random numbers are between 0 and 1, I round it to the nearest integer.

After 10 runs, the best position, the last position and the mean position are as follows:
|index|$\max(x)$|final $x$|$\bar{x}$
| ---- | ---- | ---- | ---- |
|1| 3 | 2 | -1.34 | 
|2| 3 | -14 | -5.58 | 
|3| 9 | 8 | -0.5 | 
|4| 3 | -4 | -1.32 | 
|5| 0 | -2 | -4.34 | 
|6| 3 | -22 | -8.44 | 
|7| 11 | 10 | 6.8 | 
|8| 6 | -2 | 1.3 | 
|9| 27 | 24 | 13.3 | 
|10| 4 | 2 | 0.4 | 
