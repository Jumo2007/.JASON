from Gestion_tools import agregar_Tools, listar_tools, eliminar_Tool, modificar_tool
from Gestion_dates import  guardar_datos

def menu_herramientas(herramientas):

    while True:
        print("\n--- Gestión de Herramientas ---")
        print("1. Agregar herramienta")
        print("2. Listar herramientas")
        print("3. Eliminar herramienta")
        print("4. Modificar herramienta")
        print("5. Volver")

        op = input("Seleccione: ")

        if op == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            stock = int(input("Stock: "))
            valor = input("Valor: ")

            agregar_Tools(herramientas, id, nombre, categoria, stock, valor, "disponible")
            guardar_datos(herramientas, "Herramientas.json")

        elif op == "2":
            listar_tools(herramientas)

        elif op == "3":
            id = input("ID a eliminar: ")
            eliminar_Tool(herramientas, id)
            guardar_datos(herramientas, "Herramientas.json")

        elif op == "4":
            id_herramienta = input("Ingrese el ID de la herramienta a modificar: ")
            modificar_tool(herramientas, id_herramienta)
            guardar_datos(herramientas, "Herramientas.json")  

        elif op == "5":
            print("Volviendo al menú anterior...")
            break

        else:
            print("Opción inválida.")

