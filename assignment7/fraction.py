class fraction:
    def __init__(self, soorat, makhraj):
        self.soorat = int(soorat)
        self.makhraj = int(makhraj)

    def toString(self):
        return (str(self.soorat)+'/'+str(self.makhraj))

    def add(self, f2):
        makhraj = self.makhraj * f2.makhraj
        soorat = self.soorat*f2.makhraj + self.makhraj*f2.soorat
        return fraction(soorat, makhraj)

    def subtract(self, f2):
        makhraj = self.makhraj * f2.makhraj
        soorat = self.soorat*f2.makhraj - self.makhraj*f2.soorat
        return fraction(soorat, makhraj)

    def multiply(self, f2):
        soorat = self.soorat * f2.soorat
        makhraj = self.makhraj * f2.makhraj
        return fraction(soorat,makhraj)

    def divide(self, f2):
        soorat = self.soorat * f2.makhraj
        makhraj = self.makhraj * f2.soorat
        return fraction(soorat,makhraj)

f1s = input('first fraction soorat: ')
f1m = input('first fraction makhraj: ')
f1 = fraction(f1s, f1m)
f2s = input('second fraction soorat: ')
f2m = input('second fraction makhraj: ')
f2 = fraction(f2s, f2m)

print('addition = ' + f1.add(f2).toString())
print('subtraction = ' + f1.subtract(f2).toString())
print('multipication = ' + f1.multiply(f2).toString())
print('division = ' + f1.divide(f2).toString())



