# 1
informacion_personal = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Carlos", "edad": 22}
]

primer_diccionario = informacion_personal[0]
nombre_primera_persona = primer_diccionario["nombre"]
edad_segunda_persona = informacion_personal[1]["edad"]

print("Nombre 1:", nombre_primera_persona)
print("Edad 2", edad_segunda_persona)

# 1.2 Recorrer y mostrar k,v
for persona in informacion_personal:
    for clave, valor in persona.items():
        print(clave + ":", valor)
