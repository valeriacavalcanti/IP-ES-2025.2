# ler um símbolo e informar seu tipo (número, letra maiúscula, letra minúscula
# caractere especial).

simbolo = input('Símbolo: ')

if simbolo >= '0' and simbolo <= '9':
    print('símbolo numérico')
elif simbolo >= 'A' and simbolo <= 'Z':
    print('Letra maiúscula')
elif simbolo >= 'a' and simbolo <= 'z':
    print('Letra minúscula')
else:
    print('Caractere especial')
