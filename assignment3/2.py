
#approach 1
import numpy as np
import random
n = int(input("n = "))
array = np.empty(n)
for i in range(0,n):
    duplicate = True
    while(duplicate):
        rand = random.randint(0,99)
        if rand not in array:
            duplicate = False
            array[i] = rand

print(array)

        
#approach 2
arr2 = []
n = int(input("n = "))
for i in range(0,n):
    duplicate = True
    while(duplicate):
        rand = random.randint(0,99)
        if rand not in arr2:
            duplicate = False
            arr2.append(rand)

print(arr2)
