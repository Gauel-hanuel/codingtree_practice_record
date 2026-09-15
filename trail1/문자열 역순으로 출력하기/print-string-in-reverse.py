import sys

list = []

for _ in range(4):
    list.append(sys.stdin.readline())

for i in range(3, -1, -1):
    print(list[i], end = '')