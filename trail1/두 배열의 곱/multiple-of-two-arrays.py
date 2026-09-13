mata = [[0 for _ in range(3)] for _ in range(3)]
matb = [[0 for _ in range(3)] for _ in range(3)]
matc = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    lista = list(map(int,input().split()))
    for j in range(3):
        mata[i][j] = int(lista[j])
        
blank = input()

for i in range(3):
    listb = list(map(int,input().split()))
    for j in range(3):
        matb[i][j] = int(listb[j])
        matc[i][j] = mata[i][j] * matb[i][j]

for row in matc:
    for element in row:
        print(element, end = ' ')
    print( )
        

