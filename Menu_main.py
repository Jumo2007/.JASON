from Menu_Admin import menu_admin
from Menu_User import menu_user
from Gestion_dates import gestion_tools


def login():
    print("=== BIENVENIDO A LA EL SISTEMA, QUERIDO USUARIO ===")
    print("Seleccione su rol:")
    print("1. Administrador")
    print("2. Usuario")

    opcion = input("Ingrese el número correspondiente a su rol: ")

    if opcion == "1":
        clave_a = input("Ingrese la contraseña de administrador: ")

        if clave_a == "YBA":
            print("Acceso concedido como administrador.")  
            return "admin"
        else:
            print("Contraseña incorrecta.")
            return None

    elif opcion == "2":
        print("Acceso concedido como usuario.")
        return "user"

    else:
        print("Opción inválida.")
        return None


def main():
    usuarios = gestion_tools("Usuarios.json")
    herramientas = gestion_tools("Herramientas.json")
    prestamos = gestion_tools("Prestamos.json")


    while True:
        rol = login()

        if rol == "admin":
            menu_admin()
        elif rol == "user":
            menu_user(usuarios, herramientas, prestamos)
        else:
            print("Intentelo nuevamente.\n")

if __name__ == "__main__":
    main()
