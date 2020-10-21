#Soma os digitos
valor = int(input("Digite um valor "))
cont = len(str(valor))
mostra = 0
acum = 0
while 0 != cont:
    cont = cont - 1
    mostra = valor
    mostra = valor % 10
    valor = valor // 10
    acum=acum + mostra
print(acum)