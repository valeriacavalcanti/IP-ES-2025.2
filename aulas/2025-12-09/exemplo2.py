# exibir todos os símbolos numéricos
inicio_num = ord('0')
fim_num = ord('9')
for cod_decimal in range(inicio_num, fim_num + 1):
    simbolo = chr(cod_decimal)
    print(cod_decimal, simbolo, type(simbolo))

print()

# exibir todas as letras maiúsculas
inicio_letra_mai = ord('A')
fim_letra_mai = ord('Z')
for cod_decimal in range(inicio_letra_mai, fim_letra_mai + 1):
    simbolo = chr(cod_decimal)
    print(cod_decimal, simbolo, type(simbolo))


print()

# exibir todas as letras minúsculas
inicio_letra_min = ord('a')
fim_letra_min = ord('z')
for cod_decimal in range(inicio_letra_min, fim_letra_min + 1):
    simbolo = chr(cod_decimal)
    print(cod_decimal, simbolo, type(simbolo))
