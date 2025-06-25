pessoa = {
    "Nome": "Arthur",
    "RG": "MG-15.122.123",
    "CPF": "154.235.235-85"
}
pessoa.update({"RG": "MG-00.000.000"})
print(pessoa)
if "CPF" in pessoa:
    print(pessoa["CPF"])
    