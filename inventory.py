listaProdutos = [] 

def cadastrarProduto(codigo):
    print('Você selecionou a opção de Cadastrar Produto')
    print('Código do Produto {}'.format(codigo))
    nome = input('Por favor entre com o NOME do Produto: ')
    fabricante = input('Por favor entre com o FABRICANTE do Produto: ')
    valor = float(input('Por favor entre com o VALOR(R$) do Produto: '))
    dicionarioProduto = {'codigo':codigo,
                         'nome':nome,
                         'fabricante':fabricante,
                         'valor':valor} 
    listaProdutos.append(dicionarioProduto.copy()) 

def consultarProduto(): 
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
                for produto in listaProdutos: 
                    for key, value in produto.items():
                        print('{} : {} '.format(key, value))

            elif opConsultar == 2:
                conCodigo = int(input('Digite o CODIGO do Produto: '))
                for produto in listaProdutos:
                    if (produto ['codigo'] == conCodigo):
                        for key, value in produto.items():
                            print('{} : {} '.format(key, value))


            elif opConsultar == 3:
                conFabricante = input('Digite o FABRICANTE do Produto: ')
                for produto in listaProdutos: 
                    if (produto['fabricante'] == conFabricante): 
                        for key, value in produto.items():
                            print('{} : {} '.format(key, value))

            elif opConsultar == 4:
                break
            else:
                print('Opção inválida. Tente novamente')
                              continue


        except ValueError:  
            print('Digite valores inteiros de 1 até 4.')


def removerProduto(): 
    print('Bem vindo ao menu de remoção')
    conCodigo = int(input('Digite o CODIGO do Produto que deseja remover: '))
    for produto in listaProdutos: 
        if (produto['codigo'] == conCodigo): 
            listaProdutos.remove(produto) 




print('Bem-vindo ao Controle de Estoque da Mercearia do Rafael Lima Etiene de Souza')
codigoProd = 0 
while True:
    try:
        opcao = int(input('Escolha a opção desejada: \n'
                          '1 - Cadastrar Produto \n'
                          '2 - Consultar Produto \n'
                          '3 - Remover Produto \n'
                          '4 - Sair'))
        if opcao == 1:
            codigoProd += 1 
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
