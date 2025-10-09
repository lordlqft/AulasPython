from os import system
system("cls")

peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

imc = peso / (altura * altura)

print(imc)