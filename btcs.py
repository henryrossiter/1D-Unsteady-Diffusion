import numpy as np
from scipy.sparse import diags

def btcs(alpha, t_max, x_max, f, u_0, u_x_max, dt, dx):
    print('Running btcs scheme')
    r = alpha * dt / (dx**2)

    # Create grid
    n_t = int(t_max // dt) + 1
    n_x = int(x_max // dx) + 1
    print('\tnumber of time steps: {}\n\tnumber of spacial steps: {}'.format(n_t, n_x))

    # Coefficients of tridiagonal system
    b = (-alpha/(dx**2))*np.ones((n_x))
    c = b
    a = (1/dt)*np.ones((n_x)) - (b+c)
    
    # Create tridiagonal matrix
    matrix = diags([a, b, c], [0, 1, -1]).toarray()
    matrix[0, :] = 0
    matrix[0, 0] = 1
    matrix[-1, :] = 0
    matrix[-1, -1] = 1


    u = np.zeros((n_x, n_t))
    x = np.linspace(0, x_max, n_x)
    t = np.linspace(0, t_max, n_t)

    # Set initial condition
    for i in range(1, n_x - 1):
        u[i, 0] = f(x[i])

    # Solve system at every time step
    for k in range(1, n_t):
        d = u[:, k-1]/dt
        d[0] = u_0
        d[-1] = u_x_max
        u[:, k] = np.linalg.solve(matrix, d)
    return u