from math import inf
n = int(input('Digite um número inteiro: '))
maior = -inf
while n != -100:
    n = int(input('Digite um número inteiro: '))
    if n > maior:
        maior = n
print('O maior número entre todos os informados é {}'.format(maior))