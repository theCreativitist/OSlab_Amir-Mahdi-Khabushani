def bmm(a,b):
    if a > b: 
        lower = b 
    else:
        lower = a 
    for i in range(1, lower+1): 
        if((a % i == 0) and (b % i == 0)): 
            bmm = i
    return bmm


a = int(input('a = '))
b = int(input('b = '))
print('kmm is ', (a*b)/(bmm(a,b)))
