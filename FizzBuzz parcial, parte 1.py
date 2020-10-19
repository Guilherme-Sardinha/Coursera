# FizzBuzz parcial, parte 1
#Receba um número inteiro na entrada e imprima
#Fizz
#se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

N1 = int(input("Digite o número "))

if N1 % 3 == 0:
    print("Fizz")
else:
    print(N1)