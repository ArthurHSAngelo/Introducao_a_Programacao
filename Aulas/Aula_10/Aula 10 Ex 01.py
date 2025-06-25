n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print(''' =-= Menu de Operações =-=
1 - Soma
2 - Subtração
3 - Multiplicar
4 - Dividir''')

opcao = int(input('Escolha uma operação (1 a 4): '))

match opcao:
    case 1:
        print('A soma de {} e {} é {:.2f}'.format(n1, n2, n1 + n2))
    case 2:
        print('A subtração de {} e {} é {:.2f}'.format(n1, n2, n1 - n2))
    case 3:
        print('A multiplicação de {} e {} é {:.2f}'.format(n1, n2, n1 * n2))
    case 4:
        print('A divisão de {} e {} é {:.2f}'.format(n1, n2, n1 / n2))
    case _:
        print('Opção inválida')
