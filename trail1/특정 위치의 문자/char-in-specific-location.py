import sys

A = ["L","E","B","R","O","S"]

s = sys.stdin.readline().strip()

if s in A:
    print(A.index(s))
else: 
    print("None")