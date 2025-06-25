while True:
    n = int(input('Digite um número: '))
    if n < 0:
        print('Número negado.')
        break
    else:
        dobro = n * 2
        print('O dobro de {} é {} '.format(n, dobro))
