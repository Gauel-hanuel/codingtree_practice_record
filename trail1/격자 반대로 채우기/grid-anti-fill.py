n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

num = 1

for j in range(0, n):
    for i in range(0, n):
        if j % 2 == 0 :
            arr[n - 1 - i][n - 1 - j] = num
            num += 1
        else:
            arr[i][n - 1 - j] = num
            num += 1

for row in arr:
    print(*row)