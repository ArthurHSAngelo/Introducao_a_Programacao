#1. Faça um algoritmo que solicite a idade de uma pessoa e exiba se ela é maior ou menor de idade.
print('EX 01')
idade = int(input('Qual é a sua idade? '))
if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você ainda é menor de idade')

#2. Crie um algoritmo que peça dois números inteiros e exiba qual deles é o maior.
print('EX 02')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
else:
    print('O número {} é maior que o número {}'.format(n2, n1))

#3. Escreva um algoritmo que solicite um número e exiba se ele é par ou ímpar.
print('EX 03')
n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))

#4. Faça um algoritmo que solicite três números e exiba qual deles é o menor.
print('EX 04')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
if n1 < n2 and n1 < n3:
    print('O menor número é o número {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O menor número é o número {}'.format(n2))
else:
    print('O menor número é o número {}'.format(n3))

#5. Crie um algoritmo que peça o nome do usuário e exiba uma mensagem de boas-vindas personalizada, de acordo com o horário do dia.
print('EX 05')
nome = str(input('Digite qual é o seu nome: '))
from datetime import datetime
data = datetime.now()
hora = data.hour
if nome.isalpha() and 0 <= hora <= 5:
    print('Boa madrugada {}!'.format(nome))
elif nome.isalpha() and 6 <= hora <= 11:
    print('Bom dia {}!'.format(nome))
elif nome.isalpha() and 12 <= hora <= 17:
    print('Boa tarde {}!'.format(nome))
elif nome.isalpha() and 18 <= hora <= 23:
    print('Boa noite {}!'.format(nome))
else:
    print('ERRO')

#6. Escreva um algoritmo que solicite uma nota de 0 a 10 e exiba se ela é inválida (maior que 10 ou menor que zero), ruim (0 a 4), regular (4 a 6), boa (6 a 8) ou excelente (8 a 10).
print('EX 06')
nota = float(input('Digite uma nota de 0 a 10: '))
if nota <0 or nota >10:
    print('A nota é inválida')
elif nota <=4:
    print('A nota é ruim')
elif 4 <= nota <= 6:
    print('A nota é regular')
elif 6 <= nota <= 8:
    print('A nota é boa')
else:
    print('A nota é excelente!')

#7. Faça um algoritmo que solicite o salário de um funcionário e exiba seu salário líquido, considerando um desconto de 11% para o INSS.
print('EX 07')
salario = float(input('Digite o seu salário: '))
sliquido = salario - (salario * 0.11)
print('Seu salário líquido é R${:.2f} considerando um desconto de 11% para o INSS'.format(sliquido))

#8. Crie um algoritmo que solicite um número inteiro e exiba se ele é positivo, negativo ou zero.
print('EX 08')
n = int(input('Digite um número inteiro: '))
if n > 0:
    print('O número {} é positivo!'.format(n))
elif n < 0:
    print('O número {} é negativo!'.format(n))
else:
    print('O número é 0')

#9. Escreva um algoritmo que solicite um número e exiba se ele é múltiplo de 5 e de 7.
print('EX 09')
n = float(input('Digite um número: '))
if n % 5 == 0 and n % 7 == 0:
    print('O número {} é múltiplo de 5 e de 7'.format(n))
elif n % 5 == 0:
    print('O número {} é múltiplo de 5'.format(n))
elif n % 7 == 0:
    print('O número {} é múltiplo de 7'.format(n))
else:
    print('O número {} não é múltiplo nem de 5 nem de 7'.format(n))

#10. Faça um algoritmo que solicite a idade de uma pessoa e exiba se ela está na faixa etária de criança (até 12 anos), adolescente (entre 13 e 17 anos), adulto jovem (entre 18 e 29 anos), adulto (entre 30 e 59 anos) ou idoso (a partir de 60 anos).
print('EX 10')
idade = int(input('Qual é a sua idade? '))
if 0 <= idade <= 12:
    print('Você tem {} anos, então é uma criança!'.format(idade))
elif 13 <= idade <= 17:
    print('Você tem {} anos, então é um adolescente!'.format(idade))
elif 18 <= idade <= 29:
    print('Você tem {} anos, então é um jovem adulto!'.format(idade))
elif 30 <= idade <= 59:
    print('Você tem {} anos, então é um adulto!'.format(idade))
elif 60 <= idade <= 120:
    print('Você tem {} anos, então é um idoso!'.format(idade))
else:
    print('Tem algo errado aí! Que idade é essa?')

#11. Faça um algoritmo que solicite duas notas de um aluno e exiba sua média. Se a média for maior ou igual a 6, exiba a mensagem "Aprovado". Caso contrário, exiba a mensagem "Reprovado".
print('EX 11')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2) / 2
if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')

#12. Crie um algoritmo que solicite o nome do usuário e a sua idade, e exiba uma mensagem informando se ele pode ou não dirigir. Considere que apenas maiores de 18 anos podem dirigir.
print('EX 12')
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
if nome.isalpha():
    if idade >= 18:
        print('{} você pode dirigir!'.format(nome))
    else:
        print('{} você não pode dirigir ainda!'.format(nome))
else:
    print('Seu nome provavelmente está errado')

#13. Escreva um algoritmo que solicite uma letra do alfabeto e exiba se ela é vogal ou consoante.
print('EX 13')
letra = str(input('Digite uma letra do alfabeto de A a Z: ')).lower().strip()
if letra.isalpha():
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('A letra "{}" é uma vogal'.format(letra))
    else:
        print('A letra "{}" é uma consoante'.format(letra))
else:
    print('Isso não é uma letra!')

#14. Faça um algoritmo que solicite o valor de três lados de um triângulo e exiba se ele é equilátero, isósceles ou escaleno.
print('EX 14')
l1 = float(input('Digite o valor do primeiro lado de um triângulo: '))
l2 = float(input('Digite o valor do segundo lado de um triângulo: '))
l3 = float(input('Digite o valor do terceiro lado de um triângulo: '))
if l1 == l2 and l1 == l3:
    print('O triângulo é EQUILÁTERO')
elif l1 == l2 and l1 != l3 or l3 == l1 and l3 != l2 or l2 == l3 and l2 != l1:
    print('O triângulo é ISÓSCELES')
else:
    print('O triângulo é ESCALENO')

#15. Crie um algoritmo que solicite um número inteiro e exiba se ele é primo ou não.
print('EX 15')
n = int(input('Digite um número inteiro: '))
if n < 2:
    print('O número não é primo')
else:
    primo = True
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print('O número é primo')
    else:
        print('O número não é primo')

#16. Escreva um algoritmo que solicite a altura e o peso de uma pessoa, e exiba seu índice de massa corporal (IMC). Considere a fórmula IMC = peso / altura^2. Classifique o resultado de acordo com a descrição abaixo:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 24.9: peso normal
# entre 25 e 29.9: sobrepeso
# entre 30 e 34.9: obesidade grau 1
# entre 35 e 39.9: obesidade grau 2
# acima de 40: obesidade grau 3
print('EX 16')
altura = float(input('Digite qual é a sua altura: '))
peso = float(input('Digite qual é o seu peso: '))
imc = peso / (altura ** 2)
if imc <= 0:
    print('Digitou número errado')
elif imc <= 18.5:
    print('Seu imc é {:.2f} Abaixo do peso'.format(imc))
elif 18.5 <= imc <= 24.9:
    print('Seu imc é {:.2f} Peso normal'.format(imc))
elif 25 <= imc <= 29.9:
    print('Seu imc é {:.2f} Sobrepeso'.format(imc))
elif 30 <= imc <= 34.9:
    print('Seu imc é {:.2f} Obesidade grau 1'.format(imc))
elif 34 <= imc <= 39.9:
    print('Seu imc é {:.2f} Obesidade grau 2'.format(imc))
else:
    print('Seu imc é {:.2f} Obesidade grau 3'.format(imc))

#17. Faça um algoritmo que solicite a hora atual e exiba uma mensagem de acordo com a tabela abaixo:
# entre 0 e 5: boa madrugada
# entre 6 e 11: bom dia
# entre 12 e 17: boa tarde
# entre 18 e 23: boa noite
print('EX 17')
hora = int(input('Digite que horas são, informe apenas as horas (no formato 24hrs): '))
if hora < 0 or hora >= 24:
    print('Que hora é essa?? Digite um número de 0 a 24!')
elif 0 <= hora <= 5:
    print('Boa madrugada, são {} horas'.format(hora))
elif 6 <= hora <= 11:
    print('Bom dia, são {} horas'.format(hora))
elif 12 <= hora <= 17:
    print('Boa tarde, são {} horas'.format(hora))
elif 18 <= hora <= 23:
    print('Boa noite, são {} horas'.format(hora))

#18. Escreva um algoritmo que solicite um número inteiro e exiba a tabuada desse número, do 1 ao 10.
print('EX 18')
n = int(input('Digite um número inteiro para tabuada: '))
print(n,'x 1 =', n * 1)
print(n,'x 2 =', n * 2)
print(n,'x 3 =', n * 3)
print(n,'x 4 =', n * 4)
print(n,'x 5 =', n * 5)
print(n,'x 6 =', n * 6)
print(n,'x 7 =', n * 7)
print(n,'x 8 =', n * 8)
print(n,'x 9 =', n * 9)
print(n,'x 10 =', n * 10)

#19. Faça um algoritmo que solicite um número inteiro e exiba se ele é palíndromo. Um número é palíndromo quando ele é igual ao número lido ao contrário. Exemplo: 121 é palíndromo.
print('EX 19')
n = input('Digite um número inteiro: ')
if n.isnumeric():
    if n == n[::-1]:
        print('O número {} é um palíndromo'.format(n))
    else:
        print('O número {} não é um palíndromo'.format(n))
else:
    print('Número inválido, digite um número inteiro')

#20. Crie um algoritmo que solicite o nome do usuário e sua idade, e exiba uma mensagem informando se ele pode ou não votar. Considere que apenas maiores de 16 anos podem votar.
print('EX 20')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if nome.isalpha():
    if idade >= 16:
        print('Olá {}, você tem {} anos então já pode votar!'.format(nome,idade))
    else:
        print('Olá {}, você ainda tem {} anos então você não pode votar!'.format(nome,idade))
else:
    print('Seu nome está errado, digite apenas letras')
    print('-----------------FIM-----------------')
