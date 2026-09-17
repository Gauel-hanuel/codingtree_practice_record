import sys

arr = list(map(str, sys.stdin.readline().split()))

for i in range(10):
    sys.stdout.write(str(arr[i]) + '\n')

