# ler um texto e remover TODOS os espaços em branco que estão em excesso.

texto = '      o     dia    esta     lindo      '
lista = texto.split()

novo_texto = ''
for token in lista:
    novo_texto += token + ' '

novo_texto = novo_texto.strip()

print(f'[{novo_texto}]')
