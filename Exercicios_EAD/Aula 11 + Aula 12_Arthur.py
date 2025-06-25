print('-=' * 10, 'Aula 11 EX 01', '-=' * 10)
string = input('Digite uma palavra: ').strip()
print('A quantidade de letras é : ', len(string))

print('-=' * 10, 'Aula 11 EX 02', '-=' * 10)
string = input('Digite uma palavra: ').strip()
print('O primeiro caractere é:', string[0])
print('O último caractere é:', string[-1])

print('-=' * 10, 'Aula 11 EX 03', '-=' * 10)
string = input('Digite uma palavra: ').strip()
print(string[1::2])

print('-=' * 10, 'Aula 11 EX 04', '-=' * 10)
string = input('Digite uma string para verificar se é um palíndromo: ').strip()
if string == string[::-1]:
    print('É um Palíndromo!')
else:
    print('Não é palíndromo')
print(string[::-1])

print('-=' * 10, 'Aula 11 EX 05', '-=' * 10)
string = input('Digite uma palavra: ').strip().lower()
print('Substituindo letras "a", por "i"', string.replace("a", "i"))

print('-=' * 10, 'Aula 11 EX 06', '-=' * 10)
string_1 = input('Digite uma string: ').strip()
string_2 = input('Digite outra string: ').strip()
print('A concatenação dessas duas strings é:', string_1 + string_2)

print('-=' * 10, 'Aula 11 EX 07', '-=' * 10)
palavra = input('Digite uma string: ').strip()
print('Invertendo a ordem dos caracteres:', palavra[::-1])

print('-=' * 10, 'Aula 11 EX 08', '-=' * 10)
palavra = input('Digite uma palavra: ').lower().strip()
caractere = input('Qual caractere você deseja contar? ').lower().strip()
cont = palavra.count(caractere)
print('A palavra {} possui {} caracteres "{}"'.format(palavra, cont, caractere))

print('-=' * 10, 'Aula 11 EX 09', '-=' * 10)
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

print('-=' * 10, 'Aula 11 EX 10', '-=' * 10)
string = input('Digite uma frase: ').strip()
print('A frase capitalizada é:', string.title())

print('-=' * 10, 'Aula 12 EX 01', '-=' * 10)
inteiro = list()
for i in range(5):
    n = int(input('Digite um número inteiro: '))
    inteiro.append(n)
print(inteiro)

print('-=' * 10, 'Aula 12 EX 02', '-=' * 10)
lista = list()
for i in range(10):
    n = float(input('Digite o {}° número real: '.format(i+1)))
    lista.append(n)
print(lista[::-1])

print('-=' * 10, 'Aula 12 EX 03', '-=' * 10)
notas = list()
for i in range(4):
    n = float(input('Digite a {}° nota: '.format(i+1)))
    notas.append(n)
print(notas)
media = sum(notas) / 4
print('A média das notas é: {}'.format(media))

print('-=' * 10, 'Aula 12 EX 04', '-=' * 10)
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

print('-=' * 10, 'Aula 12 EX 05', '-=' * 10)
numeros = list()
par = list()
impar = list()
c = 0
while c != 20:
    numero = input('Digite o {}° número inteiro: '.format(c+1))
    if numero.isnumeric():
        c += 1
        numeros.append(numero)
        numero = int(numero)
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)
    else:
        print('Não é um número inteiro.')
print('Os números digitados foram:', numeros)
print('Os números pares foram:',par)
print('Os números ímpares foram:',impar)

print('-=' * 10, 'Aula 12 EX 06', '-=' * 10)
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

print('-=' * 10, 'Aula 12 EX 07', '-=' * 10)
try:
    count=0
    Sistemas=["Windows Server","Unix","Linux","Netware","Mac OS","Outros"]
    resposta={"Num 1":0, "Num 2":0,"Num 3":0, "Num 4":0, "Num 5":0,"Num 6":0}
    while True:
        try:
            print("Por Favor, responda!")
            print("As Possíveis respostas são:\n1-Windows Server\n2-Unix\n3-Linux\n4-Netware\n5-Mac OS\n6-Outros")
            res=int(input("Qual o melhor Sistema Operacional para o uso em servidores?(Digite 0 para finalizar o Programa)"))
            
            if res==0:
                print("Programa Finalizado")
                break
            elif res>=1 and res<=6:
                count+=1
                escolha=f"Num {res}"
                resposta[escolha]+=1
            else:
                print("O valor digitado não é válido, por favor digite um valor entre 0 e 6")   
        except ValueError:
            print("Valor inválido, Por favor digte um número inteiro.")

    porcentagens = {sistema: (resposta[f"Num {i+1}"] / count) * 100 for i, sistema in enumerate(Sistemas)}
    print("\nResultados da Votação:")
    print("{:<20} {:<10} {:<15}".format("Sistema Operacional", "Votos", "Porcentagem"))
    print("-" * 45)
    for i, sistema in enumerate(Sistemas):
        votos = resposta[f"Num {i+1}"]
        porcentagem = porcentagens[sistema]
        print("{:<20} {:<10} {:.2f}%".format(sistema, votos, porcentagem))
    print("-" * 45)
    print(f"Total de votos: {count}")
    vencedor = max(porcentagens, key=porcentagens.get)
    totalvotos=resposta[f"Num {Sistemas.index(vencedor)+1}"]
    print(f"O Sistema Operacional mais votado foi o {vencedor}, com {totalvotos} votos, correspondendo a {porcentagens[vencedor]:.2f}")

except ZeroDivisionError:
    print("Nenhum dado foi inserido.")

print('-=' * 10, 'Aula 12 EX 08', '-=' * 10)
import random
count=0
dado={"numero 1":0,"numero 2":0,"numero 3":0,"numero 4":0,"numero 5":0,"numero 6":0}
for i in range(0,100):
    count+=1
    res=random.randint(1, 6)
    valor=f"numero {res}"
    dado[valor]+=1
vencedor=max(dado,key=dado.get)
totalvotos=dado[vencedor]
print(f"O número vencedor foi o {vencedor} com {totalvotos} vezes aparecidos")
print(dado)