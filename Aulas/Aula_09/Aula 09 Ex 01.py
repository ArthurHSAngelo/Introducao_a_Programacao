n = int(input('Digite um número inteiro: '))
contmenor = 0
contmaior = 0
while n > 0:
    if n > 5:
        print('O número {} é maior que 5'.format(n))
        contmaior += 1 
    else:
        contmenor += 1
    n = int(input('Digite um número inteiro: '))
print('-=' * 20)
print('''{} números são maiores que 5
{} número são menores que 5'''.format(contmaior, contmenor))
        