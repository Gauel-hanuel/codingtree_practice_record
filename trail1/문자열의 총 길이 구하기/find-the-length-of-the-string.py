import sys

arr = list(map(str, sys.stdin.readline().rstrip().split()))

length = 0

for i in range(len(arr)):
    length += len(arr[i])

print(length)


