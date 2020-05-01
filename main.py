# Henry Rossiter
from ftcs import ftcs
from btcs import btcs
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

ftcs_solution = ftcs(alpha, .1, x_max, f, u_0, u_x_max, dt, dx)
btcs_solution = btcs(alpha, .1, x_max, f, u_0, u_x_max, dt, dx)

print('FTCS Solution at x=6, t=0.1: {}'.format(ftcs_solution[6, -1]))
print('BTCS Solution at x=6, t=0.1: {}'.format(btcs_solution[6, -1]))

plt.plot(btcs_solution[:,-1], label='btcs')
plt.plot(ftcs_solution[:,-1], label='ftcs')
plt.title('Solution at t=0.1')
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
#plt.imshow(ftcs_solution, cmap='hot', interpolation='nearest')
#plt.imshow(btcs_solution, cmap='hot', interpolation='nearest')
plt.show()