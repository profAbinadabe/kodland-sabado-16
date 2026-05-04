import random

caractere = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+$"

entrada_do_usuario = int(input("Digite o comprimento da senha."))

senha = ""

for i in range(entrada_do_usuario):
    senha_aleatoria = random.choice(caractere)
    senha = senha + senha_aleatoria

print(f"A senha gerada é: {senha}")