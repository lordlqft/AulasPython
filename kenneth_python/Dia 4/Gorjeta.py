from os import system
system("cls")

conta = float(input("Conta do restaurante: "))
gorjeta = int(input("Porcentagem da gorjeta (ex.: 10, 15, 20, 30..): "))
system("cls")

valor_gorjeta = conta * (gorjeta / 100)
valor_total = conta + valor_gorjeta
print(f"\tConta do Restaurante:\nConta total: {conta}\nGorjeta: {gorjeta}\nValor total a pagar: R${valor_total:.2f}")