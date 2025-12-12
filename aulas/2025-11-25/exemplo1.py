import random

# declarar a matriz
matriz = []
for i in range(3):
    matriz.append([0] * 4)

# preencher com valores aleatórios
for i in range(3):
    for j in range(4):
        matriz[i][j] = random.randint(0, 100)

print('tamanho:', len(matriz))

for i in range(3):
    for j in range(4):
        #print(matriz[i][j])
        print(i, j, matriz[i][j])
    print('-')
