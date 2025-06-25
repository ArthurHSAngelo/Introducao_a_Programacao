cont1 = 0
cont2 = 0 
cont3 = 0
idade = int(input('Digite a idade de uma pessoa (entre 0 e 120): '))
while 0 <= idade <= 120:
    if idade <= 18:
        cont1 += 1
    elif 19 <= idade <= 60:
        cont2 += 1
    elif idade > 60:
        cont3 += 1
    idade = int(input('Digite a idade de uma pessoa (entre 0 e 120): '))
print('-=' * 20)
print('''O total das faixas etárias é:
1° idade = {}
2° idade = {}
3° idade = {}'''.format(cont1, cont2, cont3))
