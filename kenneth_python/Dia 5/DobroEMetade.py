from os import system
import random
system("cls")

numero = random.randint(2, 20)
dobro = numero * 2
metade = numero / 2

print(f"Número: {numero}\nMetade do número: {metade}\nDobro do número: {dobro}")