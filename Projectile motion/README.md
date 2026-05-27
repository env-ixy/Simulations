The equation for projectile motion is:

$$
y(t) = v_0 \sin(\theta)t - \frac12 gt^2
$$
$$
\text{Where } g = -9.8ms^{-2}
$$

$v_0$ is the velocity with which the object is thrown. $\theta$ is the angle at which it is thrown. 

To simulate, I must calculate *what* happens to the object at each iteration. Let $dt = 0.1$. So for every $0.1$ seconds, I will calculate what happens to the object. 

The velocity would have to change every iteration. So

$$
v_{t'} = v_t + gdt
$$

$\theta$ for this simulation, I'll let it be 45deg. 

I should create two arrays: `xs` and `ys`. In `xs` I should append to `xs` time. And position to `ys`. 

But gravity only affects the vertical velocity, so I would need to have two velocities: one for sideways motion and the other for vertical motion. 

$$
v_{t'} = v_t + gdt
$$
$$
y_{t'} = y_t + v_{y}dt \quad (\because v = \frac{dx}{dt} \implies x = vdt) 
$$
$$
x_{t'} = x_t + v_xdt
$$

NOTE:
|Symbol|Meaning|
|----|----|
|$x$| horizontal position|
|$y$| vertical position|
|$v_x$| horizontal velocity|
|$v_y$| vertical velocity|

$$
v_x = v_0 \cos(\theta) \\
v_y = v_0 \sin(\theta)
$$
