from math import gcd

class Fraction:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = n
        self.den = d
        self._simplify()

    def _simplify(self):
        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common
        if self.den < 0:
            self.den = -self.den
            self.num = -self.num

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.num * other.den - other.num * self.den
        d = self.den * other.den
        return Fraction(n, d)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        return Fraction(self.num * other.den, self.den * other.num)
