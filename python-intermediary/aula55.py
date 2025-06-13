'''
    Considerando duas listas de inteiros ou floats (lista A e lista B)
    Some os valores nas listas retornando uma nova lista com os valores somados:

    Se uma lista for maior que a outra, a soma só valerá considerar o tamanho da menor.

    Exemplo:
    lista_a = [1, 2, 3, 4]
    lista_b = [1, 2, 3, 4, 5]

    resultado
    lista_soma = [a + b for a, b in zip(lista_a, lista_b)]
'''


def somar_listas(lista_a, lista_b):
    
    #Soma os elementos das duas listas, considerando apenas o tamanho da menor.
    
    return [a + b for a, b in zip(lista_a, lista_b)]

lista_a = [1, 2, 3, 4]
lista_b = [1, 2, 3, 4, 5]

lista_soma = somar_listas(lista_a, lista_b)
print(lista_soma)