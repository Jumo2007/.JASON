def mostrar_reportes(herramientas, prestamos):
    print("\n** REPORTES **")

    # 🔹 Stock bajo
    print("\n--- Herramientas con stock bajo (<5) ---")
    encontrado = False

    for id_h, datos in herramientas.items():
        if datos["stock"] < 5:
            print(f"{datos['nombre']} (ID: {id_h}) | Stock: {datos['stock']}")
            encontrado = True

    if not encontrado:
        print("No hay herramientas con stock bajo.")

    print("\n--- Herramientas más solicitadas ---")

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    contador = {}

    for prestamo in prestamos.values():
        herramienta_id = prestamo["herramienta"]
        cantidad = prestamo["cantidad"]

        if herramienta_id in contador:
            contador[herramienta_id] += cantidad
        else:
            contador[herramienta_id] = cantidad

    ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    for herramienta_id, total in ordenadas:
        nombre = herramientas[herramienta_id]["nombre"]
        print(f"{nombre} | Total solicitado: {total}")

