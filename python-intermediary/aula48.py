def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, *args):
    #Cria uma nova função que já traz determinados parâmetros junto
    def nova_funcao(outros_arg):
        return funcao(*args, outros_arg)
    return nova_funcao


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)


valor1 = int(input("Informe o primeiro número para somar com 5: "))
print(soma_com_cinco(valor1))

valor2 = int(input("Informe o segundo número para multiplicar por dez: "))
print(multiplica_por_dez(valor2))
