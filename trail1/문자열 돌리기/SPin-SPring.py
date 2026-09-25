a = input()

print(a)

for i in range(1, len(a)+1):
    print(a[-i:] + a[0:len(a)-i])