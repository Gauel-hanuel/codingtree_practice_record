import sys 

for _ in range(5):
    arr = list(map(str, sys.stdin.readline().split()))
    for A in arr[:-1]:
        print(A.upper(), end = ' ')
    print(str(arr[2]).upper())
