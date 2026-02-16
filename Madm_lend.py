from Gestion_lend import crear_prestamo, listar_prestamos
from Gestion_dates import guardar_datos

print("SE ESTÁ CARGANDO MADM_LEND")

def menu_prestamos(prestamos, usuarios, herramientas):

    while True:
        print("\n--- Gestión de Préstamos ---")
        print("1. Crear préstamo")
        print("2. Listar préstamos")
        print("3. Volver")

        op = input("Seleccione: ")

        if op == "1":
            id_prestamo = input("ID préstamo: ")
            id_usuario = input("ID usuario: ")
            id_herramienta = input("ID herramienta: ")
            cantidad = int(input("Cantidad: "))
            fecha_inicio = input("Fecha inicio: ")
            fecha_devolucion = input("Fecha devolución: ")
            observaciones = input("Observaciones: ")

            crear_prestamo(
                prestamos, usuarios, herramientas,
                id_prestamo, id_usuario,
                id_herramienta, cantidad,
                fecha_inicio, fecha_devolucion,
                observaciones
            )

            guardar_datos(prestamos, "Prestamos.json")
            guardar_datos(herramientas, "Herramientas.json")

        elif op == "2":
            listar_prestamos(prestamos)

        elif op == "3":
            break

        else:
            print("Opción inválida.")

print("Archivo Madm_lend cargado correctamente")
