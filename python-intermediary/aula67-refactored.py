#Exercicio refatorado usando meus conhecimentos, a aula e pesquisa.

import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar(tarefas=[]):
    limpar_console()

    print("\nTAREFAS:\n")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")
    print("")

def desfazer(tarefas=None, tarefas_desfeitas=None):

    if not tarefas:
        listar()
        return
    
    ultima = tarefas.pop()
    tarefas_desfeitas.append(ultima)
    print("Ação desfeita.")
    listar(tarefas)

def refazer(tarefas=None, tarefas_desfeitas=None):

    if not tarefas:
        listar()
    if not tarefas_desfeitas:
        listar(tarefas)
        return
    
    ultima = tarefas_desfeitas.pop()
    tarefas.append(ultima)
    print("Ação refeita.")
    listar(tarefas)


def adicionar(tarefa=None, tarefas=None):
    
    if not tarefa:
        listar()
    
    tarefas.append(tarefa)
    print(f"Tarefa acrescentada: {tarefa}")
    listar(tarefas)


sair = False
tarefas = []
tarefas_desfeitas = []

comandos = {
    'listar': lambda: listar(tarefas),
    'desfazer': lambda: desfazer(tarefas, tarefas_desfeitas),
    'refazer': lambda: refazer(tarefas, tarefas_desfeitas),
    'clear':   lambda: limpar_console()
}

while not sair:
    print('Comandos: listar, desfazer, refazer, clear, ou "sair" para encerrar.')
    opcao = input('Informe um comando ou uma nova tarefa: ').strip()

    if opcao == "":
        continue

    if opcao == "sair":
        sair = True
        print("Saindo.")

    elif opcao in comandos:
        comandos[opcao]()

    else:
        adicionar(opcao, tarefas)


print("Fim.")
