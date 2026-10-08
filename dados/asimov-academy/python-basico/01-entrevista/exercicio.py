# Desafio 1 - crie um programa que: 
# - Pede pelo seu nome e idade
# - Da oi para voce
# - Conta quantas letras seu nome possui 
# - Fala quantos anos voce tera daqui a 5 anos

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

print(f"Oi {nome}!")
print(f"Seu nome possui {len(nome)} letras.")
print(f"Daqui a 5 anos, você terá {idade + 5} anos.")
