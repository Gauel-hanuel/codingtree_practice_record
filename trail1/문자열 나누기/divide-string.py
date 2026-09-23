n = input()
a = ''.join(list(map(str, input().split())))

for i in range(0,len(a) // 5 + 1):
    print(a[5*i:5*i+5])
