# class
class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def __str__(self):
        return f"{self.r} + {self.i}i"

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)


    def __mul__(self, other):
        return Complex(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __truediv__(self, other):
        return Complex((self.r * other.r + self.i * other.i) / (other.r * other.r + other.i * other.i),
                       (self.i * other.r - self.r * other.i) / (other.r * other.r + other.i * other.i))
    
    def __pow__(self, power):
        return Complex(self.r ** power, self.i ** power)


    def __abs__(self):
        import math
        return math.sqrt(self.r ** 2 + self.i ** 2)


    def __eq__(self, other):
        return self.r == other.r and self.i == other.i


    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return abs(self) < abs(other)


    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __hash__(self):
        return hash((self.r, self.i))

    def __repr__(self):
        return f"Complex({self.r}, {self.i})"

# complex number
x = Complex(1,2)
y = Complex(2,3)

# print
print(x,y)

# add / subtract
print(x + y)
print(x - y)

# abs
print(abs(x))
