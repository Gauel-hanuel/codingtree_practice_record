object = input()

first = object[0]
second = object[1]

arr = list(object)

for i in range(len(arr)):
    if arr[i] == first:
        arr[i] = second
    elif arr[i] == second:
        arr[i] = first

print(''.join(arr))