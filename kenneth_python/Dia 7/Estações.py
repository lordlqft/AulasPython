from os import system
system("cls")

estacao = input("Digite uma estação do ano:\n- ").lower()

match estacao:
    case 'verão':
        print("Utilize roupas leves, está no melhor momento para ir à praia!")
    case 'inverno':
        print("É recomendável roupas quentes para te aquecer.")
    case 'outono':
        print("É recomendável roupas confortáveis de tons neutros.")
    case 'primavera':
        print("É recomendável roupas leves e confortávei")
    case _:
        ("Você não inseriu uma estação do ano.")
