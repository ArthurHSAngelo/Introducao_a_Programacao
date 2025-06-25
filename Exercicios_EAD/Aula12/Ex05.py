numeros = list()
par = list()
impar = list()
c = 0
while c != 20:
    numero = input('Digite o {}° número inteiro: '.format(c+1))
    if numero.isnumeric():
        c += 1
        numeros.append(numero)
        numero = int(numero)
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)
    else:
        print('Não é um número inteiro.')
print('Os números digitados foram:', numeros)
print('Os números pares foram:',par)
print('Os números ímpares foram:',impar)
