# Crie um codigo que simula um baralho de cartas.
# O codigo deve conter as seguintes funcoes:

# gerar_baralho() -> retorna um baralho novo. Parametros da funcao
# definem quantas copias retornar (1 baralho, 2 baralhos, ...), 
# se o baralho deve conter coringas, e se deve ser embaralhado 
# antes de ser retornado.

#  mostrar_baralho() -> exeibe a quantidade de cartas no baralho e 
# mostra quais sao.

# dar_as_cartas() -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mao de 
# cada jogador e mostra quais sao.

# A partir dessas funcoes, o codigo deve: 
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho apos as cartas terem sido distribuidas 
# - exibir a mao de cada jogador

# DICA: utilize os simbolos ♠♥♦♣ para representar os naipes.
# DICA: utilize o simbolo 🃏 para representar o coringa.
# DICA: utilize a funcao random.shuffle() para embaralhar o baralho.

import random

def gerar_baralho(copias=1, coringas=False, embaralhar=False):
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = []

    for _ in range(copias):
        for naipe in naipes:
            for valor in valores:
                baralho.append(f"{valor}{naipe}")
        if coringas:
            baralho.append('🃏')
            baralho.append('🃏')

    if embaralhar:
        random.shuffle(baralho)

    return baralho

def mostrar_baralho(baralho):
    print(f"Quantidade de cartas no baralho: {len(baralho)}")
    print("Cartas no baralho:")
    print(", ".join(baralho))

def dar_as_cartas(baralho, num_jogadores, cartas_por_jogador):
    jogadores = {f"Jogador {i+1}": [] for i in range(num_jogadores)}
    for i in range(cartas_por_jogador):
        for jogador in jogadores:
            if baralho:
                jogadores[jogador].append(baralho.pop(0))
            else:
                print("Não há cartas suficientes no baralho para distribuir.")
                return jogadores
    return jogadores

def mostrar_jogadores(jogadores):
    for jogador, cartas in jogadores.items():
        print(f"{jogador} tem {len(cartas)} cartas: {', '.join(cartas)}")

# Exemplo de uso das funções
baralho = gerar_baralho(copias=1, coringas=True, embaralhar=True)
mostrar_baralho(baralho)
jogadores = dar_as_cartas(baralho, num_jogadores=4, cartas_por_jogador=5)
mostrar_baralho(baralho)
mostrar_jogadores(jogadores)
