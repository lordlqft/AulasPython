from os import system
system("cls")

numero = int(input("Encontrar múltiplos de qual número?\n->"))

print(f"\nMúltiplos de {numero} entre 1 e 100:")
for i in range(1, 101):
    if i % numero == 0:
        print(i)