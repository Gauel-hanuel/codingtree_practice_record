arr = ["apple", "banana", "grape", "blueberry", "orange"]

obj = input()
count  = 0 

for elem in arr:
    if elem[2] == obj or elem[3] == obj:
        print(elem)
        count += 1
        
print(count)
