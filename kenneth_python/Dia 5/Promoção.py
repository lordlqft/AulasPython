from os import system
system("cls")

dia = input("Digite o dia da semana: ").lower()
fim_de_semana = dia == "sábado" or dia == "domingo"

print(f"É fim de semana? {fim_de_semana}")