import numpy as np

def ftcs(alpha, t_max, x_max, f, u_0, u_x_max, dt, dx):
    print('Running ftcs scheme')
    r = alpha * dt / (dx**2)

    # Create grid
    n_t = int(t_max // dt) + 1
    n_x = int(x_max // dx) + 1
    print('\tnumber of time steps: {}\n\tnumber of spacial steps: {}'.format(n_t, n_x))
    u = np.zeros((n_x, n_t))
    x = np.linspace(0, x_max, n_x)
    t = np.linspace(0, t_max, n_t)

    # Set initial condition
    for i in range(1, n_x - 1):
        u[i, 0] = f(x[i])

    # Apply ftcs scheme
    for i in range(0, n_t - 1):
        for j in range(1, n_x - 1):
            u[j, i + 1] = u[j, i] + r * (u[j + 1, i] - 2*u[j, i] + u[j - 1, i])

    return u


