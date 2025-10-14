from os import system
system("cls")

numero = int(input("Digite um número para ser verificado: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")