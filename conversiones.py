import sys

#ingresos de datos del usuario
tasa_sol = float(sys.argv[1])
tasa_peso_argentino = float(sys.argv[2])
tasa_dolar_americano = float(sys.argv[3])

monto_chileno = float(sys.argv[4])

# Conversiones de divisas
conversion_sol = monto_chileno * tasa_sol
conversion_peso_argentino = monto_chileno * tasa_peso_argentino
conversion_dolar_americano = monto_chileno * tasa_dolar_americano


print(f"Los {monto_chileno} pesos equivalen a: {conversion_sol} soles, {conversion_peso_argentino} Pesos Argentinos, {conversion_dolar_americano} Dolares")
