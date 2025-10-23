from os import system
system("cls")

def linhas():
    print("")
    print("-" * 100)
    print("")


linhas()
animais = ["Cachorro", "Gato", "Pinguim"]
print(f"Lista original: {animais}")
animais.append("Leão")
print(f"Lista atualizada: {animais}")

#################################----         PAISES         ----##############################################
linhas()

paises = ["Estados Unidos", "Japão", "Chile", "Russia", "Argentina"]
print(f"Lista original: {paises}")
paises.insert(1, "Brasil")
print(f"Lista atualizada: {paises}")

#################################----        TAMANHO         ----##############################################
linhas()

numeros = [5, 10, 15, 20, 25]
print(f"Tamanho da lista original: {len(numeros)}")
numeros.append(30)
print(f"Tamanho da lista atualizada: {len(numeros)}")

#################################----         NOMES         ----##############################################
linhas()

nomes = ["Kenneth", "João", "Pedro", "Maria", "Lucas", "Julia"]
print(f"Lista original: {nomes}")
del(nomes[2])
print(f"Lista atualizada: {nomes}")

#################################----        COMPRAS         ----##############################################
linhas()

compras = []

compras.append("Maçã")
compras.append("Pão")
compras.append("Arroz")
compras.insert(0, "Feijão")
print(f"Lista original: {compras}")
print(f"Tamanho da lista: {len(compras)}")
print(f"Item removido: {compras[1]}")
del(compras[1])
print(f"Lista atualizada: {compras}")

#################################----         FIM         ----##############################################
linhas()
