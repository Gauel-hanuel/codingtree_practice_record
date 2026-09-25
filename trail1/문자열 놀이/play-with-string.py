obj, n = input().split()
obj = list(obj)

for i in range(int(n)):
    a, b, c = input().split()
    if int(a) == 1 :
        temp1, temp2 = obj[int(b)-1], obj[int(c)-1]
        obj[int(b)-1] = temp2
        obj[int(c)-1] = temp1
        print(''.join(obj))
    elif int(a) == 2:
        for i in range(len(obj)):
            if obj[i] == b:
                obj[i] = c
        print(''.join(obj))