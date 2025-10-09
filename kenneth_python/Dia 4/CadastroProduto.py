from os import system
system("cls")

produto = input("Informe o nome do produto: ")
preco = float(input("Informe o preço do produto: "))
quantidade_estoque = int(input("Informe a quantidade que há no estoque: "))
system("cls")

print(f"Produto: {produto}\nPreço: {preco}\nQuantidade: {quantidade_estoque}")