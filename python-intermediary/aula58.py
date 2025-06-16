from itertools import groupby

alunos =[ 
    {'nome': 'Luiz', 'nota' : 'A'},
   {'nome': 'Letícia', 'nota' : 'B'},
   {'nome': 'Fabrício', 'nota' : 'A'},
   {'nome': 'Rosemary', 'nota': 'C'},
   {'nome' : 'Joana' , 'nota' : 'D'},
   {'nome': 'João', 'nota' : 'A' },
   {'nome': 'Eduardo', 'nota': 'B'},
   {'nome': 'André' , 'nota' : 'A' },
   {'nome': 'Anderson', 'nota': 'C'},
]

def order(aluno):
    return aluno['nota']


# Ordenar pelo critério de agrupamento
alunos_agrupados = sorted(alunos, key=order)

# Agrupar pelo critério de agrupamento
grupos = groupby(alunos_agrupados, key=order)


for chave, grupo in grupos:
    print(f"Alunos com nota {chave}:")
    for aluno in grupo:
        print(aluno)
    print()
