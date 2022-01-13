from math import factorial as f
n = input('n=')
for i in range(int(n)):
    for j in range(i+1):
        print(f(i)//(f(j)*f(i-j)), end=' ')
    print()
