from Logs import log_info
def agregar_Tools(datos, id, nombre, categoria, stock, valor, estado = None):
    if id in datos:
        print("Ya existe una herramienta con ese ID, por favor, intentelo nuevamente")
        return

    datos[id] = {
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "valor": valor,
        "estado": estado
                }
    print("Herramienta agregado exitosamente")
    return

def modificar_tool(datos, id_herramienta):
    if id_herramienta not in datos:
        print("La herramienta no existe.")
        return

    print("\nCampos disponibles para actualizar:")
    print("1. nombre")
    print("2. categoria")
    print("3. stock")
    print("4. valor")
    print("5. estado")

    opcion = input("Seleccione el campo a modificar: ")

    campos = {
        "1": "nombre",
        "2": "categoria",
        "3": "stock",
        "4": "valor",
        "5": "estado"
    }

    if opcion not in campos:
        print("Opción inválida.")
        return

    campo = campos[opcion]
    nuevo_valor = input("Ingrese el nuevo valor: ")

    if campo == "stock" or campo == "valor":
        try:
            nuevo_valor = int(nuevo_valor)
        except ValueError:
            print("Debe ingresar un número válido.")
            return

    datos[id_herramienta][campo] = nuevo_valor

    print(" Herramienta actualizada correctamente.")
    log_info(f"Herramienta modificada: {id}")




def listar_tools(datos):
    if not datos:
        print("No hay herramientas registradas por el momento.")
        return

    for id, info in datos.items():
        print(f"\nID: {id}")
        print(f"Nombre: {info['nombre']}")
        print(f"Categoría: {info['categoria']}")
        print(f"Stock: {info['stock']}")
        print(f"Valor: {info['valor']}")
        print(f"Estado: {info['estado']}")



def eliminar_Tool(datos, id):
    if id not in datos:
        print(f"La herramienta con id {id} no existe, intentelo nuevamente ")
        return
    
    del datos [id]
    print(f"Se ha eliminado la herramienta con id: {id} ")
    return

def herramientas_stock_bajo(datos, limite=2):

    print("\n=== HERRAMIENTAS CON STOCK BAJO ===")

    encontrado = False

    for id, info in datos.items():
        if info["stock"] <= limite:
            encontrado = True
            print(f"ID: {id} | Nombre: {info['nombre']} | Stock: {info['stock']}")

    if not encontrado:
        print("No hay herramientas con stock bajo.")






    

