def mostrar_reportes(herramientas, prestamos):
    print("\n** REPORTES **")

    print("\n--- Herramientas con stock bajo (<5) ---")
    encontrado = False

    for id_h, datos in herramientas.items():
        if datos["stock"] < 5:
            print(f"{datos['nombre']} (ID: {id_h}) | Stock: {datos['stock']}")
            encontrado = True

    if not encontrado:
        print("No hay herramientas con stock bajo.")


