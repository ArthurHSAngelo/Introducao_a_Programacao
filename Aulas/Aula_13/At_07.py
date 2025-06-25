pessoa = {
    "Nome": "Thais Carla",
    "RG": "MG-15.122.123",
    "CPF": "154.235.235-85"
}
mydict = pessoa.copy()
print(mydict)
pessoa.clear()
print(pessoa)
mydict["peso"] = "800"
print(mydict)