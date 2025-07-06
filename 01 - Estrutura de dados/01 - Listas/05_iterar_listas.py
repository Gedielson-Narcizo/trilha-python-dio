carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): # Enumerate retorna o índice e o valor do elemento
    print(f"{indice}: {carro}") 
