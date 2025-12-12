# ler um texto e uma palavra. Exibir quantas vezes a palavra aparece no texto.

texto = input('Informe o texto: ')
tokens = texto.split()
palavra = input('Informe a palavra:')

qtd = 0

for token in tokens:
    if token == palavra:
        qtd = qtd + 1

print(qtd)
