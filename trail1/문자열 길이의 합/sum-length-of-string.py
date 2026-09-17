import sys

n = int(sys.stdin.readline().strip())

length = 0
location = 0 
list = []

for i in range(n):
    list.append(sys.stdin.readline().strip())

for i in range(n):
    length += len(list[i])
    if list[i][0] == 'a':
        location += 1


sys.stdout.write(str(length) + " " + str(location))

