consoantes = list()
vogais = ['a', 'e', 'i', 'o', 'u']
c = 0
while c != 10:
    letra = input('Informe o {}° caractere: '.format(c+1))
    if len(letra) == 1 and letra.isalpha():
        c += 1
        if letra not in vogais:
            consoantes.append(letra)
    else:
        print('Entrada inválida')
print('Foram lidas {} consoantes, seguem elas: \n {}'.format(len(consoantes), consoantes))