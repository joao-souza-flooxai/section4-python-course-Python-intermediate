# Closure e funções que retornam outras funções

# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome}!'
#     return saudar

# s1 = criar_saudacao('Bom dia', 'João')
# s2 = criar_saudacao('Boa noite', 'João')

# print(s1())
# print(s2())


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))