# ler um símbolo e informar seu tipo (número, letra maiúscula, letra minúscula
# caractere especial).

simbolo = input('Símbolo: ')
codigo = ord(simbolo)

if codigo >= 48 and codigo <= 57:
    print('símbolo numérico')
elif codigo >= 65 and codigo <= 90:
    print('Letra maiúscula')
elif codigo >= 97 and codigo <= 122:
    print('Letra minúscula')
else:
    print('Caractere especial')
