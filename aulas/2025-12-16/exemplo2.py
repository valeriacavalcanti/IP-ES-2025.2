arq = open('relatorio.csv', 'r')

# manipular (leitura)
for linha in arq.read().splitlines():
    registro = linha.split(';')
    print(registro[1])


arq.close()
