string = input('Digite uma string para verificar se é um palíndromo: ').strip()
if string == string[::-1]:
    print('É um Palíndromo!')
else:
    print('Não é palíndromo')
print(string[::-1])