idade = int(input('Digite sua idade: '))
if idade >= 18 and idade <= 100:
    print('Você atingiu a maioridade')
elif idade >= 0 and idade <= 18:
    print('Você ainda não atingiu a maioridade')
else: 
    print('Idade é inválida')