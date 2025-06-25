lista = list()
for i in range(10):
    n = float(input('Digite o {}° número real: '.format(i+1)))
    lista.append(n)
print(lista[::-1])