i = int(input('Digite a sua idade: '))
menor = 0
adulto = 0
idoso = 0
while 0 <= i <= 120:
    if i <= 18:
        menor += 1
    elif 19 <= i <= 60:
        adulto += 1
    elif i > 60:
        idoso += 1
    i = int(input('Digite a sua idade: '))        
print('-=' * 30)
print('''A quantidade é:
menor = {}
adulto = {}
idoso = {}'''.format(menor, adulto, idoso))