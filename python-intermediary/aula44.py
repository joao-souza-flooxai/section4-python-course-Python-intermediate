import aula44_m
import importlib as ib

print(aula44_m.variavel)

for i in range(10):
    ib.reload(aula44_m)
    print(i)

print('Fim')