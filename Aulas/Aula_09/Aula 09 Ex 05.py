soma = 0
while True:
    n = int(input('Digite um número: '))
    soma += n
    
    if soma % 7 == 0:
        print('{} é divisivel por 7'.format(soma))
