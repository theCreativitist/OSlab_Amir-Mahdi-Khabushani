n = input("n = ")
num_digits = len(n)
sum = 0
for d in n:
    sum += int(d) ** num_digits
if sum == int(n):
    print('yes')
else:
    print('no')
