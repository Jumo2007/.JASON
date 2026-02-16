
from Gestion_user import agregar_user, eliminar_user, mostrar_users
from Gestion_dates import guardar_datos
def menu_usuarios(usuarios):

    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Eliminar usuario")
        print("4. Volver")

        op = input("Seleccione: ")

        if op == "1":
            C_C = input("ID: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")

            agregar_user(usuarios, C_C, nombre, edad)
            guardar_datos(usuarios, "Usuarios.json")

        elif op == "2":
            mostrar_users(usuarios)

        elif op == "3":
            C_C = input("ID a eliminar: ")
            eliminar_user(usuarios, C_C)
            guardar_datos(usuarios, "Usuarios.json")

        elif op == "4":
            break

        else:
            print("Opción inválida.")