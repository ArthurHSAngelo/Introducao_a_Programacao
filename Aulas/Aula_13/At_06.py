pessoa = {
    "Nome": "Arthur",
    "RG": "MG-15.122.123",
    "CPF": "154.235.235-85"
}
for x in pessoa:
    print(x)
    print(pessoa[x])
    
for x, y in pessoa.items():
    print(x, y)
    