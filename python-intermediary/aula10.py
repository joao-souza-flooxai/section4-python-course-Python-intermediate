

def multiplicar(multiplicador):
    def multiplicacao(numero):
        return numero * multiplicador
    return multiplicacao

duplicar = multiplicar(2)
triplicar = multiplicar(3)

print(duplicar(10))
print(triplicar(10))