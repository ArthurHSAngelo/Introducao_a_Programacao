print('-=' * 10, 'EX 01', '-=' * 10)
n1 = float(input('Digite um primeiro número: '))
n2 = float(input('Digite um segundo número: '))
opcao = 0

print(''' =-= Menu de Operações Matemáticas =-= 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair''')

while opcao != 5:
    opcao = int(input('Qual opção você quer? '))
    match opcao:
        case 1:
            print('A soma de {} e {} é {:.2f}\n'.format(n1, n2, n1 + n2))
        case 2:
            print('A subtração de {} e {} é {:.2f}\n'.format(n1, n2, n1 - n2))
        case 3:
            print('A multiplicação de {} e {} é {:.2f}\n'.format(n1, n2, n1 * n2))
        case 4:
            print('A divisão de {} e {} é {:.2f}\n'.format(n1, n2, n1 / n2))
        case 5:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida')

print('-=' * 10, 'EX 02', '-=' * 10)
n1 = int(input('Digite um número inicial: '))
n2 = int(input('Digite um número final: '))
soma = 0

for i in range(n1, n2+1):
    if i % 2 == 0:
        soma += i

print('A soma dos pares de {} e {} é {}'.format(n1, n2, soma))

print('-=' * 10, 'EX 03', '-=' * 10)
nota = float(input('Digite a 1ª nota do aluno: '))
contador = 0
i = 1
soma = nota + 1

while nota != -1:
    contador += 1
    i += 1
    nota = float(input('Digite a {}ª nota do aluno (-1 para acabar): '.format(i)))
    soma += nota

media = soma / contador
print('A média das {} notas digitadas é {}'.format(contador, media))

print('-=' * 10, 'EX 04', '-=' * 10)
contpos = 0
contneg = 0
contzero = 0

for i in range(1, 11):
    n = int(input('Digite o {}° número inteiro: '.format(i)))
    if n > 0:
        contpos += 1
    elif n < 0:
        contneg += 1
    elif n == 0:
        contzero += 1

print('''No total foram digitados:
{} números positivos
{} números negativos
{} números zero'''.format(contpos, contneg, contzero))

print('-=' * 10, 'EX 05', '-=' * 10)
n = int(input('Digite um número: '))
opcao = 0

print(''' =-= Menu de cálculo de potência e raiz =-= 
1 - Calcula a potência
2 - Calcula a raiz quadrada
3 - Sair''')

while opcao != 3:
    opcao = int(input('Qual opção você quer? '))
    match opcao:
        case 1:
            potencia = float(input('Qual a potência você quer elevar o número {}: '.format(n)))
            print('{} elevado a {:.2f} é {:.2f}'.format(n, potencia, n ** potencia))
        case 2:
            print('A raiz de {} é {:.2f}'.format(n, n ** 0.5))
        case 3:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida')

print('-=' * 10, 'EX 06', '-=' * 10)
while True:
    n = int(input('Digite um número inteiro (0 para sair): '))

    print('Tabuada do {}'.format(n))
    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, n * i))

    if n == 0:
        print('Programa encerrado.')
        break

    novo = input('Deseja repetir com outro número? (s/n): ').lower()
    if novo != 's':
        print('Programa encerrado.')
        break

print('-=' * 10, 'EX 07', '-=' * 10)
n = int(input('Digite um número: '))
soma = 0
if n > 0:
    for i in range(1, n):
        if i % 3 == 0:
            soma += i
print('A soma dos múltiplos de 3 entre 1 e {} é: {}'.format(n, soma))

print('-=' * 10, 'EX 08', '-=' * 10)
n = int(input('Digite um número inteiro positivo: '))
contpar = 0
contimpar = 0
if n > 0:
    while n > 0:
        ultimo_digito = n % 10
        if ultimo_digito % 2 == 0:
            contpar += 1
        else:
            contimpar += 1
        n = n // 10
        print(n)
    print('''Resultado Total:
    Dígitos pares: {}
    Dígitos ímpares: {}'''.format(contpar, contimpar))
else:
    print('Número 0 ou negativo, não vai dar certo ne')

print('-=' * 10, 'EX 09', '-=' * 10)
codigo = 1234
tentativas = 0

while True:
    senha = int(input('Digite a senha numérica: '))
    tentativas += 1

    if senha != codigo and tentativas >= 3:
        print('3 tentativas incorretas, login bloqueado')
        break
    if  senha == codigo:
        print('Senha correta')
        break

print('-=' * 10, 'EX 10', '-=' * 10)
valor_total= 0
opcao = 0

print(''' =-= Menu de Cálculo Acumulado =-= 
1 - Adicionar valor ao total
2 - Subtrair valor do total
3 - Exibir o total
4 - Zerar total
5 - Sair''')

while opcao != 5:
    opcao = int(input('Qual opção você quer? '))
    match opcao:
        case 1:
            adicao = float(input('Quanto você quer adicionar? \n'))
            valor_total += adicao
        case 2:
            subtracao = float(input('Quanto você quer subtrair? \n'))
            valor_total -= subtracao
        case 3:
            print('O valor total é {} \n'.format(valor_total))
        case 4:
            valor_total = 0
            print('Você zerou o valor total \n')
        case 5:
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida. \n')
