from os import system
system("cls")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso / altura ** 2
print(f"Imc: {IMC}\n")

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
else:
    print("Obesidade")