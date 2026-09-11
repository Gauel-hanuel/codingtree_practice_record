import sys 

n = sys.stdin.readline()
arr = list(sys.stdin.readline().split())

loc = [index for index, value in enumerate(arr) if value == str(2)]
print(loc[2] + 1)