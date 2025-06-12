#filtro
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]



novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.85}
    if produto['preco'] > 20 else {**produto} #mapeamento(antes do for)
    for produto in produtos
    if ((produto['preco']  * 1.85 )> 10) #filtra depois de mapear
]

print(novos_produtos)