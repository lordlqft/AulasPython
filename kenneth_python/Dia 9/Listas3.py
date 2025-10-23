from os import system
system("cls")

def linhas():
    print("")
    print("-" * 100)
    print("")

#################################----        NOTAS         ----##############################################
linhas()

notas = [5.0, 10.0, 7.5, 9.5, 8.0]
soma_notas = 0.0

for i in notas:
    soma_notas = soma_notas + i

print(f"Notas: {notas}")
print(f"Soma das notas: {soma_notas}")

#################################----        NOTAS         ----##############################################
linhas()

convidados = ["Duda", "Rafaela", "Pedro", "Lucas", "Pietro"]
print(f"Lista original: {convidados}")
convidados.insert(0, "João")
print(f"Lista com novo convidado: {convidados}")
convidados.sort()
print(f"Lista atualizada: {convidados}")

#################################----        EQUIPE         ----##############################################
linhas()

equipe = ["Kenneth", "João", "Pedro", "Cavani", "Davi", "Douglas"]
print(f"Equipe: {equipe}")
titulares = equipe[:3]
reservas = equipe[3:]
print(f"Titulares: {titulares}")
print(f"Reservas: {reservas}")

#################################----        TAREFAS         ----##############################################
linhas()

tarefas = ["Limpar a casa", "Passear com o cachorro", "Programar em Python", "Estudar para a prova", "Desenhar"]
print(f"Tarefas iniciais: {tarefas}")
del(tarefas[1])
print(f"Tarefas após remoção: {tarefas}")
del tarefas[-1]
print(f"Tarefas atualizadas: {tarefas}")

#################################----        NÚMEROS         ----##############################################
linhas()

numeros = [41, 20, 52, 120, 64, 107, 84, 33]
print(f"Números: {numeros}")
print(f"Menor número: {min(numeros)}")
print(f"Maior número: {max(numeros)}")
numeros.sort()
print(f"Lista em ordem crescente: {numeros}")

#################################----        MÉDIA         ----##############################################
linhas()

notas_alunos = []
soma = 0.0

for i in range(4):
    i = float(input("Digite a nota do aluno: "))
    notas_alunos.append(i)

for i in notas_alunos:
    soma += i

media = soma / len(notas_alunos)

print(f"As notas dos alunos são: {notas_alunos}")
print(f"Soma das notas: {soma}")
print(f"Média das notas: {media}")

