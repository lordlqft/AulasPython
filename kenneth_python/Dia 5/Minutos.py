from os import system
import random
system("cls")

minutos = random.randint(1, 240)
horas = minutos // 60
minutos_restantes = horas % 60

print(f"Minutos: {minutos}\nHoras: {horas}h\nMinutos restantes: {minutos_restantes}min")

