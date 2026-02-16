from Gestion_tools import listar_tools
from Gestion_lend import crear_prestamo, historial_usuario
from Gestion_dates import guardar_datos

def menu_user(usuarios, herramientas, prestamos,):
    print("DEBUG: parámetros recibidos correctamente")
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
            listar_tools(herramientas)
        elif opcion == "2":
            print("Creando solicitud...")
            id_prestamo = input("ID préstamo: ")
            id_usuario = input("ID usuario: ")
            id_herramienta = input("ID herramienta: ")
            cantidad = int(input("Cantidad: "))
            fecha_inicio = input("Fecha inicio: ")
            fecha_devolucion = input("Fecha devolución: ")
            observaciones = input("Observaciones: ")

            crear_prestamo(
                prestamos,
                usuarios,
                herramientas,
                id_prestamo,
                id_usuario,
                id_herramienta,
                cantidad,
                fecha_inicio,
                fecha_devolucion,
                observaciones
            )
        elif opcion == "3":
            id_usuario = input("Ingrese su ID ")
            historial_usuario(prestamos, id_usuario)

            print("Mostrando préstamos...")
            
        elif opcion == "4":
            print("..........")
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
