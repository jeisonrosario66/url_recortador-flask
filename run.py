import os

from db.init_db import db_create


def clearWindow():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        pass


clearWindow()

while True:

    def menuView():
        print("\t\t.:Acortador de URLs - Docker:.\n")
        print(
            """
            -Opciones
            1.) Compose up
            2.) Correr container
            3.) Verificar Base de datos
            4.) Crear Base de datos
            5.) Eliminar Base de datos
            0.) Salir\n"""
        )

    menuView()
    try:
        opc = int(input("ingrese una opcion: "))
    except ValueError:
        clearWindow()
        menuView()
        opc = int(input("ingrese una opcion (en base 10) : "))

    if opc == 0:
        print("exit()")
        break
    elif opc == 1:
        clearWindow()
        try:
            dataBase = open("db/database.db")
            print("La base de datos existe")
            dataBase.close()
            print("Ejecutando 'docker compose up'")
            os.system("docker compose up")
            break
        except FileNotFoundError:
            print("La base de datos no existe, antes ejecute la opcion 4")
    elif opc == 2:
        clearWindow()
        print("Ejecutando 'docker build -t flask_docker_app .'")
        os.system("docker build -t flask_docker_app .")
        break
    elif opc == 3:
        # Comprueba que exista la base de datos
        clearWindow()
        try:
            dataBase = open("db/database.db")
            print("La base de datos ya existe")
            dataBase.close()
        except FileNotFoundError:
            print("La base de datos no existe, ejecute la opcion 4")
    elif opc == 4:
        clearWindow()
        try:
            dataBase = open("db/database.db")
            print("La base de datos ya existe")
            dataBase.close()
        except FileNotFoundError:
            print("Ejecutando 'python init_db.py'")
            db_create()
            if os.name == "posix":
                os.system("mv database.db db/")
            elif os.name == "nt":
                os.system("move database.py db/")
            print(":.Base de datos creada 'db/database.db'.;")
    elif opc == 5:
        clearWindow()
        print("Eliminar base de datos, ¿esta seguro?")
        opc2 = str(input("Esta accion es irreversible [y],[n]: ")).lower()
        if opc2 == "y":
            if os.name == "posix":
                os.system("rm db/database.db")
                print("Base de datos eliminada")
            elif os.name == "nt":
                os.system("del db/database.db")
        else:
            print("Ninguna acción realizada")
