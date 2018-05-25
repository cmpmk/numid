from pylab import *

from numid import *

# Example using Euler's Method for ODEs:
f = lambda x, y: 2*x*y # y(1) = 1, find y(1.5)
xn, yn = eul(f, 1, 1, 1.5)

# Plot Numerical (Euler's) vs Analytical Solution:
# Analytical Solution:
x = array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5])
y = 0.36787*exp(x**2)

plot(x, y, 'r', label='analytical')
plot(xn, yn, 'b', label='numerical')
legend()
show()


# Example for double integration via midpoint method:
#def f(x,y):
#    return 2*x+y
#midpoint_dbl(f, 0, 2, 2, 3, 5, 5)
