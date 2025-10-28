from os import system
system("cls")

contato = {
    "nome": "Rafaela",
    "telefone": "16 99757-6643"
}
tem_email = "email" in contato
print(f"O contato de {contato['nome']} tem email?\n-{tem_email}")