notas = list()
for i in range(4):
    n = float(input('Digite a {}° nota: '.format(i+1)))
    notas.append(n)
print(notas)
media = sum(notas) / 4
print('A média das notas é: {}'.format(media))