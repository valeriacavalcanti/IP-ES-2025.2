TAMANHO = 4
soma = 0
numeros = [0,0,0,0]
qtd = 0

for i in range(TAMANHO):
    numeros[i] = int(input('Número: '))
    soma = soma + numeros[i]
    #print(numeros)

media = soma / TAMANHO

for i in range(len(numeros)):
    if numeros[i] > media:
        qtd = qtd + 1

print(f'{soma=}')
print(f'{media=}')
print(f'{qtd=}')

# exibir os valores acima da media
for i in range(len(numeros)):
    if numeros[i] > media:
        print(i, numeros[i])

        
