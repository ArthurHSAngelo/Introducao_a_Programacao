pessoa = {
    "Nome": "Arthur",
    "RG": "MG-15.122.123",
    "CPF": "154.235.235-85"
}
del pessoa["RG"]
pessoa.pop("CPF")
print(pessoa)