#Recebe um numero e mostra a quantidade de impares
N = int(input("Digite o valor de n: "))
cont = 0
while N >= 1:
    if cont % 2 != 0:
        N = N - 1
        print(cont)
    cont = cont + 1