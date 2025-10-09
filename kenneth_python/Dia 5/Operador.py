from os import system
import random
system("cls")

a = random.randint(1, 30)
b = random.randint(1, 30)
c = random.randint(1, 30)
d = random.randint(1, 30)

print(f"Primeira soma: a + b = {a} + {b} = {a + b}")
print(f"Segunda soma: c + d = {c} + {d} = {c + d}\n")

A = a + b
B = c + d
if A > B:
    print(f"A soma de a + b é maior que a soma de c + b ({A}, {B})")
    print(A > B)
else:
    print(f"A soma de a + b é menor que a soma de c + b ({A}, {B})")
    print(F"({A < B})")