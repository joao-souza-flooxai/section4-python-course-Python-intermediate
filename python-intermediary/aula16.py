# Exercicio - sistema de perguntas e respostas

def pegarPergunta(pergunta_texto):
    def pergunta(opcao):
        for p in perguntas:
            if p['Pergunta'] == pergunta_texto:
                if opcao == p['Resposta']:
                    return True
                else:
                    return None
        return None
    return pergunta

def formatAnwser(anwser):
    if anwser is None:
        print("Resposta incorreta!")
        return 0
    print("Resposta correta!")
    return 1


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '1', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '6', '7'],
        'Resposta': '5',
    }
]

chamada = {
    0 : pegarPergunta('Quanto é 2+2?'),
    1 : pegarPergunta('Quanto é 5*5?'),
    2 : pegarPergunta('Quanto é 10/2?'),
}
acertos =0


for index, pergunta in enumerate(perguntas):
    print(pergunta['Pergunta'])
    for opcao in pergunta['Opcoes']:
        print(f"- {opcao}")
    resposta = input("Sua resposta: ")
    acertos += formatAnwser(chamada[index](resposta))
    
print(f"Você acertou: {acertos}/{len(perguntas)}")
