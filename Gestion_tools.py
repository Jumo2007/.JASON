def agregar_Tools(datos, id, categoria, stock, valor, estado = None):
    if id in datos:
        print("Ya existe una herramienta con ese ID, por favor, intentelo nuevamente")
        return

    datos[id] = {
        "categoria": categoria,
        "stock": stock,
        "valor": valor,
        "estado": estado
                }
    print("Herramienta agregado exitosamente")

def modificar_Tools(datos, id, campo, n_valor):
    if id not in datos:
        print("La herramienta no existe, por favor, intentelo nuevamente")
        return
    if campo not in datos[id]:
        print("Campo Invalido")
        return
    
    datos[id][campo] = n_valor
    print(f"Herramienta {id} actualizada correctamente.")

def listar_tools(datos):
    if not datos:
        print("No hay herramientas registradas por el momento.")
        return

    for id, info in datos.items():
        print(f"\nID: {id}")
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





    

