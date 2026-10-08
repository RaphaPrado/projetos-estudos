# Desafio 2 - crie um programa que:
# - Pede por um nome de usuario e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrario, exibe uma mensagem de erro. A mensagem eh diferente
# quando o usuario esta incorreto, e quando a senha esta incorreta.
# - O usuario/senha "corretos" podem ser definidos como 
# variaveis dentro do proprio codigo.

usuarioCorreto = "raphuzin"
senhaCorreta = int(123456)

usuario = input("Digite seu usuario: ")
senha = int(input("Digite sua senha: "))

if usuarioCorreto == usuario:
    if senha == senhaCorreta:
        print(f"Acesso liberado, seja bem vindo {usuario}!")
    else:
        print(f"Senha incorreta para o usuario: {usuario}")

else:
    print(f"Usuario: {usuario} nao cadastrado no sistema!")


