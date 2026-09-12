import sys

arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

print(sum(arr1) / len(arr1), sum(arr2) / len(arr2))
for i in range(4):
    print((arr1[i]+arr2[i]) / 2, end =  ' ')
print()
print(f"{(sum(arr1) + sum(arr2)) / (len(arr1) + len(arr2)):.1f}")