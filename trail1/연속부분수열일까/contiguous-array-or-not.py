import sys

a , b = map(int, sys.stdin.readline().split())
n1 = list(map(int, sys.stdin.readline().split()))
n2 = list(map(int, sys.stdin.readline().split()))
loc = [index for index, values in enumerate(n1) if values == n2[0]]
if n2[0] in n1:
    for i in loc:
        if n1[i : i +b] == n2:
            print("Yes")
            break
    else: 
        print("No")
else :
    print("No")