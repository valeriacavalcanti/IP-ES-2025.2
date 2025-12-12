# ler um texto e informar quantos símbolos numéricos estão contidos?

def e_numero(simbolo: str) -> bool:
    if simbolo >= '0' and simbolo <= '9':
        return True
    else:
        return False

def e_letra_minuscula(simbolo: str) -> bool:
    if simbolo >= 'a' and simbolo <= 'z':
        return True
    else:
        return False


def e_letra_maiuscula(simbolo: str) -> bool:
    if simbolo >= 'A' and simbolo <= 'Z':
        return True
    else:
        return False

def converte_letra_para_maiusculo(simbolo: str) -> str:
    if e_letra_minuscula(simbolo):
        codigo = ord(simbolo) - 32
        return chr(codigo)
    else:
        return simbolo


def converte_texto_para_maiusculo(texto: str) -> str:
    novo_texto = ''
    for simbolo in texto:
        novo_texto += converte_letra_para_maiusculo(simbolo)
        
    return novo_texto


##


texto = input('Texto: ')
qtd = 0
for simbolo in texto:
    if e_numero(simbolo):
        qtd += 1
print(qtd)
print(converte_texto_para_maiusculo(texto))

#simbolo = input('Símbolo: ')
#simbolo_maiusculo = converte_letra_para_maiusculo(simbolo)
#print(simbolo_maiusculo)

