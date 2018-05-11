from numpy import linspace

# --------------------------- Numerical Integration ------------------------
# Trapezoidal method for integration
# Inputs: function, lower limit, upper limit, number of trapezoids

def trapezoidal(f, a, b, n):
    h = float(b-a)/n
    result = 0.5*(f(a) + f(b))
    for k in range(1,n):
        result += f(a + k*h)
    result *= h
    return result

# Vectorized trapezoidal method
# 04/12/18: has issues, needs fixing.

def trapvec(f, a, b, n):
    h = float(b-a)/n
    x = linspace(a, b, n+1)
    s = sum(f(x)) - 0.5*(f(a) + f(b))
    return h*s

# Midpoint Method for numerical integration
def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + 0.5*h) + i*h)
    result *= h
    return result

# Midpoint Method for Double Integrals
# f: input function
# [a,b]: lower and upper bounds for integral wrt x
# [c,d]: lower and upper bounds for integral wrt y
# [nx,ny]: points along x and points along y

def midpoint_double(f, a, b, c, d, nx, ny):
    hx = (b-a)/float(nx)
    hy = (d-c)/float(ny)
    I = 0
    for i in range(nx):
        for j in range(ny):
            xi = a + 0.5*hx + i*hx
            yj = c + 0.5*hy + j*hy
            I += hx*hy*f(xi, yj)
    return I

# --------------------------- Numerical Differentiation --------------------
''' First Order Derivatives: '''
def ForwardDiff(f, x):
    h = 0.0001
    return (f(x+h) - f(x))/(1.*h)


def BackwardDiff(f, x):
    h = 0.0001
    return (f(x) - f(x-h))/(1.*h)


def CentralDiff(f, x):
    h = 0.0001
    return (f(x+h) - f(x-h))/(2.*h)

''' Second Order Derivatives: '''
def CentralDiff2(f, x):
    h = 0.0001
    return (f(x+h) - 2.*f(x) + f(x-h))/(h*h)
    
    





def help():
    print("Available Functions: \
    trapezoidal(f,a,b,n) \
    midpoint(f,a,b,n) \
    midpoint_double(f, a, b, c, d, nx, ny) \
    ForwardDiff(f, x, h) \
    CentralDiff(f, x, h)")
    
# make a help class that prints functionality and examples for each method
# such as: help.trapezoidal() prints how to use the method

#Example: 
#def f(x,y):
#    return 2*x + y
#midpoint_dbl(f, 0, 2, 2, 3, 5, 5)
