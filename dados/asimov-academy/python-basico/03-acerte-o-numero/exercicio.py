# Desafio 3 - crie um programa que: 
# - Escolhe um numero secreto.
# - Pede por um chute do usuario.
# - Indica se o usuario acertou ou nao.
# - Se nao acertou, da uma dica, dizendo
#   - se o numero eh mais alto ou mais baixo.
# - Repete isso ate 3 vezes

import random

numeroSecreto = random.randint(1, 100)
cont = int(3)

while cont != 0:
    palpite = int(input(f"Chute um numero de 1 a 100: "))
    cont-=1

    if palpite == numeroSecreto:
        print(f"Acertou o numero era {numeroSecreto}!")
        break
    elif palpite < numeroSecreto:
        print(f"O numero eh maior que {palpite}, restam {cont} tentativas!")
    else:
        print(f"O numero eh menor que {palpite}, restam {cont} tentativas!")

else:
    print(f"Suas tentativas acabaram! O número era {numeroSecreto}.")