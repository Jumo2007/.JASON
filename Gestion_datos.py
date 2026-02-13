
import json

def gestion_herramientas(nom_archivo="Herramientas.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}
    
def guardar_datos(datos, nom_archivo="Herramientas.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch)
    except Exception as ex:
        datos = {}