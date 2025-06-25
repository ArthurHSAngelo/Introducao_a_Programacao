#Exercício 01
n1 = float(input('Digite um número real: '))
n2 = float(input('Digite outro número real: '))
n3 = float(input('Digite outro número real: '))
n4 = float(input('Digite outro número real: '))
m = (n1+n2+n3+n4) / 4
print('A média é igual a {}'.format(m))

#Exercício 02
dolar = float(input('Digite um valor em dólar americano: '))
real = dolar * 5.10
print('O valor da conversão é R$ {}'.format(real))

#Exercício 03
valor = float(input('Qual é o valor da pizza? '))
pessoas = int(input('Quantas pessoas vão pagar ela? '))
print('O valor que cada um pagará é R$', valor / pessoas)

#Exercício 04
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um  número inteiro: '))
print('A soma desses números inteiros é igual a', n1+n2+n3)

#Exercício 05
nome = str(input('Qual é o seu nome? '))
endereço = str(input('Qual é o seu endereço? '))
bairro = str(input('Qual é o seu bairro? '))
cidade = str(input('Qual é a sua cidade? '))
idade = int(input('Quantos anos você tem? '))
print('Muito prazer {}! Fiquei sabendo que você tem {} anos, e mora no endereço {}, bairro {}, situado na cidade {}. Parabéns!!'.format(nome,idade,endereço,bairro,cidade))
