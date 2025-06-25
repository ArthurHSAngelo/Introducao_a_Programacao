n = str(input('Digite seu nome: ')).upper()
if n[0] == 'A' or n[0] == 'E' or n[0] == 'I' or n[0] == 'O' or n[0] == 'U':
    print('Seu nome começa com uma vogal, e ela é: {}'.format(n[0]))
else: print('Seu nome começa com uma consoante!')
