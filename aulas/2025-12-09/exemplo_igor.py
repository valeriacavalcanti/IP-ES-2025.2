# ler um texto e remover TODOS os espaços em branco que estão em excesso.

texto = '      o     dia    esta     lindo      '
novo_texto = ' '.join(texto.split())

print(novo_texto)
