# gerar a matriz
def gerar_matriz(qt_linhas: int, qt_colunas:int, valor = 0) -> list:
    matriz = []
    for i in range(qt_linhas):
        matriz.append([valor] * qt_colunas)
    return matriz


# preencher a matriz com valores aleatórios
def preencher_matriz(matriz: list, menor = 1, maior = 100):
    import random
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(menor, maior)


# identificar os distintos valores na matriz
def valores_distintos(matriz: list) -> list:
    memoria = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] not in memoria:
                memoria.append(matriz[i][j])
    return memoria


# verificar se o vetor está ordenado
def verificar_ordenada(vetor: list) -> bool:
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            return False
    return True
