import time
from os import system
system("cls")

contagem = 10

while contagem >= 1:
    print(contagem)
    contagem -= 1
    time.sleep(0.4)
print("Fogo!")