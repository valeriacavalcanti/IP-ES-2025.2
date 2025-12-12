import funcoes

numeros = funcoes.gerar_matriz(10, 10)
#print(numeros)

funcoes.preencher_matriz(numeros, 10, 15)
print(numeros)

distintos = funcoes.valores_distintos(numeros)
print(distintos)
print(len(distintos))

#distintos.sort()

if funcoes.verificar_ordenada(distintos) == True:
    print('Ordenada')
else:
    print('Não ordenada')

    


