def carregar_estoque() -> list:
    estoque = []
    with open('estoque.csv', 'r') as arq:
        conteudo = arq.read().splitlines()

    for linha in conteudo[1:]:
        dados = linha.split(',')
        produto = {}
        produto['descricao'] = dados[0]
        produto['valor'] = float(dados[1])
        produto['quantidade'] = int(dados[2])
        estoque.append(produto)

    return estoque        

def exportar_estoque(lista: list):
    with open('estoque.csv', 'w') as arq:
        arq.write('descricao,valor,quantidade\n')
        for produto in lista:
            arq.write(f"{produto['descricao']},{produto['valor']},{produto['quantidade']}\n")


def menu():
    print('1 - adicionar')
    print('2 - listar')
    print('3 - Pesquisar')
    print('4 - salvar')
    print('s - sair')


def exibir_produtos(lista:list):
    print(f"{'descricao':20} {'valor':6} {'quantidade':4}")
    for i in range(len(lista)):
        produto = lista[i]
        print(f"{produto['descricao']:20} {produto['valor']:6} {produto['quantidade']:4}")


def pesquisar(lista:list, descricao: str) -> dict:
    for produto in lista:
        if produto['descricao'] == descricao:
            return produto
    return None


# main

produtos = carregar_estoque()

while True:
    menu()
    opcao = input('Informe sua opcao: ')
    
    if opcao == '1':
        print('NOVO PRODUTO')
        produto = {}
        produto['descricao'] = input('Descricao: ')
        produto['valor'] = float(input('Valor: '))
        produto['quantidade'] = int(input('Quantidade: '))
        produtos.append(produto)
        print('adicionado com sucesso')
        
    elif opcao == '2':
        print('PRODUTOS CADASTRADOS')
        exibir_produtos(produtos)
        
    elif opcao == '3':
        print('PESQUISAR PRODUTO')  
        descricao = input('Descricao: ')
        produto = pesquisar(produtos, descricao)
        if produto != None:
            print(produto['descricao'], produto['valor'], produto['quantidade'])
        else:
            print('Produto nao encontrado')

    elif opcao == '4':
        exportar_estoque(produtos)
        print('Produtos exportados com sucesso')
        
    elif opcao == 's':
        break
    else:
        print('Opcao invalida')
