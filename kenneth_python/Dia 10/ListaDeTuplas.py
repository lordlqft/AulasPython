from os import system
system("cls")

alunos = [("Kenneth", 10.0), ("Rafaela", 8.5), ("Mariana", 4.5), ("João Vitor", 8.0), ("Pedro", 3.5)]

print("Parabens a todos os alunos abaixo:")
for i, v in alunos:
    if v >= 7.0:
        print(f"{i}, sua nota foi: {v}")
print("Os demais abaixo devem melhorar!...")
for i, v in alunos:
    if v < 7.0:
        print(f"{i}: {v}")
