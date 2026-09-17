import sys

arr = list(map(str, sys.stdin.readline().split()))

for i in range(0,10,2):
    sys.stdout.write(str(arr[i]) + '\n')

