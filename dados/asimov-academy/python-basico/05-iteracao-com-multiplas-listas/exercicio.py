# Dado duas listas, printe todos os valores que aparecem
# duplicados nas duas listas.

# Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou nao.

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comum = False


for valor in lista1: 
    if valor in lista2:
        comum = True
        print(f"O valor {valor} aparece nas duas listas.")

if comum:
    print("Existe algum elemento em comum entre as duas listas.")
else:
    print("Não existe nenhum elemento em comum entre as duas listas.")
