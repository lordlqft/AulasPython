from os import system
system("cls")

frase = input("Digite uma frase para contar as consoantes: ").lower()
vogais = "aeiou"
consoantes = "bcdfghjklmnpqrstvwxyz"
quantidade_consoantes = 0
quantidade_vogais = 0

for i in frase:
    if i in consoantes:
        quantidade_consoantes += 1
    if i in vogais:
        quantidade_vogais += 1
print(f"Na sua frase há {quantidade_consoantes} consoantes e {quantidade_vogais} vogais.")