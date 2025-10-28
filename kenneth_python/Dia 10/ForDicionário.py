from os import system
system("cls")

capitais = {
    "São Paulo": "São Paulo",
    "Rio de Janeiro": "Rio de Janeiro",
    "Bahia": "Salvador"
}

for estado, capital in capitais.items():
    print(f"A capital de {estado} é {capital}")
