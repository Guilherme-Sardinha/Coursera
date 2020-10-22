#verifica se existem dois digitos repetidos
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
    #deixei a variavel 'mostra2' um passo a frente para realizar a comparação entre os digitos
    mostra2 = (valor // 10) % 10
    valor = valor // 10
    #coloquei um segundo contador para contar o número de vezes que um digito se repetia
    if mostra == mostra2:
        cont2 = cont2 + 1
if cont2 >= 1 and cont != 1:
    print("sim")
else:
    print("não")