#Distância entre dois pontos
#Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.
#Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
#longe
#na saída. Caso o contrário, quando a distância for menor que 10, imprima
#perto

import math

X1 = int(input("Digite o valor do eixo X do primeiro número "))
Y1 = int(input("Digite o valor do eixo Y do primeiro número "))

X2 = int(input("Digite o valor do eixo X do segundo número "))
Y2 = int(input("Digite o valor do eixo Y do segundo número "))

distancia = math.sqrt(((X1-X2)**2)+((Y1-Y2)**2))

if distancia >= 10:
    print("longe")
else:
    print("perto")