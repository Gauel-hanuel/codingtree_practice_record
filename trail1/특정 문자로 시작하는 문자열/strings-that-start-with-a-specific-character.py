import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    arr.append(sys.stdin.readline().strip())

target = sys.stdin.readline().strip()

length = 0
answer = 0

for i in range(n):
    if arr[i][0] == target:
        length += len(arr[i])
        answer += 1
sys.stdout.write(str(answer) + ' ' + f'{(length / answer):.2f}')

