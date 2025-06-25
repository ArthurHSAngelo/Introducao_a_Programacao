#1. Entrar com números e imprimir o triplo do seu valor. O algoritmo não acaba enquanto o número −999 não for informado.
print('EX 01')
numeros = []
while True:
    numero = int(input('Digite um número (-999 para sair): '))
    if numero == -999:
        print('Encerrando o programa')
        break
    else:
        print('O triplo de {} é {}'.format(numero, numero *3))
print('-=' * 30)

#2. Imprimir todos os números de 1 até 100.
print('EX 02')
for i in range(1,101,1):
    print(i, end=' ')
print('-=' * 30)

#3. Imprimir todos os números de 100 até 1.
print('EX 03')
for i in range(100, 0, -1):
    print(i, end=' ')
print('-=' * 30)

#4. O programa deve receber números enquanto forem positivos e imprimir quantos números foram digitados (extra).
print('EX 04')
c = 0
while True:
    n = int(input('Digite um número, negativo encerra o programa: '))
    if n < 0:
        break
    c += 1
print('Números positivos digitados: {}'.format(c))
print('-=' * 30)

#5. Enquanto digitar números positivos some os números, quando digitar um número negativo, imprimir a média dos números positivos digitados (extra).
print('EX 05')
s = 0
c = 0
n = float(input('Digite um número positivo (número negativo para realizar a média): '))
while n > 0:
    c += 1
    s += n
    n = float(input('Digite um número positivo (número negativo para realizar a média): '))

if c > 0:
    m = s / c
    print('A média dos números é {}'.format(m))
else:
    print('Nenhum valor positivo foi informado')
print('-=' * 30)

#6. Criar um algoritmo que imprima os números pares no intervalo de 1 a 600.
print('EX06')
for i in range(1, 601, 2):
    print(i, end=' ')
print('-=' * 30)

#7. O programa deve ler vários números e informar quantos números entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo deverá cessar a sua execução.
print('EX 07')
c = 0
while True:
    n = float(input('Digite um número (0 para encerrar): '))
    if 100 <= n <= 200:
        c += 1
    elif n == 0:
        break
print('Foram digitados {} números de 100 a 200'.format(c))
print('-=' * 30)

#8. Entrar com profissão de várias pessoas e imprimir quantos são dentistas (considerar DENTISTA, dentista, Dentista). Quando o usuário digitar FIM o algoritmo deverá cessar a sua execução.
print('EX 08')
c = 0
while True:
    profissao = str(input('Digite a sua profissão: ')).lower()
    if profissao == 'dentista':
        c += 1
        print('Dessas profissões, {} são dentistas (escreva "fim" para encerrar)'.format(c))
    elif profissao == 'fim':
        break
print('Total de dentistas é {} dentistas!'.format(c))
print('-=' * 30)

#9. Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10 e cresce 3 centímetros por ano. Construir um algoritmo que calcule e imprima quantos anos serão necessários para que Juca seja maior que Chico. (extra)
print('EX 09')
chico = 1.5
juca = 1.1
ano = 0
while juca <= chico:
    chico += 0.02
    juca += 0.03
    ano += 1
print('Chico tem {:.2f}m e Juca tem {:.2f}m, demorou {} anos para isso acontecer.'.format(chico, juca, ano))
print('-=' * 30)

#10. Entrar com 10 números e imprimir o quadrado e a metade de cada número
print('EX 10')
for i in range(10):
    num = float(input('Digite o {} número: '.format(i+1)))
    quadrado = num ** 2
    metade = num / 2
    print('{:.1f} ao quadrado é {:.1f}'.format(num, quadrado))
    print('metade de {:.1f} é {:.1f}'.format(num, metade))
print('-=' * 30)

#11. Criar um algoritmo que imprima uma tabela de conversão de polegadas para centímetros. Deseja-se que na tabela conste valores desde a 1 polegada (2,54 cm) até a 20ª polegada (Cada polegada equivale a 2.54cm).
print('EX 11')
pol = 2.54
print('Tabela de conversão de polegadas para centímetros')
for i in range(1,21):
    centimetros = i * pol
    print('{} polegadas são {:.2f} centímetros.'.format(i, centimetros))
print('-=' * 30)

#12. Criar um algoritmo que imprima a soma dos números pares entre 25 a 200.
print('EX 12')
soma = 0
for i in range(26, 201, 2):
    soma += i
print('A soma dos pares de 25 a 200 é {}'.format(soma))
print('-=' * 30)

#13. Criar um algoritmo que deixe entrar com 10 números positivos e imprima raiz quadrada de cada número. Para cada entrada de dados deverá haver um trecho de proteção para que um número negativo não seja aceito.
print('EX 13')
from math import sqrt
for i in range(1, 11):
    n = float(input('Digite o {}° número: '.format(i)))
    if n < 0:
        print('Número inválido')
    else:
        raiz = sqrt(n)
        print('A raiz de {} é {}'.format(n, raiz))
print('-=' * 30)

#14. Criar um algoritmo que leia uma número (num) e imprima a soma dos números múltiplos de 5 no intervalo entre 1 e num. Suponha que num será maior que zero.
print('EX 14')
num = int(input('Digite um número: '))
soma = 0
if num > 0:
    for i in range(1, num+1):
        if i % 5 == 0:
            soma += i
    print('A soma é dos números múltiplos de 5, de 1 a {} é {}'.format(num, soma))
else:
    print('Número incorreto')
print('-=' * 30)
