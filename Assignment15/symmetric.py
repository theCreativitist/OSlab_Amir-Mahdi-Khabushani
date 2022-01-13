
def isSymmetric(array):
    mid = len(array) // 2
    first_half = array[:mid]
    if len(array) % 2 != 0: #odd
        second_half = array[mid+1:]
    else: #even
        second_half = array[mid:]
    second_half.reverse()

    if first_half == second_half:
        return True
    else:
        return False

arr = []
while(True):
    inp = input('add item to list(f for finish):')
    if inp!='f':
        arr.append(inp)
    else:
        break

if isSymmetric(arr):
    print(arr,'is Symmetric!')
else:
    print(arr,'is not  Symmetric!')


