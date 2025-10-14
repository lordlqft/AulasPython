from os import system
system("cls")

numero = int(input("Digite o número para ser verificado: "))

if numero % 2 == 0:
    print(f"{numero} é par.")
else:
    print(f"{numero} é impar.")