recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
['2021-05-01', "15:00", "No trabajar"],
['2021-07-15', "13:00", "No hacer nada es feriado"],
['2021-09-18', "16:00", "Ramadas"],
['2021-12-25', "00:00", "Navidad"]]

#Elimina el evento del día del trabajo
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])

# Agrega evento el 2 de Febrero de 2021
recordatorios.insert(1, ['2021-02-02', "06:00", "Empezar el Año"])

# Edita el evento del 15 de Julio para que sea el 16 de Julio
recordatorios[2][0] = '2021-07-16'

# Agrega cenas de Navidad y de Año Nuevo
recordatorios.insert(-1,['2021-12-25', "22:00", "Cena de Navidad"])
recordatorios.append(['2022-01-01', "22:00", "Cena de Año Nuevo"])




# Output
print(recordatorios)
