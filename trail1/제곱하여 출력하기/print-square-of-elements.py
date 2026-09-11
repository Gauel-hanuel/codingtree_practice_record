import sys

n = sys.stdin.readline()
arr = list(map(int, sys.stdin.readline().split()))

for i in range(int(n)):
    print(arr[i] ** 2, end = ' ')