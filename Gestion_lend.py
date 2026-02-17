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




def devolver_prestamo(prestamos, herramientas, id_prestamo):

    if id_prestamo not in prestamos:
        print("El préstamo no existe.")
        return

    prestamo = prestamos[id_prestamo]

    if prestamo["estado"] != "activo":
        print("El préstamo no está activo.")
        return

    herramientas[prestamo["herramienta"]]["stock"] += prestamo["cantidad"]
    prestamo["estado"] = "devuelto"

    print("Préstamo devuelto correctamente.")



def historial_usuario(prestamos, id_usuario):

    print(f"\n=== HISTORIAL DEL USUARIO {id_usuario} ===")

    encontrado = False

    for id_prestamo, info in prestamos.items():
        if info["usuario"] == id_usuario:
            encontrado = True
            print(f"Préstamo: {id_prestamo} | Estado: {info['estado']}")

    if not encontrado:
        print("Este usuario no tiene préstamos.")
