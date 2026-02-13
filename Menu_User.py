
def menu_user():
    while True:
        print("\n=== MENÚ USUARIO ===")
        print("1. Consultar herramientas")
        print("2. Solicitar préstamo")
        print("3. Ver mis préstamos")
        print("4. Salir")
        print("-------------------------")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Mostrando herramientas...")
        elif opcion == "2":
            print("Creando solicitud...")
        elif opcion == "3":
            print("Mostrando préstamos...")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
