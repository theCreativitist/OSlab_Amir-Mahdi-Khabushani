arr = []
end=False
while(not end):
    n = input("enter n (enter 'x' for end) : ")
    if (n != 'x'):
        arr.append(int(n))
    else:
        end = True
last = -99999

for i in arr:
    if i >= last:
        last = i
        continue
    else:
        print('no')
        exit()
print('yes')

