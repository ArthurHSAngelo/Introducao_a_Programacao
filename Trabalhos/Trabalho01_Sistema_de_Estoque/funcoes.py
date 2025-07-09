lista_de_produtos = []

# 1 - Cadastrar produto
def cadastrar_produtos(lista_de_produtos):
    print('\n----- CADASTRO -----')
    while True:
        try:
            codigo = int(input('\nDigite o código do produto: '))
            for x in lista_de_produtos:
                if x['codigo'] == codigo:
                    print('\033[1;31mO código que você inseriu já está cadastrado em outro produto.\n\033[m')
                    return
            nome = input('Digite o nome do produto: ').strip()
            preco = float(input('Digite o preço do produto (com os centavos): R$'))
            quantidade = int(input('Qual é a quantidade inicial em estoque que esse produto deve ter: '))
            produto ={
            'codigo': codigo,
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
            }
            lista_de_produtos.append(produto)
            print('\n\033[1;32mO cadastro foi realizado com sucesso!\033[m\n')
            break
        except:
            print('''\n\033[1;31mO cadastro não foi realizado com sucesso, tente novamente.\033[m
\033[1;33mPossíveis erros:
-> Código escrito com alguma letra ou caractere especial. 
-> Preço inválido, ou incorreto, deve ser escrito com casas decimais (os centavos)
-> Quantidade escrita com alguma letra ou caractere especial.\n\033[m
\033[1;32mVamos tentar novamente!\033[m''')


# 2 - Listar os produtos
def listar_produtos(lista_de_produtos):
    print('\n----- LISTA DE PRODUTOS CADASTRADOS -----')
    if not lista_de_produtos:
        print('\nNenhum produto foi cadastrado!\n')
        return
    total_quantidade_itens = 0
    valor_total_estoque = 0.00
    print(f'{'Código':<8} {'Nome':<20} {'Preço'}   {'Quantidade':<5}')
    for x in lista_de_produtos:
        print(f'{x['codigo']:<8} {x['nome']:<20} R${x['preco']:.2f} {x['quantidade']:<5} \n')
        total_quantidade_itens += x['quantidade']
        valor_total_estoque += x['preco'] * x['quantidade']
    print('\n----- Relatórios do Estoque -----')
    print(f'Total de itens no estoque: {total_quantidade_itens}')
    print(f'Valor total do estoque: R${valor_total_estoque:.2f} \n')


# 3 - Consultar produto por código
def consultar_produto(lista_de_produtos):
    print('\n----- CONSULTA DE PRODUTO POR CÓDIGO -----')   
    while True:
        try:
            codigo_inserido = int(input('\nDigite o código do produto que quer buscar: '))
            produto_encontrado = None
            for produto_procurado in lista_de_produtos:
                if produto_procurado['codigo'] == codigo_inserido:
                    print('\nProduto encontrado!\n')
                    produto_encontrado = produto_procurado

            if produto_encontrado is not None:
                print(f'{'Código':<10} {'Nome':<20} {'Preço'}   {'Quantidade':<5}')
                print(f'{produto_encontrado['codigo']:<10} {produto_encontrado['nome']:<20} R${produto_encontrado['preco']:.2f} {produto_encontrado['quantidade']:<5}')
                break
            else:
                print('\nNão existe produto com esse código, tente novamente!\n')
        except:
            print('\nAlgo deu errado, tente novamente!\n')


# 4 - Alterar produto
def alterar_produto(lista_de_produtos):
    print('\n----- ALTERAR PRODUTO -----')
    while True:
        try:
            codigo_inserido = int(input('\nDigite o código do produto que deseja alterar:\n'))
            produto_encontrado = None
            for produto_procurado in lista_de_produtos:
                if produto_procurado['codigo'] == codigo_inserido: 
                    print('\nProduto encontrado!\n')
                    produto_encontrado = produto_procurado
                    print('\n---Menu de Alterações---\n')
                    print('''1 - Nome do Produto
2 - Preço do Produto
3 - Quantidade do Produto''' )
                    x = int(input('\nO que você deseja alterar?\n'))
                    match x:
                        case 1:
                            nome_novo = str(input('\nQual será o novo nome do produto?:\n'))
                            produto_procurado['nome'] = nome_novo
                            print('\nO nome do produto foi alterado!\n')
                            return
                        case 2:
                            preco_novo = float(input('\nQual será o novo preço do produto?:\nR$'))
                            produto_procurado['preco'] = preco_novo
                            print('\nO preço do produto foi alterado!\n')
                            return
                        case 3:
                            qtde_nova = int(input('\nQual será a nova quantidade do produto?:\n'))
                            produto_procurado['quantidade'] = qtde_nova
                            print('\nA quantidade do produto foi alterada!\n')
                            return
                        case _:
                            print('Opção invalida inserida, tente novamente!')
                else:
                    print('\nNão há nenhum produto com esse código, tente novamente!\n')
        except:
            print('\nAlgo deu errado, tente novamente!\n')


# 5 - Remover produto
def remover_produto(lista_de_produtos):
    while True:
        try:
            codigo_procurado = int(input('\nDigite o código do produto que você deseja remover:\n'))
            produto_encontrado = False
            for produto_procurado in lista_de_produtos:
                if produto_procurado['codigo'] == codigo_procurado: 
                    print('\nProduto encontrado!\n')
                    produto_encontrado = produto_procurado
                    break
            if produto_encontrado:
                print(f'\nProduto encontrado: {produto_encontrado['nome']}, Preço: {produto_encontrado['preco']:.2f}\n')
                confirmação = input('Você realmente deseja remover esse produto? (S para sim, N para não):\n').upper()
                if confirmação == 'S':
                    lista_de_produtos.remove(produto_encontrado)
                    print("\nProduto removido com sucesso!\n")
                    return
                elif confirmação == 'N':
                    print('\nOperação de remoção cancelada.\n')
                    return
                else:
                    print('\nOpção invalida inserida.\n')
            else:
                print('\nProduto com este código não foi encontrado.\n')

        except:
            print('\nPor favor, digite um código válido.\n')

