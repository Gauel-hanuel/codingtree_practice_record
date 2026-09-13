a, b = map(int,input().split())

for i in range(a):
    for j in range(b):
        print(i * b + j + 1, end = ' ')
    print()