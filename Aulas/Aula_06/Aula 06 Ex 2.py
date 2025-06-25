n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

c = input(('Escolha uma opção, sendo "1" para ADIÇÃO, e "2" para SUBTRAÇÃO: '))

if c == '1':
    print('A adição é : {:.2f}'.format(n1+n2))
elif c == '2':
    print('A subtração é: {:.2f}'.format(n1-n2))
else: 
    print('Código inválido')
