try:
    a=18
    b=0
    c = a / b
    print(b[0])

    print('Linha 1')
    c = a / b
    print('Linha 2')
    print('ERRO DESCONHECIDO.')

except ZeroDivisionError as e:
    print('Dividiu por zero.', e)
except NameError:
    print('Nome não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:"', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')


print('CONTINUAR')
