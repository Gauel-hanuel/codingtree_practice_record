import sys

N, M = map(int, sys.stdin.readline().split())
list = list(sys.stdin.readline().split())

count = 0

for i in range(N):
    if int(M) == int(list[i]):
        count += 1

print(count)

