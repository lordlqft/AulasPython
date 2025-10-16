import random
from os import system
system("cls")

nota = random.randint(0,10)
print(f"Sua nota é {nota}!")
match nota:
    case 10:
        print("Excelente!")
    case 9 | 8:
        print("Ótimo!")
    case 7 | 6:
        print("Bom!")
    case 5 | 4 | 3 | 2 | 1:
        print("Precisa melhorar...")
    case _:
        print("Caractere inválido.")
