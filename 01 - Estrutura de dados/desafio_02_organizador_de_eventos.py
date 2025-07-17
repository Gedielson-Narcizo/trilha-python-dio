# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# todo: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip() 

    # Encontra a última ocorrência de vírgula para separar nome e tema
    posicao_virgula = linha.rfind(",")
    
    # Separa o nome do participante e o tema
    participante = linha[:posicao_virgula] # faz a separação do nome do participante
    tema = linha[posicao_virgula + 1:] # faz a separação do tema do participante
    
    # Adiciona o participante ao dicionário de eventos
    if tema not in eventos: # verifica se o tema já existe no dicionário
        # Se não existir, cria uma nova lista para o tema
        eventos[tema] = [] # cria uma nova lista para o tema
    # Adiciona o participante à lista do tema
    eventos[tema].append(participante)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")