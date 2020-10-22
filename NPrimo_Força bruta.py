N = (int(input("Digite um número inteiro: ")))

cont = 0
sucesso = 0
while cont < 1000:
    cont = cont + 1
    if N % cont == 0:
        sucesso = sucesso + 1

if sucesso > 2:
    print ("não primo")
else:
    print("primo")