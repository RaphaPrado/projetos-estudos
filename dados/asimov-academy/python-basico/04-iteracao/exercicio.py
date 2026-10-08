# Dado uma sequencia de numeros, calcule a soma e media dos numeros.
# ATENCAO: nao vale usar a funcao sum() !

# Dado uma sequencia de numeros, calcule o maior valor da sequencia.
# ATENCAO: nao vale usar a funcao max() !

# Dado uma lista de palavras, printe todas as palavras 
# com pelo menos 5 caracteres.

seq = [10, 30, -8, 0, -2, 4]

soma = 0 
for valor in seq:
    soma += valor

media = soma / len(seq)

print(f"A soma dos valores da sequencia é: {soma}")
print(f"A media dos valores da sequencia é: {media:.2f}")

# -----------------------------------------------------

maior = 0
for valor in seq:
    if valor > maior:
        maior = valor

print(f"O maior valor da sequencia é: {maior}")

# ------------------------------------------------------

palavras = ["casa", "carro", "bicicleta", "avião", "computador", "livro"]

for palavra in palavras:
    if len(palavra) >= 5:
        print(f"A palavra '{palavra}' tem pelo menos 5 caracteres.")
