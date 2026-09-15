a = str(input())

count = 0

obj = str(input())

for i in range(len(a)):
    if obj == a[i]:
        count += 1

print(count)