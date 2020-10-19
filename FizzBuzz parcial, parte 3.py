#FizzBuzz parcial, parte 3
#Receba um número inteiro na entrada e imprima
#FizzBuzz
#na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

N1 = int(input("Digite o número "))

if N1 % 5 == 0 and N1 % 3 == 0:
    print("FizzBuzz")
else:
    print(N1)