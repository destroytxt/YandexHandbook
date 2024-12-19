class Fraction:

    def __init__(self, a, b=1):
        if isinstance(a, str) and '/' in a:
            self.num, self.den = [int(c) for c in a.split('/')]
        else:
            self.num = int(a)
            self.den = b
        self.__reduce()

    def __reduce(self):
        a = abs(self.num)
        b = abs(self.den)
        while b:
            a, b = b, a % b
        self.num = self.num // abs(a)
        self.den = self.den // abs(a)
        if self.den < 0:
            self.num = -self.num
            self.den = abs(self.den)

    def __sign(self):
        return -1 if self.num < 0 else 1

    def __comparison(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        return self.num * other.den, other.num * self.den

    def __is_fraction(self, other):
        return isinstance(other, Fraction)

    def numerator(self, number=None):
        if number:
            self.num = number * self.__sign()
            self.__reduce()
        return self.num

    def denominator(self, number=None):
        if number:
            self.den = number * self.__sign()
            self.__reduce()
        return self.den

    def reverse(self):
        rev = self.num
        self.num = self.den
        self.den = rev
        self.__reduce()
        return self

    def __str__(self):
        string = f'{self.num}/{self.den}'
        return string

    def __repr__(self):
        string = f'{self.num}/{self.den}'
        return f'Fraction(\'{string}\')'

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __add__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        denominator = self.den * other.den
        numerator = self.num * other.den + other.num * self.den
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        denominator = self.den * other.den
        numerator = self.num * other.den - other.num * self.den
        return Fraction(numerator, denominator)

    def __radd__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        denominator = self.den * other.den
        numerator = self.num * other.den + other.num * self.den
        return Fraction(numerator, denominator)

    def __rsub__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        denominator = self.den * other.den
        numerator = other.num * self.den - self.num * other.den
        return Fraction(numerator, denominator)

    def __rmul__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        return Fraction(self.num * other.num, self.den * other.den)

    def __rtruediv__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        return Fraction(self.den * other.num, self.num * other.den)

    def __iadd__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        self.num = self.num * other.den + other.num * self.den
        self.den = self.den * other.den
        self.__reduce()
        return self

    def __isub__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        self.num = self.num * other.den - other.num * self.den
        self.den = self.den * other.den
        self.__reduce()
        return self

    def __mul__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        return Fraction(self.num * other.den, self.den * other.num)

    def __imul__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        self.num *= other.num
        self.den *= other.den
        self.__reduce()
        return self

    def __itruediv__(self, other):
        if not self.__is_fraction(other):
            other = Fraction(other)
        self.num *= other.den
        self.den *= other.num
        self.__reduce()
        return self

    def __gt__(self, other):
        num, other_num = self.__comparison(other)
        return num > other_num

    def __lt__(self, other):
        num, other_num = self.__comparison(other)
        return num < other_num

    def __ge__(self, other):
        num, other_num = self.__comparison(other)
        return num >= other_num

    def __le__(self, other):
        num, other_num = self.__comparison(other)
        return num <= other_num

    def __eq__(self, other):
        num, other_num = self.__comparison(other)
        return num == other_num

    def __ne__(self, other):
        num, other_num = self.__comparison(other)
        return num != other_num
