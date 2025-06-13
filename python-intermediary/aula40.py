def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')

def deve_ser_int_ou_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float.'
        )

    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)


print(divide(8, 0))