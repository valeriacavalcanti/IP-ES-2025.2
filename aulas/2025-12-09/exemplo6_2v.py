# ler um texto e remover TODOS os espaços em branco que estão em excesso.

texto = '      o     dia    esta     lindo      '
novo_texto = texto

while novo_texto.find('  ') > -1:
    novo_texto = novo_texto.replace('  ', ' ')

print(novo_texto)
