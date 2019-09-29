from numpy import linspace, zeros, size

class numid:
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n
        self.h = float(self.b - self.a) / self.n
# Trapezoidal method    
    def trapezoidal(self):
        result = 0.5*(self.f(self.a) + self.f(self.b))
        for k in range(1, self.n):
            result += self.f(self.a + k * self.h)
        result *= self.h
        return round(result, 2)

# Vectorized trapezoidal method
    def trapvec(self):
        x = linspace(self.a, self.b, self.n + 1)
        s = sum(self.f(x)) - 0.5*(self.f(self.a) + self.f(self.b))
        return round(self.h * s, 2)
    
# Midpoint method for numerical integration
    def midpoint(self):
        result = 0
        for i in range(self.n):
            result += self.f((self.a + 0.5*self.h) + i*self.h)
        result *= self.h
        return result

