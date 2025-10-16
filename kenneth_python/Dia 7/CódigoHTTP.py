import random
import time
from os import system
system("cls")

codigo = random.randint(200, 500)

match codigo:
    case 200:
        print("Sucesso!")
    case 404:
        print("Não encontrado...")
    case 500:
        print("Erro no servidor.")
    case _:
        if codigo >= 200 and codigo <= 299:
            print(f"Status: Código de sucesso ({codigo})")
        elif codigo >= 400 and codigo <= 499:
            print(f"Status: Erro do cliente ({codigo})")
        else:
            print(f"Código desconhecido ({codigo})")
time.sleep(5)