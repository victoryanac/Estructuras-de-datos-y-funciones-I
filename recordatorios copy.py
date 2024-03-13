recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

print("Antes de modificar:", recordatorios)

# 1. Agrega evento el 2 de Febrero de 2021
recordatorios.insert(1, ['2021-02-02', "06:00", "Empezar el Año"])

# Verificar la lista después de agregar el evento
print("Después de agregar el evento de febrero:", recordatorios)

# 2. Edita el evento del 15 de Julio para que sea el 16 de Julio
recordatorios[3][0] = '2021-07-16'  # Actualizado para reflejar el cambio en el índice después de insertar en febrero

# Verificar la lista después de editar el evento de julio
print("Después de editar el evento de julio:", recordatorios)

# 3. Elimina el evento del día del trabajo
recordatorios.remove(['2021-05-01', "15:00", "No trabajar"])

# Verificar la lista después de eliminar el evento de mayo
print("Después de eliminar el evento de mayo:", recordatorios)

# 4. Agrega cenas de Navidad y de Año Nuevo
recordatorios.append(['2021-12-25', "22:00", "Cena de Navidad"])
recordatorios.append(['2022-01-01', "22:00", "Cena de Año Nuevo"])

# Verificar la lista después de agregar las cenas
print("Final:", recordatorios)
