listaProdutos = [] #Lista onde os cadastros são armazenados

def cadastrarProduto(codigo): #Função do cadastro de produtos
    print('Você selecionou a opção de Cadastrar Produto')
    print('Código do Produto {}'.format(codigo))
    nome = input('Por favor entre com o NOME do Produto: ')
    fabricante = input('Por favor entre com o FABRICANTE do Produto: ')
    valor = float(input('Por favor entre com o VALOR(R$) do Produto: '))
    dicionarioProduto = {'codigo':codigo,
                         'nome':nome,
                         'fabricante':fabricante,
                         'valor':valor} #Dicionário que armazena as informações do produto
    listaProdutos.append(dicionarioProduto.copy()) #Inserindo uma cópia do dicionário na lista de produtos

def consultarProduto(): #Função de consulta dos produtos
    print('Você selecionou a opção de Consultar Produto')
    while True:
        try:
            opConsultar = int(input('Escolha a opção desejada: \n'
                              '1 - Consultar Todos os Produtos \n'
                              '2 - Consultar Produtos por Código \n'
                              '3 - Consultar Produtos por Fabricante \n'
                              '4 - Retornar'))
            if opConsultar == 1:
                print
                for produto in listaProdutos: #Laço de repetição para varrer os produtos dentro da lista
                    for key, value in produto.items():#Laço de repetição para apresentar todos os produtos
                        print('{} : {} '.format(key, value))

            elif opConsultar == 2:
                conCodigo = int(input('Digite o CODIGO do Produto: '))
                for produto in listaProdutos: #Laço de repetição para varrer os produtos dentro da lista
                    if (produto ['codigo'] == conCodigo): #If para verificar o código desejado dentro dos dicionários
                        for key, value in produto.items():
                            print('{} : {} '.format(key, value))


            elif opConsultar == 3:
                conFabricante = input('Digite o FABRICANTE do Produto: ')
                for produto in listaProdutos: #Laço de repetição para varrer os produtos dentro da lista
                    if (produto['fabricante'] == conFabricante): #If para verificar o fabricante desejado dentro dos dicionários
                        for key, value in produto.items():
                            print('{} : {} '.format(key, value))

            elif opConsultar == 4:
                break
            else:
                print('Opção inválida. Tente novamente')
                              continue


        except ValueError:  #Tratando erros
            print('Digite valores inteiros de 1 até 4.')


def removerProduto(): #Função de remoção de produtos
    print('Bem vindo ao menu de remoção')
    conCodigo = int(input('Digite o CODIGO do Produto que deseja remover: '))
    for produto in listaProdutos: #Laço de repetição para varrer os produtos dentro da lista
        if (produto['codigo'] == conCodigo): #If para verificar o código desejado dentro dos dicionários
            listaProdutos.remove(produto) #Método para remover o produto


# Programa Principal

print('Bem-vindo ao Controle de Estoque da Mercearia do Rafael Lima Etiene de Souza')
codigoProd = 0 #Contador
while True:
    try:
        opcao = int(input('Escolha a opção desejada: \n'
                          '1 - Cadastrar Produto \n'
                          '2 - Consultar Produto \n'
                          '3 - Remover Produto \n'
                          '4 - Sair'))
        if opcao == 1:
            codigoProd += 1 #Equação que gera o código de cada produto
            cadastrarProduto(codigoProd)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            break
        else:
            print('Opção inválida. Tente novamente')
            continue
    except ValueError:
        print('Digite valores inteiros de 1 até 4.')
        continue
