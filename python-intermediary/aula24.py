# Empacotamento e desempacotamento de dicionários
a, b = 1, 2

a, b = b, a

# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
a, b = pessoa.values() #traz os valores
print(a, b)
a, b = pessoa.items() #traz as tuplas
print(a, b)
(a1, a2), (b1,b2) = pessoa.items() #traz os valores das tuplas e o nome dos campos
print(a1, a2, b1, b2)

for valor in pessoa.items():
    print(valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}

print(pessoas_completa)


# args e kwargs
# args 
# kwargs - keyword arguments - (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Joana', qlq=123)

mostro_argumentos_nomeados(**pessoas_completa)