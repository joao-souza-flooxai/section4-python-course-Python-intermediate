# Sets - Conjuntos em Python: (tipo set)

# Conjuntos são ensinados na matemática

# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set:
# set(iterável) ou {1, 2, 3}

# Sets são eficientes para remover valores duplicados
# de iteráveis.

# - eles não têm índices;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

s1 = set()
s1 = {"João", 1,2,3, 5.5, 7,7,7,7,7}
print(s1) #sem valores duplicados
lista = [1,1,1,1,1,1,2]
s1 = set(lista)
print(s1)




