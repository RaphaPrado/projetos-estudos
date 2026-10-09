# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder 
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar 
# ao usuario "Qual a capital do Estado X?", e checar se o usuario 
# respondeu de forma correta. Apos cada pergunta, o usuario pode escolher
# parar o jogo ou continuar para a proxima pergunta. Quando o usuario
# decidir parar, ou quando todas as perguntas forem respondidas, 
# o codigo mostra o numero bruto e porcentagem de acertos.

estados = [
    {"nome": "Acre", "capital": "Rio Branco"},
    {"nome": "Alagoas", "capital": "Maceio"},
    {"nome": "Amapa", "capital": "Macapa"},
    {"nome": "Amazonas", "capital": "Manaus"},
    {"nome": "Bahia", "capital": "Salvador"},
    {"nome": "Ceara", "capital": "Fortaleza"},
    {"nome": "Espirito Santo", "capital": "Vitoria"},
    {"nome": "Goias", "capital": "Goiania"},
    {"nome": "Maranhao", "capital": "Sao Luis"},
    {"nome": "Mato Grosso", "capital": "Cuiaba"},
    {"nome": "Mato Grosso do Sul", "capital": "Campo Grande"},
    {"nome": "Minas Gerais", "capital": "Belo Horizonte"},
    {"nome": "Para", "capital": "Belem"},
    {"nome": "Paraiba", "capital": "Joao Pessoa"},
    {"nome": "Parana", "capital": "Curitiba"},
    {"nome": "Pernambuco", "capital": "Recife"},
    {"nome": "Piaui", "capital": "Teresina"},
    {"nome": "Rio de Janeiro", "capital": "Rio de Janeiro"},
    {"nome": "Rio Grande do Norte", "capital": "Natal"},
    {"nome": "Rio Grande do Sul", "capital": "Porto Alegre"},
    {"nome": "Rondonia", "capital": "Porto Velho"},
    {"nome": "Roraima", "capital": "Boa Vista"},
    {"nome": "Santa Catarina", "capital": "Florianopolis"},
    {"nome": "Sao Paulo", "capital": "Sao Paulo"},
    {"nome": "Sergipe", "capital": "Aracaju"},
    {"nome": "Tocantins", "capital": "Palmas"}
]

cont = 0

for estado in estados:
    resposta = input(f"Qual a capital do Estado {estado['nome']}? ")
    if resposta.lower() == estado['capital'].lower():
        print("Resposta correta!")
        cont += 1
    else:
        print(f"Resposta incorreta! A capital de {estado['nome']} é {estado['capital']}.")

    continuar = input("Deseja continuar para a próxima pergunta? (s/n) ")
    if continuar.lower() != 's':
        break

print(f"Você acertou {cont} de {len(estados)} perguntas.")
print(f"Porcentagem de acertos: {cont/len(estados)*100:.2f}%")