# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca' ],
    ['p','m','g'],
    ['masculina','feminina','unisex']
]

print_iter(combinations(pessoas,2))
print()
print_iter(permutations(pessoas,2))

print_iter(product(*camisetas))
