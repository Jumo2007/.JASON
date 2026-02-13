from Menu_Admin import menu_admin

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Administrador")
        print("2. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_admin()

        elif opcion == "2":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

        
