linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"] resulta em ordem alfabética
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"] retorna em ordem alfabética reversa
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"] retorna pela quantidade de caracteres
'''
"Para cada elemento 'x' dentro da lista 'linguagens', use o tamanho de 'x' (quantidade de caracteres)
 como chave para ordenar a lista."
'''
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"] retorna pela quantidade de caracteres em ordem decrescente
print(linguagens)
