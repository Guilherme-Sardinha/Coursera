#Recebe um número e exibe seu fatorial
N = int(input("Digite o valor de n: "))
fatorial = 1
while N > 0:
    fatorial = fatorial * N
    N = N - 1
print(fatorial)
