#Exemplo com o uso de sets

letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if '1' in letras:
        print('PARABENS!')
        break

    print(letras)