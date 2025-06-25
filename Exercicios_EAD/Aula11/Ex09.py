string = input('Digite uma palavra: ')
sequencia = input('Digite a sequência que deseja saber se a palavra possui: ')
inicio = string.startswith(sequencia)
final = string.endswith(sequencia)
if inicio:
    print('A palavra inicia com a sequência', inicio)
elif final:
    print('A palavra finaliza com a sequência',final)
else:
    print('A palavra não possui a sequência citada')