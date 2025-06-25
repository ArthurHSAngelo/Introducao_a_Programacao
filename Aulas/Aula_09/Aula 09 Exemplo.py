palavra_secreta = 'python'
count = 0

while True:
    word = input('Entra com palavra secreta: ').lower()
    count += 1
    
    if word == palavra_secreta:
        print('Palavra correta')
        break
    
    if word != palavra_secreta and count >= 3:
        print('Tentativas encerradas!')
        break
