sen = input()
sen = list(sen)

while len(sen) is not int(1):
    c = int(input())
    if c >= len(sen):
        del sen[-1]
        print(''.join(sen))
    else:
        del sen[c]
        print(''.join(sen))
