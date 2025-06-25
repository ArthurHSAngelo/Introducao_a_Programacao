n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

if (n1 < 0 or n2 < 0 or n3 < 0):
    print('Uma das notas é negativa')
elif (n1 > 10 or n2 > 10 or n3 > 10):
    print('Uma das notas é maior que 10')
else: 
    m = (n1 + n2 + n3) / 3 

    if m >= 7 :
        print('Você foi aprovado!')
    else:
        print('Você foi reprovado!')