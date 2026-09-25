A = input()
B = input()

a = list(A)
b = list(B)

while True:
    for i in range(len(a) - 1):
        if a[i:i+len(b)] == b:
            del a[i:i+len(b)]
    A = ''.join(a)
    B = ''.join(b)
    if B not in A:
        break

print(A)
