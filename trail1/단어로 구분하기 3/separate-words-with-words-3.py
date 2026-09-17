import sys

arr = list(map(str, sys.stdin.readline().split()))

for i in range(9,-1,-1):
    sys.stdout.write(str(arr[i]) + '\n')

