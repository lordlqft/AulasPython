from os import system
system("cls")

letra = input("Digite uma letra para ser verificada: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"A letra {letra} é Vogal.")
else:
    print(f"A letra {letra} é Consoante.")