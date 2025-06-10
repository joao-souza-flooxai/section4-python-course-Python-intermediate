# Existe o escopo global e local.

# O escopo global é o escopo onde todo o código é alcançável.
# O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

x = 1 #

def escopo():
    global x
    x = 10 #mesmo x de fora por causa do global
    def outra_funcao():
        x = 20 #x diferente, x do escopo outra_funcao
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

escopo()
