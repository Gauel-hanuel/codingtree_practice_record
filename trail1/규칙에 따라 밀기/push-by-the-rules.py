obj = input()
arr = list(input())

for i in range(len(arr)):
    if arr[i] == 'R':
        obj = obj[-1] + obj[:-1]
    elif arr[i] == 'L':
        obj = obj[1:] + obj[0]

print(obj)