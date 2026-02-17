def mostrar_logs():
    archivo = "logs/eventos.log"
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
            if not lineas:
                print("No hay registros aún.")
                return
            print("\n=== REPORTE DE EVENTOS ===")
            for linea in lineas:
                print(linea.strip())
            print("==========================\n")
    except FileNotFoundError:
        print("No se ha generado ningún log todavía.")