def agregar_tarea(tareas, descripcion, fecha_limite, prioridad):
    tarea = {"descripcion": descripcion, "fecha_limite": fecha_limite, "prioridad": prioridad}
    tareas.append(tarea)

def mostrar_tareas(tareas):
    for idx, tarea in enumerate(tareas, start=1):
        print("Tarea", idx, ":", tarea)

tareas = []

while True:
    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_limite = input("Ingrese la fecha límite de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea: ")
        agregar_tarea(tareas, descripcion, fecha_limite, prioridad)
    elif opcion == "2":
        if tareas:
            print("\nLista de tareas:")
            mostrar_tareas(tareas)
        else:
            print("\nNo hay tareas registradas.")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
