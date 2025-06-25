n = int(input('Digite um número: '))
soma = 0
while n % 2 != 0:
    soma += n
    n = int(input('Digite um número: '))
dif = soma - n
print('A diferença entre a soma dos ímpares \033[31m{}\033[m e o par \033[32m{}\033[m é: \033[33m{}\033['.format(soma, n, dif))
