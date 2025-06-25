#1. Faça um algoritmo que receba quatro números inteiros, processa o valor cúbico de todos, processa a soma entre eles, e exibe o resultado na tela.
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))

resultado = (n1 ** 3) + (n2 ** 3) + (n3 ** 3) + (n4 ** 3)

print('A soma do valor cúbico dos números digitados é: {}'.format(resultado))

#2. Faça um algoritmo que receba a base e a altura de um retângulo (entrada), calcule a área usando a fórmula área = base * altura (processamento), e exiba o resultado da área na tela (saída).
base = float(input('Digite a base do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

area = base * altura

print('A área do retângulo é {:.2f}'.format(area))

#3.Faça um algoritmo que receba o valor de uma compra e o valor pago pelo cliente (entrada), calcule o troco apenas com subtração (processamento), e exiba o valor do troco na tela (saída).
valor_compra = float(input('Qual é o valor da compra? '))
valor_pago = float(input('Qual foi o valor pago pelo cliente? '))

troco = valor_pago - valor_compra

print('O valor do troco necessário é R${:.2f}'.format(troco))

#4. Faça um algoritmo que receba o raio de uma circunferência, calcule e mostre ao usuário:
r = float(input('Digite o raio: '))

a = 2 * 3.14159 * r
b = 3.14159 * (r ** 2)
c = (4 * 3.14159 * (r ** 3) / 3 )

print('O comprimento da esfera é: {:.2f}'.format(a))
print('A área da esfera é :{:.2f}'.format(b))
print('O volume da esfera é:{:.2f}'.format(c))

#5. Faça um algoritmo que receba a medida de dois ângulos de um triângulo. Calcule e mostre o valor do terceiro ângulo, sabendo que a soma dos três ângulos internos de um triângulo é de 180º.
a1 = float(input('Digite o primeiro ângulo: '))
a2 = float(input('Digite o segundo ângulo: '))

a3 = 180 - a1 - a2

print('O valor do terceiro ângulo é {:.2f}, sabendo que a soma é 180°'.format(a3))

#6. Faça um algoritmo que receba o salário atual de um funcionário (entrada), calcule o novo salário com um aumento de 15% (processamento), e exiba o novo salário na tela (saída).
s = float(input('Digite seu salário atual: '))

ns = s * 1.15

print('O seu novo salário é R${:.2f}'.format(ns))

#7. Faça um algoritmo que receba uma temperatura em celsius e transforme em Farenheit
c = float(input('Digite quantos graus Celsius: '))

f = (c * 1.8) + 32

print('{:.2f}° Celsius, são {:.2f}° Farenheit'.format(c,f))

#8. Faça uma algoritmo que receba uma medida em pés, processe e mostre os valores dessa medida em polegadas, jardas e milhas.
pes = float(input('Digite quantos pés: '))

pol = pes * 12
jar = pes / 3
mil = jar / 1760

print('{} pés são: {:.2f} polegadas, {:.2f} jardas e {:.4f} milhas'.format(pes,pol,jar,mil))

#9. Crie um algoritmo que receba em duas variáveis distintas: o valor das horas e dos minutos de um dia. Calcule e mostre quantos segundos se passaram desde a meia-noite desse dia.
h = int(input('Digite o valor das horas (no formato 24 horas): \n Ex: "20" horas (apenas os números) \n :'))
m = int(input('Digite o valor dos minutos: \n Ex: "53" minutos (apenas os números) \n :'))

s = (h * 3600) + (m * 60)

print('Se passaram {} segundos desde a meia-noite!'.format(s))

#10. 10. A prefeitura de uma cidade abriu uma linha de crédito aos seus servidores com a seguinte regra.– O valor máximo das prestações não pode ser superior a 30% do seu salário. Desenvolva um algoritmo que receba o salário de um funcionário, calcule e exibe o valor máximo da prestação que pode ser paga por esse funcionário.
s = float(input('Digite seu salário atual: '))

p = s * 0.30

print('O valor máximo da prestação que pode ser paga por você é de R${:.2f}'.format(p))
