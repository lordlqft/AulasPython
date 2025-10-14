from os import system
system("cls")

print("\t\tMenu de Opções\t\t")
print("1. Ver Saldo")
print("2. Fazer Deposito")
print("3. Realizar Saque")
opcao = int(input("Digite o número da opção desejada"))

if opcao == 1:
    print("Executando a opção: Ver Saldo...")
elif opcao == 2:
    print("Executando a opção: Fazer Depósito...")
elif opcao == 3:
    print("Executando a opção: Realizar Saque...")
else:
    print("Opção incorreta.")