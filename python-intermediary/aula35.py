
# Introdução aos Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1  # Pausar
    print('Continuando...')
    yield 2  # Pausar
    print('Mais uma...')
    yield 3
    print('Vou terminar')
    return 'ACABOU'

gen = generator(n=0)
for n in gen:
    print(n)
