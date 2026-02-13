from Gestion_user import agregar_user, modificar_user, eliminar_user, mostrar_users

from Gestion_tools import agregar_Tools, modificar_tool, listar_tools, eliminar_Tool

from Gestion_lend import crear_prestamo, listar_prestamos, act_ven

def menu_admin():
    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Herramientas")
        print("3. Gestionar Préstamos")
        print("4. Ver Reportes")
        print("5. Salir")
        print("------------------------------")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Entrando a gestión de usuarios...")
        
        elif opcion == "2":
            print("Entrando a gestión de herramientas...")
        elif opcion == "3":
            print("Entrando a gestión de préstamos...")
        elif opcion == "4":
            print("Mostrando reportes...")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
