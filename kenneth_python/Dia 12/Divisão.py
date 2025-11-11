from os import system
system("cls")

quanitdade_pessoas = input("Quantas pessoas estão na sala?\n-> ")

try:
    numero_pessoas = int(quanitdade_pessoas)
    resultado = 100 / numero_pessoas
    print(f"Cada pessoa recebe {resultado:.2f} partes.")
except:
    print(f"Não é possivel dividir por 0 pessoas!")