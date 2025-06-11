#Dicionário
pessoa = {
    'nome': 'João Victor',
    'sobrenome': 'Crivoi'
}
pessoa2 = dict(nome='Lucas', sobrenome='Almeida')
print(pessoa ,type(pessoa))
print(pessoa2 ,type(pessoa2))

pessoa3 = {
    'nome': 'Luiz Otavio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321}
    ]
}

for chave in pessoa3:
    print(chave, pessoa3[chave], sep='\n')


for endereco in pessoa3:
    print(pessoa3[endereco], sep='\n')

pessoa3['telefone'] = '12345'
print(pessoa3)