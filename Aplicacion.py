def mostrar_menu():
    print("Menú Opciones")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Has seleccionado la opción Registrar.")
            # Aquí puedes agregar la lógica para la opción Registrar
        elif opcion == "2":
            print("Has seleccionado la opción Eliminar.")
            # Aquí puedes agregar la lógica para la opción Eliminar
        elif opcion == "3":
            print("Has seleccionado la opción Editar.")
            # Aquí puedes agregar la lógica para la opción Editar
        elif opcion == "4":
            print("Has seleccionado la opción Listar.")
            # Aquí puedes agregar la lógica para la opción Listar
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

if __name__ == "__main__":
    main()
