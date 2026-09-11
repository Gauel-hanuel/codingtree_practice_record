import sys

N, Q = map(int, sys.stdin.readline().split())

seq = list(sys.stdin.readline().split())

for i in range(Q):
    templist = list(sys.stdin.readline().split())
    if templist[0] == str(1):
        print(seq[int(templist[1]) - 1])
    elif templist[0] == str(2):
        if str(templist[1]) in seq:
            print(seq.index(str(templist[1])) + 1)
        else :
            print(0)
    elif templist[0] == str(3):
        for i in range(int(templist[1]) - 1, int(templist[2]) - 1):
            print(seq[i], end = ' ')
        print(seq[int(templist[2]) - 1])
        