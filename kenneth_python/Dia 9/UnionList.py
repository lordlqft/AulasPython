from os import system
system("cls")

vegetais = ["Alface", "Couve", "Brócolis"]
frutas = ["Maçã", "Tomate", "Pera", "Uvas"]

feira = vegetais + frutas
feira.sort()
print(f"A feira de hoje é:\n{feira}")