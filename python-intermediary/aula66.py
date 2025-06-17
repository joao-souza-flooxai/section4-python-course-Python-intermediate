#Problema dos parâmetros mutaveis em funções Python

def adiciona_clientes(nome, lista=None):
    if(lista is None):
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('José')
adiciona_clientes('João', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('Helena')
adiciona_clientes('Agatha', cliente3)
print(cliente3)