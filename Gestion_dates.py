import json

def gestion_tools(nom_archivo="Herramientas.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}
    
def guardar_datos(datos, nom_archivo="Herramientas.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch, indent=4)
        print("Datos guardados correctamente.")
    except Exception as ex:
        print("Error al guardar:", ex)
