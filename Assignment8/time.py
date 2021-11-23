class Time:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
        self.correct()

    def print(self):
        print(self.h, ':', self.m, ':', self.s)

    def correct(self):
        if self.s >= 60 or self.s < 0:
            m = self.s // 60 # number of whole minutes in the seconds
            mod = self.s % 60 # baghimande
            self.m += m
            self.s = mod
        if self.m >= 60 or self.m < 0:
            h = self.m // 60 # number of whole hours in the minutes
            mod_h = self.m % 60 # baghimande
            self.h += h
            self.m = mod_h
        return self

    def add(self, other):
        h = self.h + other.h
        m = self.m + other.m
        s = self.s + other.s
        return Time(h,m,s).correct()

    def subtract(self, other):
        h = self.h - other.h
        m = self.m - other.m
        s = self.s - other.s
        return Time(h,m,s).correct()

    def toSeconds(self):
        return self.s + (self.m * 60) + (self.h * 3600)

    def fromSeconds(self, s):
        h = s // 3600
        s %= 3600
        m = s // 60
        s %= 60
        self.h = h
        self.m = m
        self.s = s
        return self
        

while(1):
    h1=input('\nh1:')
    m1=input('m1:')
    s1=input('s1:')
    h2=input('h1:')
    m2=input('m1:')
    s2=input('s1:')
    t1 = Time(int(h1),int(m1),int(s1))
    t2 = Time(int(h2),int(m2),int(s2))

    print('\nt1 is ')
    t1.print()
    print('t2 is ')
    t2.print()

    print('\nt1 + t2 = ')
    t1.add(t2).print()
    print('\nt1 - t2 = ')
    t1.subtract(t2).print()
    print('\nt1 to seconds = ',t1.toSeconds())
    print('t2 to seconds = ',t2.toSeconds())

    s = input('\nenter seconds : ')
    print(s, ' to time is ')
    t = Time()
    t.fromSeconds(int(s)).print()
    
