from os import system
system("cls")

valor_compra = float(input("Digite o valor da compra: R$ "))
valor_final = valor_compra

if valor_compra > 500:
    desconto = valor_compra * 0.15
    valor_final = valor_compra - desconto
    print(f"Você recebeu um desconto de 15%! (R$ {desconto:.2f})")
elif valor_compra >= 200 and valor_compra <= 500:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Você recebeu um de sconto de 10%! (R$ {desconto:.2f})")
else:
    print("As compras feitas com valor abaixo de R$200,00 não recebem descontos.")

print(f"O valor final a pagar é {valor_final}.")