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