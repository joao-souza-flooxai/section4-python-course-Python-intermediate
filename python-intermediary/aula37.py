try:
    a=18
    b=0
    c = a / b
    print(b[0])

    print('Linha 1')
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
