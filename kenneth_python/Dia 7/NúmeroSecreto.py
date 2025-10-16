import random
import time
from os import system
system("cls")

numeros_tentados = []

numero_secreto = random.randint(10000, 50000)
tentativa = int(input("Tente adivinhar o número secreto:\n- "))
tentativas = 1
while tentativa != numero_secreto:
    if tentativa > numero_secreto:
        numeros_tentados.append(tentativa)
        system("cls")
        print(f"Tentativas: {numeros_tentados}")
        print("Número incorreto.")
        print(f"Número adivinhado: {tentativa}")
        print(" ")
        time.sleep(1)
        print("É um número menor.")
        time.sleep(1)
        tentativa = int(input("Tente adivinhar novamente o número secreto:\n- "))
        tentativas += 1
    else:
        numeros_tentados.append(tentativa)
        system("cls")
        print(f"Tentativas: {numeros_tentados}")
        print("Número incorreto.")
        print(f"Número adivinhado: {tentativa}")
        print(" ")
        time.sleep(1)
        print("É um número maior.")
        time.sleep(1)
        tentativa = int(input("Tente adivinhar novamente o número secreto:\n- "))
        tentativas += 1
system("cls")
print("Parabens! Você acertou o número secreto")
print(f"Você acertou em {len(numeros_tentados)} vezes" )