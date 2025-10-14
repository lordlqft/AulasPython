from os import system
system("cls")

nota = float(input("Digite a nota do aluno: "))

if nota > 7.0:
    print("Passou!")
else:
    print("Reprovou...")