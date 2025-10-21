from os import system
system("cls")

frase = input("Digite uma frase para retirar as vogais: ")
nova_frase = ""
vogais = "aeiouAEIOU"

for i in frase:
    if i not in vogais:
        nova_frase = nova_frase + i

print(f"Sua frase sem vogais é: \"{nova_frase}\"")