from os import system
system("cls")

letra = input("Digite uma letra para ser verificada: ").is

match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
         print("Vogal!")
    case 'b'|'c'|'d'|'f'|'g'|'h'|'j'|'k'|'l'|'m'|'n'|'p'|'q'|'r'|'s'|'t'|'v'|'w'|'x'|'y'|'z':
         print("Consoante!")
    case _:
         print("Caractere inválido")