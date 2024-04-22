def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

palabra = "reconocer"
print("¿Es palíndromo?", es_palindromo(palabra))
