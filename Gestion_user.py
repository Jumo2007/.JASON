def agregar_user(datos, C_C, nombre, edad):

    if C_C in datos:
        print("El usuario ya existe.")
        return

    datos[C_C] = {
        "nombre": nombre,
        "edad": edad
    }

    print("Usuario agregado correctamente.")


def modificar_user(datos, C_C, campo, nuevo_valor):

    if C_C not in datos:
        print("El usuario no existe.")
        return

    if campo not in datos[C_C]:
        print("Campo inválido.")
        return

    datos[C_C][campo] = nuevo_valor
    print("Usuario modificado correctamente.")


def eliminar_user(datos, C_C):
    if C_C not in datos:
        print(f"El usuario :{C_C} ; no existe. ")
        return
    
    del datos [C_C]
    print(f"El camper id {C_C} eliminado.")

def mostrar_users(datos):

    if not datos:
        print("No hay usuarios registrados.")
        return

    for C_C, info in datos.items():
        print(f"ID: {C_C}")
        print(f"Nombre: {info['nombre']}")
        print(f"Edad: {info['edad']}")
        print("-" * 20)
