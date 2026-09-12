import sys

sum = 0

for i in range(1,5):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(i):
        sum += arr[i]

print(sum)
