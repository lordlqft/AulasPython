from os import system
import time
system("cls")


print("Seja bem vindo à festa de aniversário do Kenneth!\n\nPor questões de segurança, precisamos que verifique\nseu nome na entrada da festa, e digite seu nome abaixo.")
convidados = []

for i in range(30):
    nome = input("\n- Nome: ")

    if nome.lower() != "12345":
        system("cls")
        print("Processando...")
        time.sleep(1)
        system("cls")
        convidados.append(nome)
        print("Seja bem vindo à festa de aniversário do Kenneth!\n\nPor questões de segurança, precisamos que verifique\nseu nome na entrada da festa, e digite seu nome abaixo.")
        print(f"Convidados: {len(convidados)}")
    else:
        system("cls")
        break
convidados.sort()
system("cls")
print("Você (Administrador) optou por encerrar o sistema de verificação de entrada, ou os 30 convidados já foram verificados.\n")
print(f"Total de convidados: {len(convidados)}\n{convidados}")