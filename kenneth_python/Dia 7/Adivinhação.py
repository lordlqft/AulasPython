import random
import time
from os import system
system("cls")

numero = random.randint(1, 10)

tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    tentativa = int(input("Tente adivinhar o número que a máquina pensou:\n- "))

    if tentativa == numero:
        system("cls")
        print("Parabéns, você acertou o número que a máquina pensou!")
        print(f"Tentativas: {tentativas}")
        break
    else:
        system("cls")
        print("Errado! tente novamente.")
        tentativas += 1
if tentativas == limite_tentativas:
    system("cls")
    print("Você atingiu o limite de tentativas.")
