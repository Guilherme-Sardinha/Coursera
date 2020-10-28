#Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def Maior(X, Y):
    if X > Y:
        return X
    else:
        return Y

X = int(input("Digite o primeiro número "))
Y = int(input("Digite o segundo número "))

print(Maior(X, Y))