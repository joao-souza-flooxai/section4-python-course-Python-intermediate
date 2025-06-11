#Função Lambda

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda', 'idade': 20 },
    {'nome': 'Maria', 'sobrenome': 'Oliveira', 'idade': 31 },
    {'nome': 'Daniel', 'sobrenome': 'Silva', 'idade': 50 },
    {'nome': 'Eduardo', 'sobrenome': 'Moreira', 'idade': 89},
    {'nome': 'Aline', 'sobrenome': 'Souza','idade': 10}
]

def por_nome(item):
    return item['nome']
def por_idade(item):
    return item['idade']

def exibir(lista, mensagem=''):
    print(mensagem)
    for item in lista:
        print(item)

lista.sort(key=por_nome)

exibir(lista, 'Ordenados por nome:')

lista.sort(key=por_idade)

exibir(lista,  'Ordenados por idade:')

#Com lambda para omitir a função

lista.sort(key=lambda item: item['nome'])
exibir(lista, 'Ordenados por nome, com lambda:')

#Para não alterar a lista orginal
lista2 = sorted(lista, key=lambda item: item['idade'])
exibir(lista, "Lista original(ordenada por nome):")
exibir(lista2, "Lista com sorted(ordenada por idade):")