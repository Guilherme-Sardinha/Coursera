import math

a = float(input("Digite o valor de A "))
b = float(input("Digite o valor de B "))
c = float(input("Digite o valor de C "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = ((-b + math.sqrt(delta))) / (2 * a)
    print("A raiz deta equação é", raiz1 )
else:
    if delta < 10:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = ((-b + math.sqrt(delta))) / (2 * a)
        raiz2 = ((-b - math.sqrt(delta))) / (2 * a)
        if raiz1 < raiz2:
            print("1° raiz = ", raiz1, raiz2)
        else:
            print("1° raiz = ", raiz2, raiz1)
