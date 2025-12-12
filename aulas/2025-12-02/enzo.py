##  criação da matriz
import random

matriz = [0]*6

for i in range(6):
    matriz[i] = [0]*6


qnt_bombas = int(input())

for i in range(qnt_bombas):
    l_bomba = random.randint(0,5)
    c_bomba = random.randint(0,5)
    matriz[l_bomba][c_bomba] = 'B'

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == 'B':
            for dl in range(-1,2):
                for dc in range(-1,2):
                    adj_linha = i + dl
                    adj_coluna = j + dc
                    if 0<= adj_linha and adj_linha < len(matriz) and  0<= adj_coluna and adj_coluna < len(matriz[0]):
                        if matriz[adj_linha][adj_coluna] == 'B':
                            continue
                        else:
                            matriz[adj_linha][adj_coluna] += 1


alvo = input().split()
l_alvo = int(alvo[0])
c_alvo = int(alvo[1])

if matriz[l_alvo][c_alvo] == 0:
    print('X')
else:
    print(matriz[l_alvo][c_alvo])
    












                        
                
    
    
