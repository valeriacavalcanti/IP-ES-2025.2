arq = open('dados.txt', 'w')

# manipular
for i in range(2):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    endereco = input('Endereço: ')
    
    arq.write(f'{nome},{idade},{endereco}\n')

arq.close()
