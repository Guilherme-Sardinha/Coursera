#FizzBuzz parcial, parte 2
#Receba um número inteiro na entrada e imprima
#Buzz
#se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

N1 = int(input("Digite o número "))

if N1 % 5 == 0:
    print("Buzz")
else:
    print(N1)