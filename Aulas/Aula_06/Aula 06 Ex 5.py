n = str(input('Qual é o seu nome: '))
s = str(input('Qual é o seu sexo: \n Digite F para feminino e M para masculino \n:')).upper().strip()
if s == 'F':
    print('Ilmo Sra. {}'.format(n))
elif s == 'M':
    print('Ilmo Sr. {}'.format(n))
else: 
    print('Sexo está incorreto')
