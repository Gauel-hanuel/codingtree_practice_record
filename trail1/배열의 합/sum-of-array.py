import sys

for _ in range(4):
    arr = list(map(int, sys.stdin.readline().split()))
    print(sum(arr))