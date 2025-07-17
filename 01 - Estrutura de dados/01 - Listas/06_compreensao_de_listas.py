# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0] 

''' 
"Retorne 'numero' para cada 'numero' dentro da lista de
 'numeros' se o resto da divisão de 'numero' por 2 for igual a zero.
 '''
# Isso significa que estamos filtrando os números pares da lista.
# A variável 'pares' agora contém apenas os números pares da lista original.

print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
