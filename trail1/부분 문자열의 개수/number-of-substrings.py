target = input()
object = input()
count = 0

if object in target:
    for i in range(len(target) - 1):
        if target[i:i+2] == object:
            count +=1

print(count)