from os import system
system("cls")

n1 = int(input("Digite o primeiro número:\n- "))
n2 = int(input("Digite o segundo número:\n- "))
operador = input("Digite um operador (+; -, /, *)\n- ")

match operador:
    case '+':
        print(f"A soma de {n1} {operador} {n2} é {n1 + n2}")
    case '-':
        print(f"A diferença de {n1} {operador} {n2} é {n1 - n2}")
    case '/':
        print(f"A divisão de {n1} {operador} {n2} é {n1 / n2:.2f}")
    case '*':
        print(f"A multiplicação de {n1} {operador} {n2} é {n1 * n2}")
    case _:
        print(f"Operador ({operador}) inválido.")