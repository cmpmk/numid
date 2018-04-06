from numpy import sqrt, exp, linspace

def trap(f, a, b, n):
    h = float(b-a)/n
    result = 0.5*(f(a) + f(b))
    for k in range(1,n):
        result += f(a + k*h)
    result *= h
    return result

def trapvec(f, a, b, n):
    h = float(b-a)/n
    x = linspace(a, b, n+1)
    s = sum(f(x)) - 0.5*(f(a) + f(b))
    return h*s

def mdpt(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + 0.5*h) + i*h)
    result *= h
    return result

def mdpt_dbl(f, a, b, c, d, nx, ny):
    hx = (b-a)/float(nx)
    hy = (d-c)/float(ny)
    I = 0
    for i in range(nx):
        for j in range(ny):
            xi = a + 0.5*hx + i*hx
            yj = c + 0.5*hy + j*hy
            I += hx*hy*f(xi, yj)
    return I
'''
Example: 
def f(x,y):
    return 2*x + y
midpoint_dbl(f, 0, 2, 2, 3, 5, 5)
'''

# Forward Difference Method:
def fd(f, x, h):
    num = float(f(x+h) - f(x))
    return num/h

# Central Difference Method:
def cd(f, x, h):
    f1 = f(x-2*h) + 8*f(x+h)
    f2 = 8*f(x-h) + f(x+2*h)
    cd = (1.0/12*h)*(f1 - f2)
    return cd
