from os import system
system("cls")

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
cidade = input("Informe sua cidade: ")
system("cls")

print("\t---- Perfil do usuário ----")
print(f"{nome}, {idade} - {cidade}")