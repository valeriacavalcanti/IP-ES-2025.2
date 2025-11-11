soma = 0

qtd = int(input('Quantidade: '))

for i in range(qtd):
    while True:
        n = int(input(f'Nota {i+1}: '))
        if n >= 0 and n <= 100:
            break
    soma = soma + n

media = soma / qtd
        
