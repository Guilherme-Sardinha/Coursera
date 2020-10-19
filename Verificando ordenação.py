#Receba 3 números inteiros na entrada e imprima
#crescente
#se eles forem dados em ordem crescente. Caso contrário, imprima
#não está em ordem crescente

N1 = int(input("Digite o primeiro número "))
N2 = int(input("Digite o segundo número "))
N3 = int(input("Digite o terceiro número "))

if N1 < N2 and N2 < N3:
    print("crescente")
else:
    print("não está na ordem crescente")