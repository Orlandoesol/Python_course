def mostrar_menu():
    print("""
    Gestor de Tareas
    1. Agregar tarea
    2. Ver tareas
    3. Marcar tarea como completada
    4. Eliminar tarea
    5. Guardar tareas en archivo
    6. Salir
    """)

def agregar_tarea(tareas):
    nombre = input("Nombre de la tarea: ")
    tareas.append({"nombre": nombre, "completada": False})
    print("Tarea agregada.")

def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            estado = "[x]" if tarea["completada"] else "[ ]"
            print(f"{i}. {estado} {tarea['nombre']}")

def marcar_completada(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("Número de tarea a marcar como completada: ")) - 1
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    except (IndexError, ValueError):
        print("Selección inválida.")

def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1
        tareas.pop(indice)
        print("Tarea eliminada.")
    except (IndexError, ValueError):
        print("Selección inválida.")

def guardar_en_archivo(tareas, archivo="tareas.txt"):
    """Guarda las tareas en un archivo de texto."""
    with open(archivo, "w") as f:
        for tarea in tareas:
            estado = "x" if tarea["completada"] else " "
            f.write(f"[{estado}] {tarea['nombre']}\n")
    print("Tareas guardadas en el archivo.")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            guardar_en_archivo(tareas)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
