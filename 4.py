def fact(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum
# creating a list of factoriel numbers!
#because its so bad for performance if we check every time the number is entered!
fac_nums = []
for i in range(0,12):
    fac_nums.append(fact(i))
num = int(input("n = "))
if num in fac_nums:
    print('yes')
else:
    print('no')
