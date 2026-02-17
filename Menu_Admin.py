from Gestion_dates import gestion_tools

def menu_admin():

    usuarios = gestion_tools("Usuarios.json")
    herramientas = gestion_tools("Herramientas.json")
    prestamos = gestion_tools("Prestamos.json")

    while True:
        print("=== MENÚ ADMINISTRADOR ===")
        print("1. Usuarios")
        print("2. Herramientas")
        print("3. Préstamos")
        print("4. Reportes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            from Madm_user import menu_usuarios
            menu_usuarios(usuarios)

        elif opcion == "2":
            from Madm_tool import menu_herramientas
            menu_herramientas(herramientas)

        elif opcion == "3":
            from Madm_lend import menu_prestamos
            menu_prestamos(prestamos, usuarios, herramientas)

        elif opcion == "4":
            from reports import mostrar_reportes
            mostrar_reportes(herramientas, prestamos)

        elif opcion == "5":
            from reports import mostrar_reportes
            mostrar_reportes(herramientas, prestamos)

        elif opcion == "6":
            print("Saliendo del menú administrador...")
            break

        else:
            print("Opción inválida.")
