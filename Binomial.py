def fatorial (N):
    fatorial = 1
    while N > 0:
        fatorial = fatorial * N
        N = N - 1
    return fatorial

#Criando uma função que irá realizar testes em meu código
def teste():
    if fatorial (0) == 1:
        print("certo 0")
    else:
        print("errado 0")
    if fatorial(1) == 1:
        print("Certo 1")
    else:
        print("errado 1")
    if fatorial(2) == 2:
        print("Certo 2")
    else:
        print("errado 2")
    if fatorial (3) == 6:
        print("certo 3")
    else:
        print("errado 3")
    if fatorial (5) == 120:
        print("certo 5")
    else:
        print("errado 5")


N = int(input("digite o valor N: "))
K = int(input("digite o valor de K: "))
M = N - K
Bi= (fatorial(N))/((fatorial(K))*(fatorial(M)))
print(Bi)
print(teste())