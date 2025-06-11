

pessoa = {}


chave = 'nome'

pessoa[chave] = 'Luiz Otavio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'
del pessoa['sobrenome']
print(pessoa)
# print(pessoa['sobrenome']) erro

if pessoa.get('sobrenome') is not None:
    print('Existe')
else:
     print('Não Existe')
