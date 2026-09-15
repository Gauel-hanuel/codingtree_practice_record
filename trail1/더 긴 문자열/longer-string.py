a , b = map(str, input().split())

lena, lenb = len(a), len(b)

if lena > lenb:
    print(a, lena)
elif lena < lenb:
    print(b, lenb)
elif lena == lenb:
    print("same")