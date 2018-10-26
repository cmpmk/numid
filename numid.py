from numpy import linspace, zeros, size

# --------------------------------------------------------------------------
# --------------------------- Numerical Integration ------------------------
# --------------------------------------------------------------------------
# Trapezoidal method for integration
# Inputs: function, lower, upper limit, number of trapezoids

def trapezoidal(f, a, b, n):
    h = float(b-a) / n
    result = 0.5*(f(a) + f(b))
    for k in range(1,n):
        result += f(a + k*h)
    result *= h
    return result

def trapvec(f, a, b, n):
    h = float(b-a) / n
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
# [a,b]: lower and upper bounds wrt x, [c,d] : bounds wrt y
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

# --------------------------------------------------------------------------
# --------------------------- Numerical Differentiation --------------------
# --------------------------------------------------------------------------

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

# --------------------------------------------------------------------------    
# --------------------------Numerical Methods for ODEs----------------------
# --------------------------------------------------------------------------    

''' Euler's Method ''' 
def eul(f, x0, xf):
    t = linspace(x0, xf, 1000)
    h = (xf - x0)/1.0e3
    x = zeros(size(t))
    for i in range(size(t)):
        if i == 0:
            x[i] = x0
        else:
            x[i] = x[i-1] + h*f(x[i-1], t[i-1])
    return t, x

''' Runge-Kutta 4th Order '''
def rk4(f, x0, xf):
    t = linspace(x0, xf, 1000)
    #h = (xf - x0)/1.0e3
    h = 0.05
    x = zeros(size(t))
    for i in range(size(t)):
        if i == 0:
            x[i] = x0
        else:
            k1 = h*f(x[i-1], t[i-1])
            k2 = h*f(x[i-1] + 0.5*k1, t[i-1] + 0.5*h)
            k3 = h*f(x[i-1] + 0.5*k2, t[i-1] + 0.5*h)
            k4 = h*f(x[i-1] + k3, t[i-1] + h)
            x[i] = x[i-1] + 1/6.*(k1 + 2*(k2 + k3) + k4)
    return t, x

# --------------------------------------------------------------------------
# ---------------------------General Calls----------------------------------
# --------------------------------------------------------------------------

def Integrate(f, a, b, n, method):
    if method == 'trapvec':
        return trapvec(f, a, b, n)
    if method == 'trapezoidal':
        return trapezoidal(f, a, b, n)
    if method == 'midpoint':
        return midpoint(f, a, b, n)

def Differentiate(f, a, b, n, method):
    if method == 'Forward':
        return ForwardDiff(f, x)
    if method == 'Central':
        return CentralDiff(f, x)
    if method == 'Backward':
        return BackwardDiff(f, x)
