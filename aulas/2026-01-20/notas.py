def converter_int(matriz: list):
    matriz[0] = matriz[0].split(',')
    for i in range(1, len(matriz)):
        matriz[i] = matriz[i].split(',')
        for j in range(2, 8):
            matriz[i][j] = int(matriz[i][j])

def media_estudante(lista: list) -> int:
    return (lista[2] + lista[4] + lista[6]) // 3

def faltas_estudante(lista: list) -> int:
    return lista[3] + lista[5] + lista[7]

def situacao_estudante(media: int, faltas: int) -> bool:
    if media >= 50 and faltas <= 150:
        return True
    else:
        return False

    #return media >= 70 and faltas <= 90


def qtd_aprovados(matriz: list) -> int:
    qtd = 0
    for i in range(1, len(matriz)):
        media = media_estudante(matriz[i])
        faltas = faltas_estudante(matriz[i])
        if situacao_estudante(media, faltas) == True:
            qtd += 1
            print(matriz[i][0])
    return qtd


def media_nota(matriz: list, avaliacao: int) -> int:
    if avaliacao == 1:
        coluna = 2
    elif avaliacao == 2:
        coluna = 4
    else:
        coluna = 6

    soma = 0
    for i in range(1, len(matriz)):
        soma += matriz[i][coluna]

    return soma // 100


def nomes_identificados(matriz: list) -> list:
    memoria = []
    for i in range(1, len(matriz)):
        nome = matriz[i][0].split()
        primeiro_nome = nome[0]
        if primeiro_nome not in memoria:
            memoria.append(primeiro_nome)
    return memoria


def frequencia_nomes_identificados(matriz: list) -> list:
    memoria = []
    frequencia = []
    lista = []
    
    for i in range(1, len(matriz)):
        nome = matriz[i][0].split()
        primeiro_nome = nome[0]
        if primeiro_nome not in memoria:
            memoria.append(primeiro_nome)
            frequencia.append(1)
        else:
            indice = memoria.index(primeiro_nome)
            frequencia[indice] += 1

    for i in range(len(memoria)):
        lista.append((memoria[i], frequencia[i]))
        
    return lista


# main
arq = open('notas.csv', 'r')
dados = arq.read().splitlines()
arq.close()

#dados = dados[1:]
converter_int(dados)

#print(qtd_aprovados(dados))
#print(media_nota(dados, 1), media_nota(dados, 2), media_nota(dados, 3))

#print(nomes_identificados(dados))
print(frequencia_nomes_identificados(dados))
