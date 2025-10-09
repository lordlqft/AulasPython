from os import system
system("cls")

PI = 3.14159

raio = float(input("Informe o raio de um círculo: "))

area = PI * (raio * raio)
system("cls")

print(f"A área de um circulo com raio {raio} é {area:.2f}")