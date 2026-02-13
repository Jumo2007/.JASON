Clave_a = [1098]

def login():
    print("=== INICIO DE SESIÓN ===")
    rol = input("Ingrese su rol (admin/user): ").lower()

    if rol == "admin":
        clave = input("Ingrese la clave de administrador: ")
        if clave == Clave_a:
            print("Acceso concedido como administrador.\n")
            return "admin"
        else:
            print("Clave incorrecta.")
            return None

    elif rol == "user":
        print("Accedio como usuario.\n")
        return "user"

    else:
        print("Rol inválido.")
        return None
