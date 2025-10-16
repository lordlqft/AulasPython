from os import system
system("cls")

tabuada = int(input("Digite um número para verificar a tabuada:\n- "))
multiplicador = 1
print(f"Tabuada do {tabuada}:\n")

while multiplicador <= 10:
    print(f"{tabuada} x {multiplicador} = {tabuada * multiplicador};")
    multiplicador += 1