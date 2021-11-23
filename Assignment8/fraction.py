from math import gcd #because, why invent the wheel again?! :)

class Fraction:
    def __init__(self, soorat, makhraj):
        self.soorat = int(soorat)
        self.makhraj = int(makhraj)

    def toString(self):
        return (str(self.soorat)+'/'+str(self.makhraj))

    def simplify(self):
        bmm = gcd(self.soorat, self.makhraj)
        soorat = self.soorat / bmm
        makhraj = self.makhraj / bmm
        return Fraction(soorat, makhraj)

    def add(self, f2):
        makhraj = self.makhraj * f2.makhraj
        soorat = self.soorat*f2.makhraj + self.makhraj*f2.soorat
        return Fraction(soorat, makhraj).simplify()

    def subtract(self, f2):
        makhraj = self.makhraj * f2.makhraj
        soorat = self.soorat*f2.makhraj - self.makhraj*f2.soorat
        return Fraction(soorat, makhraj).simplify()

    def multiply(self, f2):
        soorat = self.soorat * f2.soorat
        makhraj = self.makhraj * f2.makhraj
        return Fraction(soorat,makhraj).simplify()

    def divide(self, f2):
        soorat = self.soorat * f2.makhraj
        makhraj = self.makhraj * f2.soorat
        return Fraction(soorat,makhraj).simplify()

f1s = input('first fraction soorat: ')
f1m = input('first fraction makhraj: ')
f1 = Fraction(f1s, f1m)
f2s = input('second fraction soorat: ')
f2m = input('second fraction makhraj: ')
f2 = Fraction(f2s, f2m)

print('addition = ' + f1.add(f2).toString())
print('subtraction = ' + f1.subtract(f2).toString())
print('multipication = ' + f1.multiply(f2).toString())
print('division = ' + f1.divide(f2).toString())



