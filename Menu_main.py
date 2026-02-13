from Menu_Admin import menu_admin
from Menu_User import menu_user
from Gestion_Rol import login


def main():
    while True:
        rol = login()

        if rol == "admin":
            menu_admin()
        elif rol == "user":
            menu_user()
        else:
            print("Intentelo nuevamente.\n")

if __name__ == "__main__":
    main()
