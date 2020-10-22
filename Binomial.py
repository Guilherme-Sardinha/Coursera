def fatorial (N):
    fatorial = 1
    while N > 0:
        fatorial = fatorial * N
        N = N - 1
    return fatorial


N = int(input("digite o valor N: "))
K = int(input("digite o valor de K: "))
M = N - K
Bi= (fatorial(N))/fatorial(K)*(fatorial(M))
print(Bi)
