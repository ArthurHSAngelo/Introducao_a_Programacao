print('-=' * 6, 'LISTA DE CONTATOS', '-=' * 6)
lista_de_contatos = {}
while True:
    print('''Menu:
1. Adicionar contato
2. Remover contato
3. Alterar contato
4. Exibir todos os contatos
5. Sair''')

    opcao = int(input('Informe a opção desejada: \n'))
    match opcao:
        case 1:
            nome = input('Qual o nome do contato que deseja adicionar? \n').title().strip()
            if nome == '':
                print('Nome não pode ficar vazio!\n')
                continue
            numero = input('Qual o número de telefone? \n').strip()
            if numero == '':
                print('O número não pode ficar vazio.\n')
                continue

            lista_de_contatos[nome] = numero
        case 2:
            excluir = input('Qual o nome do contato que você deseja remover? \n').title().strip()
            if excluir == '':
                print('Você precisa digitar algo para remover.\n')
                continue

            if excluir in lista_de_contatos:
                del lista_de_contatos[excluir]
                print(f'Você removeu o contato {excluir} da sua lista de contatos com sucesso!\n')
            else:
                print(f'O contato {excluir} não existe na sua lista de contatos.\n')
        case 3:
            contato_antigo = input('Qual contato você deseja alterar? ').title()
            if contato_antigo == '':
                print('Você precisa informar algum nome.\n')
                continue

            elif contato_antigo in lista_de_contatos:
                alterar = input(f'O que você deseja alterar no contato {contato_antigo} (nome) ou (telefone)? \n').strip().lower()
                if alterar == 'nome':
                    novo_nome = input('Digite o NOVO NOME para o contato: ').title().strip()
                    if novo_nome == '':
                        print('O novo nome não pode estar em branco.\n')
                        continue

                    n = lista_de_contatos[contato_antigo]
                    lista_de_contatos[novo_nome] = n
                    del lista_de_contatos[contato_antigo]
                    print('Você alterou o telefone do contato com sucesso.\n')
                
                elif alterar == 'telefone':
                    novo_telefone = input(f'Digite o NOVO NUMERO de telefone para o {contato_antigo}? ').strip()
                    if novo_telefone == '':
                        print('O novo telefone não pode estar em branco.\n')
                        continue

                    lista_de_contatos[contato_antigo] = novo_telefone
                    print('Você alterou o telefone do contato com sucesso.\n')

                else:
                    print('\nOpção inválida. Digite se você quer alterar o "nome" ou o "telefone".\n')
            else:
                print(f'\nO nome {contato_antigo} não está na sua lista de contatos.')
            print('-=' * 10)

        case 4:
            print('TODOS OS CONTATOS \n')
            if not lista_de_contatos:
                print('Você não tem nenhum contato em sua lista de contatos.')
            else:
                for x, y in lista_de_contatos.items():
                    print(x,': ',y, sep='')
            print('-=' * 10)
        case 5:
            print('Finalizando o programa...')
            break
        case _:
            print('Opção inválida. Escolha um número de 1 a 5 \n')
                