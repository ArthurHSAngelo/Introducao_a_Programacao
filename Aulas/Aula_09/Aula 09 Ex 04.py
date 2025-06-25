n = int(input('Digite um número inteiro (0 para acabar): '))
cont = 0
soma = 0
while n != 0:
    soma += n 
    cont += 1
    n = int(input('Digite um número inteiro (0 para acabar): '))
print('Foram digitados {} números e a média deles é {:.2f}'.format(cont, soma / cont))
