lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()


l2[0] = 2
l2[1] = "Java"

print(lista)  # [1, "Python", [40, 30, 20]]
print(l2)  # [2, "Java ", [40, 30, 20]]