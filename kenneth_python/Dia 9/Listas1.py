from os import system
system("cls")

def linhas():
    print("-" * 100, "\n")



linhas()
frutas = ["pera", "banana", "uva", "laranja", "maçã"]
print(frutas)

frutas[2] = "manga"
print(frutas, "\n")
linhas()

#################################----         DIAS         ----##############################################

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
dias.append("Domingo (descanso)")


print(dias, "\n")
linhas()

#################################----         NOTAS         ----##############################################

numeros = [1, 5, 8, 18, 21, 41, 67, 69, 76]
numeros[0] = 100
numeros[7] = 200

print(numeros, "\n")
linhas()

#################################----        NÚMEROS        ----##############################################

notas = [5.0, 7.5, 4.0, 10.0]
notas[2] = 10.0

print(notas, "\n")
linhas()

#################################----         CORES         ----##############################################

cores = ["Vermelho", "Azul", "Roxo", "Verde"]
cores[1] = "Preto"
cores[3] = "Branco"

print(cores, "\n")
linhas()

#################################----         FIM         ----##############################################