# Henry Rossiter
from ftcs import ftcs
import matplotlib.pyplot as plt

# alpha
alpha = 1

# Domain is 0 < x < x_max, 0 < t
x_max = 20

# Set IC
def f(x):
    if 8 <= x <= 12:
        return 2 - abs(x - 10)
    return 0

# Set BC's
u_0 = 0
u_x_max = 0

# Time and space step sizes
dt = 0.1
dx = 1

ftcs_solution = ftcs(alpha, 10, x_max, f, u_0, u_x_max, dt, dx)
plt.imshow(ftcs_solution, cmap='hot', interpolation='nearest')
plt.show()