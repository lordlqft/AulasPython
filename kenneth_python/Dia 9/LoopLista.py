from os import system
system("cls")

compras = []
item = ""
print("Digite o nome dos items para adicionar-los à lista, \"sair\" para terminar a lista.")
while item.lower() != "sair":
    item = input("Adicionar items:\n-> ")

    if item.lower() != "sair":
        compras.append(item)
        system("cls")
        print(f"Lista de compras: {compras}\n")
        print("Digite o nome dos items para adicionar-los à lista, \"sair\" para terminar a lista.")
    else:
        system("cls")
        break
compras.sort()
print(f"Lista de compras: {compras}")