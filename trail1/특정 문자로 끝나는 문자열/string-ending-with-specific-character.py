import sys

arr = []

for i in range(11):
    arr.append(sys.stdin.readline().strip())

target = arr[-1]

ans = []

for i in range(10):
    if arr[i][-1] == target:
        ans.append(arr[i])

if len(ans) is not 0:
    for i in range(len(ans)):
        sys.stdout.write(str(ans[i]) + '\n')
elif len(ans) is 0:
    sys.stdout.write('None')


