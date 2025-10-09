from os import system
system("cls")

numero = int(input("Digite um número para verificar: "))

if numero >= 10 and numero >= 20:
    print(f"{numero} é maior que 10 e 20.")
elif numero >= 10 and numero <= 20:
    print(f"{numero} é maior que 10 e menor que 20.")
elif numero < 10:
    print(f"{numero} é menor que 10 e 20.")