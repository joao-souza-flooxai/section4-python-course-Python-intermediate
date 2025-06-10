'''
    Introdução às funções (def) em Python

    Funções são trechos de código usados para
    replicar determinada ação ao longo do seu código.
    Elas podem receber valores para parâmetros (argumentos)
    e retornar um valor específico.
    Por padrão, as funções Python retornam None (nada).
'''


def print_function(i):
    print('Varias' + str(i))
    print('Varias2'  + str((i+1)))

print_function(1)
print_function(2)
