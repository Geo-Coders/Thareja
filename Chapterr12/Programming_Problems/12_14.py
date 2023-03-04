# A program that overloads the -= and /= operators in COMPLEX class.
# The program must throw an exception if divide by zero exception occurs or if the real part of the two objects are zero

print('--- A Program to overload -= and /= operators in complex class---')
print()


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __iadd__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self

    def __isub__(self, other):
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __idiv__(self, other):
        if other.real == 0 or self.real == 0:
            raise Exception("Divide by zero error or zero real part")
        self.real /= other.real
        self.imag /= other.imag
        return self

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# testing the overloaded operators
c1 = Complex(2, 3)
c2 = Complex(1, 2)

# testing -= operator
c1 -= c2
print(c1)  # output: 1 + 1i

# testing /= operator
c3 = Complex(0, 2)
try:
    c2 /= c3  # raises an exception due to divide by zero error
except Exception as e:
    print(e)  # output: Divide by zero error or zero real part
