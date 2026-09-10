import sys

A = list(sys.stdin.readline().split())

location = 0

for i in A:
    if int(i) % 3 == 0:
        location = A.index(i)
        break

print(A[int(location) - 1])