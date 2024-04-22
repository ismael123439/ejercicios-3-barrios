def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

frase = "Esta es una frase de ejemplo"
print("Número de palabras:", contar_palabras(frase))
