
# Argumentos nomeados

# *args (empacotamento e desempacotamento)
# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4

print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0 
    for numero in args:
        print(numero)
        total +=numero
    return total

total = soma(1, 2, 3, 4, 5, 6)
print("Esse é o total que veio da função: ", total )
numeros = 1, 2, 3, 4, 5, 6
print(sum(numeros))
print(soma(*numeros))
