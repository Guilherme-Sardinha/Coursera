#Recebe um valor inteiro e lê separadamente o número de cada casa
valor = int(input("Digite um valor "))
cont = len(str(valor))
mostra = 0
while 0 != cont:
    cont = cont - 1
    mostra = valor
    mostra = valor % 10
    print(mostra)
    valor = valor // 10
