#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função


def Maior_primo(X):
    cont = 0
    sucesso = 0
    while cont < 1000:
        cont = cont + 1
        if X % cont == 0:
            sucesso = sucesso + 1
        if sucesso > 2 and cont == 1000 :
            cont = 0
            X = X - 1
            sucesso = 0
        elif sucesso <= 2 and cont == 1000 :
            return X
            cont = 1000


