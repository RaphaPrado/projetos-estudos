# Crie um codigo que conta o numero de vogais de um bloco de texto
# qualquer. O codigo de desconsiderar letras maiusculas/minusculas, 
# isto eh, "a" e "A" contam da mesma forma.
# O texto pode ser colado diretamente como um string no codigo.

texto = "O meu nome eh Raphael e eu gosto de programar em Python. Python eh uma linguagem de programacao muito legal."

vogais = "aeiou"
contador = 0

for letra in texto.lower():
    if letra in vogais:
        contador += 1

print(f"O número de vogais no texto é: {contador}")
