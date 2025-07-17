contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

print(list(contatos.keys()))  # esse é o jeito mais comum de acessar as chaves 
# de um dicionário e o retorno é:
# ["guilherme@gmail.com", "giovanna@gmail.com", "chappie@gmail.com", "melaine@gmail.com"]

for email, info in contatos.items():
    print(f"{email}: {info['nome']} - {info['telefone']}") # esse é o jeito mais comum
# de iterar sobre dicionários aninhados e retorna o nome e telefone de cada contato

