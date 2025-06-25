n = float(input('Digite um número entre 12 e 20: '))
while n:
    if 12 >= n >= 20:
        print('Número inválido')
        n = float(input('Digite um número entre 12 e 20: '))
    else:
        print(n)
        break