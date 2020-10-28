#Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
def Vogal(X):
    if X ==  'a' or X ==  'e' or X ==  'i' or X ==  'o' or X ==  'u':
        return True
    else:
        return False





X = str(input("Digite uma letra "))

print(Vogal(X))
