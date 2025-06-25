print('-=' * 10, 'EX 01', '-=' * 10)
n = int(input('Digite um número inteiro: '))
while n >= 0:
    if n == 5:
        print('O número É 5')
    elif n < 5:
        print('O número é MENOR que 5')
    else:
        print('O número é MAIOR que 5')
    n = int(input('Digite um número inteiro (negativo para acabar): '))
print('Número negativo informado, Fim.')

print('-=' * 10, 'EX 02', '-=' * 10)
menor = 0
adulto = 0
idoso = 0
idade = int(input('Digite uma idade entre 1 e 120: '))
while 0 < idade <= 120:
    if idade <= 18:
        menor += 1
    elif 18 <= idade <= 60:
        adulto += 1
    elif idade > 60:
        idoso += 1
    idade = int(input('Digite uma idade entre 1 e 120: '))
print('''A soma das faixas etárias é: 
Menor {}
Adulto {}
Idoso {}'''.format(menor, adulto, idoso))

print('-=' * 10, 'EX 03', '-=' * 10)
n = int(input('Digite um número: '))
maior = n
while n != -100:
    n = int(input('Digite um número (-100 para acabar): '))
    if n > maior:
        maior = n
print('O maior número informado foi: {}'.format(maior))

print('-=' * 10, 'EX 04', '-=' * 10)
n = float(input('Digite um número: '))
cont = 0
soma = n
while n != 0:
    n = float(input('Digite um número (0 para acabar): '))
    cont += 1
    soma += n
if cont > 0:
    print('Foram informados {} números, e a média deles é {:.2f}'.format(cont,soma / cont))
else:
    print('Não foi digitado um número valido')

print('-=' * 10, 'EX 05', '-=' * 10)
n = int(input('Digite um número: '))
while n:
    for i in range(1, n+1):
        if i % 2 == 1:
            print(i, end=' ')
        if i % 2 == 0:
            print(i)
    break

print('-=' * 10, 'EX 06', '-=' * 10)
n = float(input('Digite um número (de 12 a 20): '))
while n < 12 or n > 20:
    n = float(input('Entrada inválida, escolha entre 12 e 20: '))
print('O número informado foi {}'.format(n))

print('-=' * 10, 'EX 07', '-=' * 10)
n = int(input('Digite um número positivo: '))
while n < 0:
    n = int(input('Digite um número POSITIVO: '))
print('Sequência de Fibonacci')
a,b = 0,1
while a <=n:
    print(a, end=' -> ')
    a, b = b, a + b
print('Fim.')

print('-=' * 10, 'EX 08', '-=' * 10)
soma = 0
n = int(input('Digite um número inteiro ímpar: '))
while n % 2 == 1:
    soma += n
    n = int(input('Digite um número inteiro par: '))
if soma > 0:
    diferenca = soma - n
    print('A diferença da soma dos números ímpares ({}) e o número par informado ({}) é = {}'.format(soma, n, diferenca))

print('-=' * 10, 'EX 09', '-=' * 10)
soma = 0
n = int(input('Digite um número inteiro: '))
while True:
    soma += n
    if soma % 7 != 0:
       n = int(input('Digite um número inteiro: '))
    else:
      break
print('A soma dos número foi: {} que é divisível por 7'.format(soma))

print('-=' * 10, 'EX 10', '-=' * 10)
tentativas = 1
n = int(input('Digite um número ímpar entre 1 e 100: '))
while n % 2 == 0:
    tentativas += 1
    n = int(input('Digite um número ímpar entre 1 e 100: '))
print('Você precisou de {} tentativas para digitar um número ímpar'.format(tentativas))
