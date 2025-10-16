import time 
from os import system
system("cls")
soma = 0
numero = int(input("Digite um número (ou 0 para parar)\n- "))
while numero != 0:
    system("cls")
    print(f"Soma: {soma}")
    soma = numero + soma
    time.sleep(0.4)
    numero = int(input("Digite um número (ou 0 para parar)\n- "))
system("cls")
print(f"A soma total dos digitos foi: {soma}.")

