
# importa el documento txt y lo guarda en la variable "texto"
with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

# cuente los caracteres distintos
caracteres_distintos = len(set(texto))

# cuente las palabras distintas
palabras_distintas = len(set(texto.split(" ")))


print(f"El número de caracteres distintos es: {caracteres_distintos}")
print(f"El número de palabras distintas es: {palabras_distintas}")
