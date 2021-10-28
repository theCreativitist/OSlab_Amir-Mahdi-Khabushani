#fibonachi

n = int(input("n : "))
listt = [0,1]
for i in range(2,n+1):
    listt.append(listt[i-2]+listt[i-1])
print(listt)
