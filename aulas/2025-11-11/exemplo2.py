
for i in range(4):
    soma = 0
    qtd = 0

    num = int(input('Número: '))

    for j in range(1, num + 1):
        if num % j == 0:
            print(j)
            soma = soma + j
            # qtd = qtd + 1
            qtd += 1

    print(qtd, soma, num)
