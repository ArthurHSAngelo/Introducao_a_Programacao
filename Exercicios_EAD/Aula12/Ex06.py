cont = 0
maior = 0
while True:
    saltos = list()
    nome = str(input('Digite o nome do atleta (se não inserir nada o prograda finalizado): ')).strip()
    if nome =='':
        print('Encerrando programa.')
        break
    else:
        while cont != 5:
            try:
                cont += 1
                salto = float(input('Digite a distância do {}° salto: '.format(cont)))
                saltos.append(salto)
                if salto > maior:
                    maior = salto
            except ValueError:
                print('Você precisa informar um número.')
                cont -= 1
        soma = sum(saltos)
        media = soma / 5

        print('')
        print('Atleta:',nome)        
        print('')
        print('Primeiro Salto: {:.1f} m'.format(saltos[0]))
        print('Segundo Salto: {:.1f} m'.format(saltos[1]))
        print('Terceiro Salto: {:.1f} m'.format(saltos[2]))
        print('Quarto Salto: {:.1f} m'.format(saltos[3]))
        print('Quinto Salto: {:.1f} m'.format(saltos[4]))
        print('')
        print('Resultado final:',maior)
        print('Atleta:',nome)
        print('Saltos:',saltos)
        print('Média dos saltos: {:.1} m'.format(media))
        break