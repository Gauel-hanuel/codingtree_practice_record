n = int(input())

arr = [[0 for _ in range(n)] for  _ in range(n)]

arr[0][0] = 1

for i in range(1, n):
    arr[i][0] = 1
    arr[i][i] = 1

for i in range(1, n):
    for j in range(1, i):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

for row in arr:
    for element in row:
        if element == 0:
            pass
        else: print(element, end = ' ')
    print()