from os import system
system("cls")

valor = int(input("Valor desejado a sacar: "))

if valor > 0 and (valor % 10) == 0:
    print(f"Saque do valor {valor},00 realizado com sucesso")
else:
    print("Erro: Valor desejado para sacar não é múltiplo de 10.")