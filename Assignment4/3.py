#jadval zarbh n*m

n = int(input("enter n:"))
m = int(input("enter m:"))

print('   ',end='')
for a in range(1,n):
    print(a,end=' ')
print()
for i in range(1,n):
    print(i,end='| ')
    for j in range(1,m):
        print(i*j,end=' ')
    print()
