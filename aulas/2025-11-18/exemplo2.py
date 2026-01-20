numeros = []

num = int(input('Número: '))

while (num > 0):
    numeros.append(num)
    num = int(input('Número: '))

print(numeros)

# exibir os números na ordem que foram digitados
for i in range(len(numeros)):
    print(i, numeros[i])

print('Valores digitados na ordem inversa')
# exibir os números na ordem INVERSA da leitura
for i in range(len(numeros) - 1, -1, -1):
    print(i, numeros[i])
