# Métodos Úteis dos dicionários em Python

# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

d1 = {
    'c1':1,
    'c2':2,
    'l1': [0, 1, 2],
}

print("D1 antes do shallow copy: ", d1)

d2 = d1.copy() #copia tudo menos mutaveis(lista por exemplo)
print("Depois do shallow copy e alterado o l1 de d2(também o d1 será alterado)")
d2['c1'] = 1000
d2['l1'][1] = 999999

print("d1: ",d1)
print("d2: ",d2)

import copy #copia profunda(tudo)

d2 = copy.deepcopy(d1)

d2['l1'][1] = 1
print("Depois do deep copy e alterado o l1 de d2")
print("d1: ", d1)
print("d2: ",d2)
