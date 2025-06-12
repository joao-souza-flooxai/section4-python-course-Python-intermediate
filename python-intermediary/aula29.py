produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}

print(dc)

s1 = {i for i in range(10)}
print(set(range(10)))