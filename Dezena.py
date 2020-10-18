N = int(input("Digite o número "))

Centena = N / 100

Dezena = int( (N % 100)/10)

Unidade = (N % 100) % 10
 
print("O dígito das dezenas é", Dezena)
