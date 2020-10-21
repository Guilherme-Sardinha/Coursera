valor = int(input("Digite um valor "))
cont = len(str(valor))
mostra = 0
mostra2 = 0
cont2 = 0
while 0 != cont:
    cont = cont - 1
    mostra = valor
    mostra = valor % 10
    mostra2 = valor
    mostra2 = (valor // 10) % 10
    valor = valor // 10
    if mostra == mostra2:
        cont2 = cont2 + 1
if cont2 >= 1:
    print("és")