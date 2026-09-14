n, m = map(int, input().split())

arr = [[1 for _ in range(m)] for _ in range(n)]

num = 2

for sum in range(1, n + m):
    for i in range(0, sum + 1):
        if i >= n:
            pass
        elif sum - i >= m: 
            pass
        else :
            arr[i][sum - i] = num
            num += 1

for row in arr:
    for num in row:
        print(num, end = ' ')
    print( )
