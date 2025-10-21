from os import system
system("cls")

#Caso queiramos ver a tabuada de 1 a 10
# podemos optar pela estrutura abaixo
numero = int(input("Informe a tabuada que deseja ver: "))

for i in range(11):
    print(f"{numero} x {i} = {(numero * i):02d}")
