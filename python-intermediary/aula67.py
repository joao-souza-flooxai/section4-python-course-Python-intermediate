import os
sair = False
tarefas = []
tarefas_desfeitas = []

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def listar(tarefas = None):
    if tarefas is None:
        tarefas = []
    limpar_console()
    print("\nTAREFAS:\n")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")
    print("")
    

def desfazer(tarefas, tarefas_desfeitas):
    if not tarefas:
        print("\nNão há nada para desfazer. \n\n")
        return
    limpar_console()
    ultima = tarefas.pop()
    tarefas_desfeitas.append(ultima)
    listar(tarefas)

def refazer(tarefas, tarefas_desfeitas):
    if not tarefas_desfeitas:
        print("\nNão há nada para refazer.\n\n")
        return
    limpar_console()
    ultima = tarefas_desfeitas.pop()
    tarefas.append(ultima)
    listar(tarefas)


comandos = {
    'listar':listar,
    'desfazer':desfazer,      
    'refazer':refazer
}

while not sair:
    print('Comandos: listar, desfazer, refazer.')
    digitou = input('Digite uma tarefa ou comando: \n')

    if digitou == 'sair':
        sair = True
        print("Saindo.")
        continue
    elif digitou in comandos:
        if digitou == "listar":
            comandos[digitou](tarefas)
            continue
        elif digitou == "desfazer":
            comandos[digitou](tarefas, tarefas_desfeitas)
            continue
        elif digitou == "refazer":
            comandos[digitou](tarefas, tarefas_desfeitas)
            continue
    elif digitou == "":
        print("Informe uma tarefa ou um comando.")
        continue
    else:
        tarefas.append(digitou)
        listar(tarefas)
        continue

print("Fim.")

    