from os import system
system("cls")

palavra = input("Digite a palavra para imprimir-lá invertida: ")
invertida = ""

for i in palavra:
    invertida = i + invertida

print(invertida)