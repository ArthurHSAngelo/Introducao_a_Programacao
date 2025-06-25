#1. Operações
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
adi = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
print(' A adição é {}, a subtração é {}, a multiplicação é {} e a divisão é {:.2f}'.format(adi,sub,mul,div))

#2. Conversor de Temperatura
c = float(input('Digite quantos graus Celsius: '))
f = (c * 1.8) + 32
print('Convertendo para Fahrenheit, fica em {}°'.format(f))

#3. Calculadora de IMC
p = float(input('Digite seu peso, em quilos: '))
a = float(input('Digite sua altura, em metros: '))
imc = p / (a*a)
print('Seu IMC é {:.2f}kg/m²'.format(imc))

#4.Cálculo da Média
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))
m = (n1+n2+n3+n4) / 4
print('A média é = {}'.format(m))

#5. Conversor de Moeda
d = float(input('Digite o valor em dólar: '))
r = d * 5.05
print('O resultado da conversão dólar americano para Real é {}'.format(r))

#6. Dividindo a pizza
v = float(input('Informe o valor da pizza: '))
p = int(input('Quantas pessoas irão pagar a pizza? '))
r = v / p
print('O valor de R${} será dividido por {} pessoas, e cada uma irá pagar R${}'.format(v,p,r))

#7. Cálculo da Soma
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))
n4 = float(input('Digite o 4° número: '))
n5 = float(input('Digite o 5° número: '))
s = n1+n2+n3+n4+n5
print('A soma de todos os números informados é {}'.format(s))

#8. Calculadora
t = int(input('Digite um número inteiro: '))
print('{} x 1 ='.format(t), t * 1)
print('{} x 2 ='.format(t), t * 2)
print('{} x 3 ='.format(t), t * 3)
print('{} x 4 ='.format(t), t * 4)
print('{} x 5 ='.format(t), t * 5)
print('{} x 6 ='.format(t), t * 6)
print('{} x 7 ='.format(t), t * 7)
print('{} x 8 ='.format(t), t * 8)
print('{} x 9 ='.format(t), t * 9)
print('{} x 10 ='.format(t), t * 10)

#9. Nome e Idade
nome = input('Qual é o seu nome? ')
nas = int(input('Qual é o ano da sua data de nascimento? '))
idade = 2025 - nas
print('Olá {}, a sua idade é {} anos'.format(nome, idade))

#10. Carro e média de consumo
nome = input('Qual é o nome do carro? ')
preco = float(input('Quanto está custando o Etanol? '))
cpl = float(input('Quantos quilômetros o carro faz por litro? '))
qlitros = 650/cpl
valor = (650/cpl) * preco
print('Para uma viagem de 650km, o carro {} gastará R${:.2f} sendo {} litros de Etanol.'.format(nome, valor,qlitros))
