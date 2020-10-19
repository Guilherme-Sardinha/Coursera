import math

a = float(input("Digite o valor de A "))
b = float(input("Digite o valor de B "))
c = float(input("Digite o valor de C "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = ((-b + math.sqrt(delta))) / (2 * a)
    print("só existe uma raiz e seu valor é: ", raiz1 )
else:
    if delta < 10:
        print("não existem raizes reais")
    else:
        raiz1 = ((-b + math.sqrt(delta))) / (2 * a)
        raiz2 = ((-b - math.sqrt(delta))) / (2 * a)
        print("1° raiz = ", raiz1)
        print("2° raiz = ", raiz2)
