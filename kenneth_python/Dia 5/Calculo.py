from os import system
import time
system("cls")

while True:  # Re-run program
    # main program
    system("cls")
    teste = int(input("Qual é o resultado de 12 x 5?\n-| "))


    if teste == 60:
        print("Acertou!")
        time.sleep(2)
        break
    elif teste > 60:
        print("Quase, é um número menor...")
        time.sleep(1)
    elif teste < 60:
        print("Quase, é um número maior...")
        time.sleep(1)
        while True:  # Validate user input
            answer = input('Tentar novamente? (s/n): ')
            if answer in ('s', 'n'):
                break
                print("invalid input.")

            if answer == 's':
                
                continue
            else:
                break

    

    