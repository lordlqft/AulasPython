from os import system
system("cls")

entrada = input("Digite um usuário: ")

try:
    numero = int(entrada)
    print(f"O número {numero} é inteiro!")
except:
    print("O número é invalido. (NotInteger)")