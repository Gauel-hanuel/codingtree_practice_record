arr = list(input())

first, second = arr[0], arr[1]

for i in range(len(arr)):
    if arr[i] == second:
        arr[i] = first
    
print(''.join(arr))