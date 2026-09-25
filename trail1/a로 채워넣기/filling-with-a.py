sen = input()

arr = list(sen)

arr[1], arr[-2] = 'a','a'

ans = ''.join(arr)

print(ans)