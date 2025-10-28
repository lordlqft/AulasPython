from os import system
system("cls")

cadastro = {
    "nome": input("Digite seu nome:\n- "),
    "idade": int(input("Digite a sua idade:\n- ")),
    "cidade": input("Digite o nome da sua cidade:\n- ")
}
system("cls")
print(cadastro)