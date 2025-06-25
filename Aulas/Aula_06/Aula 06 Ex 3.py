salario = float(input('Digite o salário atual: '))

if salario <= 0:
    print('Erro, número negativo informado')
elif salario <= 300:
    print('Seu salário teve um aumento de 35% e agora é de {:.2f}'.format(salario * 1.35))
else: 
    print('Seu salário teve um aumento de 15% e agora é de {:.2f}'.format(salario * 1.15))
    