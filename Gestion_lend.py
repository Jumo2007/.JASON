def crear_prestamo(prestamos, usuarios, herramientas, id_prestamo,
                   id_usuario, id_herramienta,
                   cantidad, fecha_inicio,
                   fecha_devolucion, observaciones):

    if id_prestamo in prestamos:
        print("El préstamo ya existe.")
        return

    if id_usuario not in usuarios:
        print("El usuario no existe.")
        return

    if id_herramienta not in herramientas:
        print("La herramienta no existe.")
        return

    if herramientas[id_herramienta]["stock"] < cantidad:
        print("No hay suficiente stock.")
        return


    herramientas[id_herramienta]["stock"] -= cantidad

    prestamos[id_prestamo] = {
        "usuario": id_usuario,
        "herramienta": id_herramienta,
        "cantidad": cantidad,
        "fecha_inicio": fecha_inicio,
        "fecha_devolucion": fecha_devolucion,
        "estado": "activo",
        "observaciones": observaciones
    }

    print("Préstamo creado correctamente.")


def listar_prestamos(prestamos):

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    for id_prestamo, info in prestamos.items():
        print(f"\nID Préstamo: {id_prestamo}")
        print(f"Usuario: {info['usuario']}")
        print(f"Herramienta: {info['herramienta']}")
        print(f"Cantidad: {info['cantidad']}")
        print(f"Fecha inicio: {info['fecha_inicio']}")
        print(f"Fecha devolución: {info['fecha_devolucion']}")
        print(f"Estado: {info['estado']}")
        print(f"Observaciones: {info['observaciones']}")
        print("-" * 30)


def act_ven(prestamos):

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    print("\n=== PRÉSTAMOS ACTIVOS ===")
    hay_activos = False

    for id_prestamo, info in prestamos.items():
        if info["estado"] == "activo":
            hay_activos = True
            print(f"\nID: {id_prestamo}")
            print(f"Usuario: {info['usuario']}")
            print(f"Herramienta: {info['herramienta']}")
            print(f"Cantidad: {info['cantidad']}")
            print(f"Fecha devolución: {info['fecha_devolucion']}")
            print("-" * 25)

    if not hay_activos:
        print("No hay préstamos activos.")

    print("\n=== PRÉSTAMOS VENCIDOS ===")
    hay_vencidos = False

    for id_prestamo, info in prestamos.items():
        if info["estado"] == "vencido":
            hay_vencidos = True
            print(f"\nID: {id_prestamo}")
            print(f"Usuario: {info['usuario']}")
            print(f"Herramienta: {info['herramienta']}")
            print(f"Cantidad: {info['cantidad']}")
            print(f"Fecha devolución: {info['fecha_devolucion']}")
            print("-" * 25)

    if not hay_vencidos:
        print("No hay préstamos vencidos.")



