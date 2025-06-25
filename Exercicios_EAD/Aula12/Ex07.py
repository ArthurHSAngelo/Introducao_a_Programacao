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