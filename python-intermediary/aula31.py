# Mutáveis
lista = []
dicionario = {}
conjunto = set()

# Imutáveis
tupla = ()
string = ""
inteiro = 0
flutuante = 0.0
falso = False
intervalo = range(0, 1)
nada = None  # Correção aqui

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE: {falsy("TESTE")}')
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
