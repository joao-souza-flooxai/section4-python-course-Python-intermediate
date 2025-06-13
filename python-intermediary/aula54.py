# Exercicio - Unir listas

# Crie uma função zipper (como o zipper de roupas)

# O trabalho dessa função será unir duas

# listas na ordem.

# Use todos os valores da menor lista.

# EX.            1

# ['Salvador', 'Ubatuba', 'Belo Horizonte']

# ['BA', 'SP', 'MG', 'RJ']

# Resultado

# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(list1, list2):
    min_length = min(len(list1), len(list2))
    result = []
    for i in range(min_length):
        result.append((list1[i], list2[i]))
    return result

print(zipper(['Salvador', 'Ubatuba', 'Belo Horizonte'], ['BA', 'SP', 'MG', 'RJ']))
