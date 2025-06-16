# Criando arquivos com Python
# Usamos a funçao open parar abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r.(leitura), w (escrita), x (para criação)
# a (escreve ao final), b(binário)
# t (modo texto), +(leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
#· seek . (move o cursor)
#.readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os. remove ou unlink - apaga o arquivo
# os. rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json. dump .= Gera um arquivo json
# json.load

caminho_arquivo = 'D:\\T.I\\workspace\\clear\\Curso_Python_Clear\\Modulo 4\\python-intermediary\\'
caminho_arquivo += 'aula64-arquivo-criado-com-codigo.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo:
    print(f'Aberto:\n')
    arquivo.write('Começando a escrever neste arquivo...\n')
    arquivo.write('Outra linha no arquivo...\n')
    arquivo.writelines(
        ('Outra linha, mas escrita no mesmo comando.\n',
         'Linha, linha.\n' 
        )
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(),end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    
    print()
    
    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())
    
    print()

print('#' * 10,end='\n\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
    print('Seu arquivo será fechado.\n')
  
