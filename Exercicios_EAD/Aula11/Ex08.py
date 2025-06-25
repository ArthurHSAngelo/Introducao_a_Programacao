palavra = input('Digite uma palavra: ').lower().strip()
caractere = input('Qual caractere você deseja contar? ').lower().strip()
cont = palavra.count(caractere)
print('A palavra {} possui {} caracteres "{}"'.format(palavra, cont, caractere))