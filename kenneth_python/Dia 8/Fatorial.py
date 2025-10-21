from os import system
system("cls")

numero = int(input("Digite um número para ser fatorado: "))
fatorial = 1

for i in range(numero, 0, -1):
    fatorial = fatorial * i

print(f"O fatorial de {numero} é {fatorial}")