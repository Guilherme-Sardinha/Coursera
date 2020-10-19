Segundos = int(input("Digite o valor em segundos "))

Dias = Segundos // 86400

Resto = Segundos % 86400

Horas = Resto // 3600

Resto = Segundos % 3600

Min = Resto // 60

Final = Resto % 60

print(Dias, "dias,", Horas, "horas,", Min, "minutos e", Final, "segundos.")
