import random

numeros = [0] * 30
memoria = []

# gerar os valores aleatórios
for i in range(len(numeros)):
    numeros[i] = random.randint(1, 1000)

# exibir
print(numeros)

# ler um número do usuários
numero_usuario = int(input('Digite um número: '))

# verificar se o número digitado está contido no vetor
if numero_usuario in numeros:
    print('existe')
else:
    print('nao existe')

existe = False

# calcular a frequencia dos elementos contidos no vetor
for i in range(len(numeros)):
    if numeros[i] not in memoria:
        qtd = 1
        for j in range(len(numeros)):
            if i != j and numeros[i] == numeros[j]:
                qtd += 1
        if qtd > 1:
            existe = True
        print(numeros[i], qtd)
        memoria.append(numeros[i])

if existe:
    print('tem repeticao')
else:
    print('nao tem repeticao')

        
