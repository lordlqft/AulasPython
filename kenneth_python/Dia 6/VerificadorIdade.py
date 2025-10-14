from os import system
system("cls")

idade = int(input("Qual é a sua idade?\n-> "))

if idade >= 18:
    print("Ingresso para o filme de terror liberado.")
else:
    print("Você ainda não tem a idade necessária.")