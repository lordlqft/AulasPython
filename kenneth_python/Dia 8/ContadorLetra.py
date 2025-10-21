from os import system
system("cls")

frase = input("Digite uma frase:\n->").lower()
letra = input("Qual letra você quer contar?\n->").lower()
contador = 0

for i in frase:
    if i == letra:
        contador += 1
print()
print(f"A letra \"{letra}\" aparece {contador} vezes na frase.")
