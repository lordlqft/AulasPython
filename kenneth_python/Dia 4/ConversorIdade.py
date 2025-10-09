from os import system
system("cls")

idade = int(input("Informe a sua idade: "))

DIAS = 365
MESES = 12
HORAS = 24

idade_meses = idade * MESES
idade_dias = idade * DIAS
idade_horas = idade * HORAS

system("cls")

print(f"Sua idade em diferentes períodos:\nSua idade em meses é: {idade_meses}\nSua idade em dias é: {idade_dias}\nSua idade em horas é: {idade_horas}.")
