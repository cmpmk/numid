import time
from numid import trapezoidal, trapvec
from numpy import *

f = lambda x: sin(exp(x) -((cos(exp(5)))))

start = time.time()
print(trapezoidal(f, 1, 100, 1000000))
end = time.time()
print('trapezoidal finished in ', (end-start))

start = time.time()
print(trapvec(f, 1, 100, 1000000))
end = time.time()
print('trapvec finished in ', (end-start))
