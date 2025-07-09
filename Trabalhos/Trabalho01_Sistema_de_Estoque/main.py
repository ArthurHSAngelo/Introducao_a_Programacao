import funcoes
inventário = []

while True:
    print('''-=-=- Sistema de Estoque -=-=-
          
    1 - Cadastrar produto
    2 - Listar os produtos
    3 - Consultar produto por código
    4 - Alterar produto
    5 - Remover produto
    6 - Finalizar 
          ''')
    try:
        opcao = int(input('O que deseja fazer? '))
        match opcao:
            case 1:
                funcoes.cadastrar_produtos(inventário)

            case 2:
                funcoes.listar_produtos(inventário)

            case 3:
                funcoes.consultar_produto(inventário)

            case 4:
                funcoes.alterar_produto(inventário)

            case 5:
                funcoes.remover_produto(inventário)

            case 6:
                saida = input('Você realmente deseja sair? (Digite [S] para sim e [N] para não.): ').strip().upper()
                if saida == 'S':
                    print('Saindo do sistema...')
                    break
                elif saida == 'N':
                    print('Saída cancelada! Vamos voltar pro sistema.')
                else:
                    print('Você não escreveu corretamente.')

            case _:
                print('Opção inválida, tente novamente.')
    
    except:
        print('Escolha uma opção de 1 a 6 por gentileza.')