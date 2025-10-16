from os import system
system("cls")
import random

posicao = random.randint(1, 10)
print(f"Sua posição foi: {posicao}º lugar")

match posicao:
    case 1:
        print("Medalha de Ouro!")
    case 2:
        print("Medalha de Prata!")
    case 3:
        print("Medalha de Bronze...")
    case _:
        print("Sem medalha desta vez...")