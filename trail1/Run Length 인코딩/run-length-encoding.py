A = input()

arr = []
arr.append(A[0])

num = 1

for i in range(1, len(A)):
    if A[i-1] == A[i]:
        num += 1
        if i == len(A) - 1:
            arr.append(num)
    elif A[i-1] != A[i]:
        arr.append(num)
        arr.append(A[i])
        num = 1
        if i == len(A) - 1:
            arr.append(num)

if len(A) == 1:
    arr.append(1)

ans = str('')

for i in range(len(arr)):
    ans += str(arr[i])

print(len(ans))
print(ans)



