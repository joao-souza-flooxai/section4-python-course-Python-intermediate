#Exercicio anterior mas com json


import os
import json

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

ARQUIVO = 'aula68.json'

def verificar_ou_criar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w', encoding='utf8') as f:
            json.dump({"tarefas": [], "desfeitos": []},
                       f, ensure_ascii=False, indent=2)


def carregar():
    verificar_ou_criar_arquivo()
    with open(ARQUIVO, 'r', encoding='utf8') as f:
        return json.load(f)


def salvar(tarefas=None, desfeitos=None):
    if tarefas is None or desfeitos is None:
        listar()
        return
    with open(ARQUIVO, 'w', encoding='utf8') as f:
        json.dump({"tarefas": tarefas, "desfeitos": desfeitos}, f, ensure_ascii=False, indent=2)


def listar():
    limpar_console()
    conteudo = carregar()
    tarefas = conteudo['tarefas']

    print("\nTAREFAS:\n")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

    print("")

def desfazer():
    conteudo = carregar()
    tarefas = conteudo['tarefas']
    desfeitos = conteudo['desfeitos']


    if not tarefas:
        print("Nada para desfazer.")
        return
    
    ultima = tarefas.pop()
    desfeitos.append(ultima)
    salvar(tarefas, desfeitos)
    print("Ação desfeita.")
    listar()


def refazer():
    conteudo = carregar()
    tarefas = conteudo['tarefas']
    desfeitos = conteudo['desfeitos']


    if not desfeitos:
        print("Nada para refazer.")
        return
    
    ultima = desfeitos.pop()
    tarefas.append(ultima)
    
    salvar(tarefas, desfeitos)
    print("Ação refeita.")
    listar()


def acrescentar(tarefa=None):
    if not tarefa:
        listar()
        return
    
    conteudo = carregar()
    tarefas = conteudo['tarefas']
    desfeitos = conteudo['desfeitos']
    desfeitos.clear()
    tarefas.append(tarefa)

    salvar(tarefas, desfeitos)
    listar()


sair = False

comandos = {
    'listar': listar, 
    'desfazer': desfazer, 
    'refazer': refazer, 
    'clear':   limpar_console
}

verificar_ou_criar_arquivo()

while not sair:
    print('Comandos: listar, desfazer, refazer, clear, ou "sair" para encerrar.')
    opcao = input('Informe um comando ou uma nova tarefa: ')

    if opcao == "":
        continue

    if opcao == "sair":
        sair = True
        print("Saindo.")
    elif opcao in comandos:
        comandos[opcao]()
    else:
        acrescentar(opcao)


print("Fim.")
