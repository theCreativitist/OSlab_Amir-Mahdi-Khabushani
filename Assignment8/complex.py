from decimal import Decimal

class Complex:
    def __init__(self, a=0, b=0):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))

    def print(self):
        print(self.a,'+',self.b,'i')
        
    def add(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a,b)

    def subtract(self, other):
        a = self.a - other.a
        b = self.b - other.b
        return Complex(a,b)

    def multiply(self, other):
        a = self.a*other.a - self.b*other.b
        b = self.a*other.b + self.b*other.a
        return Complex(a,b)

while(1):
    a1 = input('\nc1 real part: ')
    b1 = input('c1 imaginary part: ')
    a2 = input('c1 real part: ')
    b2 = input('c1 imaginary part: ')
    c1 = Complex(a1,b1)
    c2 = Complex(a2,b2)
    print('\nc1 is')
    c1.print()
    print('c2 is')
    c2.print()
    print('\nc1 + c2 =')
    c1.add(c2).print()
    print('\nc1 - c2 =')
    c1.subtract(c2).print()
    print('\nc1 * c2 =')
    c1.multiply(c2).print()

