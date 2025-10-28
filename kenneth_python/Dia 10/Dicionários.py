import time
from os import system
system("cls")

livro = {
    "titulo": "Quarto de Despejo",
    "autor": "Carolina Maria de Jesus",
    "ano": 1960
}

livro["gênero"] = "Autobiografia"

print(f"Informações do livro:\n\n{livro}")
time.sleep(1)
system("cls")
print(f"Nome do(a) autor(a): {livro['autor']}")
time.sleep(1)
system("cls")
