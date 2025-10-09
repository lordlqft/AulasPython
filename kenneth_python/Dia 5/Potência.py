from os import system
system("cls")

base = int(input("Digite um número base:\n ->"))
expoente = int(input("Digite um número expoente:\n ->"))
potencia = base ** expoente

system("cls")
print(f"A potência do seus números são:\n-> {potencia}")