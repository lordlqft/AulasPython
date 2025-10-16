from os import system
system("cls")

opcao = input("|Escolha um comando:\n|\t1. Entrar\n|\t2. Sair\n|\t3. Ajuda\n\n|-> ").lower()

match opcao:
    case "entrar":
        print("Seja bem-vindo ao nosso sistema!")
    case "sair":
        print("Volte logo!")
    case "ajuda":
        print("Olá, com o que eu poderia ajudá-lo?")
    case _:
        print("Informação inválida.")

