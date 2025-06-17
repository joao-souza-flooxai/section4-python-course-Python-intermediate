#Positional-only Parameters (/) - Tudo antesda barra deve
# ser ! APENAS ! posicional.
#Keyword-Only . Arguments . (*) - * sozinho ! NÃO SUGA ! valores.

def soma(a, b, /, x, y):
    print(a + b + x +y)

soma(1, 2, 3, y=3)

def soma2(a, b, *, c):
    print(a +b+c)

soma2(1, 2, c=3)