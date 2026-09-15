n, m = tuple(map(int, input().split()))

arr = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = tuple(map(int, input().split()))
    arr[a - 1][b -1 ] = 1

for row in arr:
    print(*row)