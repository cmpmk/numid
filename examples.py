from pylab import *
from numid import *

# Example using Euler's Method for ODEs:
f = lambda x, y: 2*x*y # y(1) = 1, find y(1.5)
xn, yn = eul(f, 1, 1, 1.5)

# Plot Numerical (Euler's) vs Analytical Solution:
# Analytical Solution:
x = linspace(1, 1.5, 6)
y = 0.36787*exp(x**2)

plot(x, y, 'r', label='analytical')
plot(xn, yn, 'b', label='numerical')
legend()
show()

# Example for double integration via midpoint method:
#def f(x,y):
#    return 2*x+y
#midpoint_dbl(f, 0, 2, 2, 3, 5, 5)

# Test the calculation times of trapezoidal and trapvec methods
import time
from numid import trapezoidal, trapvec

f = lambda x: sin(exp(x) -((cos(exp(5)))))

start = time.time()
print(trapezoidal(f, 1, 100, 1000000))
end = time.time()
print('trapezoidal finished in ', (end-start))

start = time.time()
print(trapvec(f, 1, 100, 1000000))
end = time.time()
print('trapvec finished in ', (end-start))
