# Crie um codigo que implenta a "Cifra de Cesar", isto eh, que
# transforma um string movendo cada letra um certo numero de 
# passos no alfabeto. O numero de passos eh dado por uma chave.
# Letra com acentos, espacos e pontuacao permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCD" com chave 2 = "CDEF"
# "Cachorro" com chave -1 = "Bzbgqqnq"
# "Ola, Mundo!" com chave 3 = "Roc, Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minusculas e outra para as letras maiusculas, e use este
# string para guiar as substituicoes.

texto = input("Digite o texto a ser cifrado: ")
chave = int(input("Digite a chave (numero de passos): "))

minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for caractere in texto:
    if caractere in minusculas:
        indice = minusculas.index(caractere)
        novo_indice = (indice + chave) % 26
        print(minusculas[novo_indice], end="")
    elif caractere in maiusculas:
        indice = maiusculas.index(caractere)
        novo_indice = (indice + chave) % 26
        print(maiusculas[novo_indice], end="")
    else:
        print(caractere, end="")

