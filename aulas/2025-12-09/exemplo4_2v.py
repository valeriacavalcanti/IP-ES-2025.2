# ler um símbolo e informar seu tipo (número, letra maiúscula, letra minúscula
# caractere especial).

simbolo = input('Símbolo: ')
codigo = ord(simbolo)

if codigo >= ord('0') and codigo <= ord('9'):
    print('símbolo numérico')
elif codigo >= ord('A') and codigo <= ord('Z'):
    print('Letra maiúscula')
elif codigo >= ord('a') and codigo <= ord('z'):
    print('Letra minúscula')
else:
    print('Caractere especial')
