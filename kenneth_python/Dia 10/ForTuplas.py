from os import system
import time
system("cls")

nomes = ("Kenneth", "Rafaela", "Mariana", "João", "Pedro")

for i in nomes:
    print(f"Saudações, {i}!")
    time.sleep(1)
print("Sejam todos bem vindos!")