ee = 0
eb = 0

sen = input()

for i in range(len(sen) - 1):
    if str(sen[i])+str(sen[i + 1]) == 'ee' :
        ee += 1
    elif str(sen[i])+str(sen[i + 1]) == 'eb' :
        eb += 1

print(ee, eb)