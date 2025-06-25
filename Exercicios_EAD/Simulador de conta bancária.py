saldo = 1000 # saldo inicial
opcao = 0
usuario = str(input('Digite o seu nome: \n'))

print('=-=-=-= SIMULADOR DE CONTA BANCÁRIA =-=-=-=')
print('''Prazer Sr(a) {} você acessou a sua conta bancária
Opções
1 = Ver saldo
2 = Depositar 
3 = Sacar
4 = Sair da conta'''.format(usuario))
while opcao != 4:
    opcao = int(input('O que deseja fazer? \n'))
    match opcao:
        case 1:
            print('Seu saldo atual é {} \n'.format(saldo))
        case 2:
            deposito= int(input('Quanto você quer depositar? \n'))
            saldo = saldo + deposito
            print('Você depositou R${} e agora seu saldo é de R${} \n'.format(deposito, saldo))
        case 3:
            saque = int(input('Quanto você quer sacar? \n'))
            if saque > saldo:
                print('Você não pode sacar mais do que o seu saldo')
            else:
                saldo = saldo - saque
                print('Você sacou R${} e agora seu saldo é de R${} \n'.format(saque, saldo))
        case 4:
            print('Você saiu da conta ')
            break
        case _:
            print('Opção inválida \n')
