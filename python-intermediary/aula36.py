# Yield from

def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print("ACABOU GEN1")

def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')

def gen2(gen):
    print('COMECOU GEN2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')

gl = gen2(gen1)
g2 = gen2(gen3)
for numero in gl:
    print(numero)
for numero in g2:
    print(numero)
