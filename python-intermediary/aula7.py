
# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicado = multiplicar(1, 2, 3, 4, 5)
print(multiplicado)

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))