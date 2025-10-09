from os import system
system("cls")

nome = input("Informe seu nome: ")
idade = int(input("Sua idade: "))
salario = float(input("Seu salário: "))
status = bool(input("Status de login (True/False): "))

system("cls")
print(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nStatus de login: {status}")
