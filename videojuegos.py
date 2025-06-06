# Código videojuegos con uso de listas y diccionarios.

import os, time

WAIT = 3

videojuegos = []

plataformas = ("PC", "PS5", "Xbox Series X/S", "Nintendo Switch")

mani_menu = """--- MENÚ DE VIDEOJUEGOS
1. Registrar videojuego.
2. Ver videojugos.
3. Modificar videojuego.
4. Eliminar videojuego.
5. Salir."""

while True:
    os.system('cls')
    print(mani_menu)

    opt = input("Seleccione una opción (1-5): ")

    if opt == "1":
        os.system('cls')
        print("--- 1. Registrar videojuego. ---")
        while True:
            try:
                codigo = int(input("Ingrese el código del videojuego: "))
                if codigo > 0:
                    break
                else:
                    print("ERROR: El código debe er un valor entero positivo.")
            except:
                print("ERROR: Debe ingresar una opción numérica entera válida.")
            time.sleep(WAIT)
        while True:
            try:
                nombre = input("Ingrese el nombre del videojuego: ").strip().title()
                break
            except:
                ("ERROR: Debe ingresar un dato alfanumérico para nombre.")
            time.sleep(WAIT)
        while True:
            try:
                genero = input("Ingrese el género del videojuego: ").strip().title()
                if genero.isalpha():
                    break
                else:
                    print("ERROR: Debe ser un dato de sólo letras.")
            except:
                ("ERROR: Debe ingresar un dato alfanumérico para género.")
            time.sleep(WAIT)

        print("Plataformas disponible:")
        print("1. PC")
        print("2. PS5")
        print("3. Xbox Series X/S")
        print("4. Nintendo Swtich")
        
        while True:
            try:
                plataforma_codigo = int(input("Seleccione el número de la plartaforma: "))
                if plataforma_codigo in(1,2,3,4):
                    plataforma = plataformas[plataforma_codigo - 1]
                    break
                else:
                    print("ERROR: Opción no válida. Debe ser una opción de las disponibles en plataformas disponibles.")
            except:
                print("ERROR: Debe ingresar un valor numérico entero. Elija una de las opciones.")
            time.sleep(WAIT)

        videojuego = {
            "codigo" : codigo,
            "nombre" : nombre,
            "genero" : genero,
            "plataforma" : plataforma
        }

        videojuegos.append(videojuegos)
        print("Videojuego registrado correctamente.")
        time.sleep(WAIT)

    elif opt == "2":
        os.system('cls')
        print("--- 2. Ver videojugos. ---")
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            print("\n--- LISTA DE VIDEOJUEGOS ---")
            for v in videojuegos:
                print(f"Código: {v['codigo']} | Nombre: {v['nombre']} | Género: {v['genero']} | Plataforma: {v['plataforma']}")
    
    elif opt == "3":
        os.system('cls')
        print("--- 3. Modificar videojuego. ---")

        while True:
            try:
                codigo = int(input("Ingrese el código del videojuego a modificar: "))
                if codigo > 0:
                    break
                else:
                    print("ERROR: Debe ingresar un valor numérico entero positivo.")
            except:
                print("ERROR: Debe ingresar un valor numérico entero.")
            time.sleep(WAIT)

        encontrado = False
        for v in videojuegos:
            if v['codigo'] == codigo:
                v['nombre'] =  input("Nuevo nombre: ")
                v['genero'] = input("Nuevo género: ")

                print("Plataformas disponible:")
                print("1. PC")
                print("2. PS5")
                print("3. Xbox Series X/S")
                print("4. Nintendo Swtich")

                plataforma_codigo =  int(input("Seleccione el número de la nueva plataforma: "))
                v['plataforma'] = plataformas[plataforma_codigo - 1]

                print("Videojuego modificado correctamente.")
                encontrado = True

        if not encontrado:
            print("Videojuego no encontrado.")
        time.sleep(WAIT)
    elif opt == "4":
        os.system('cls')
        print("--- 4. Eliminar videojuego. ---")

        while True:
            try:
                codigo = int(input("Ingrese el código del videojuego a eliminar: "))
                if codigo > 0:
                    break
                else:
                    print("ERROR: Debe ingresar un valor numérico entero positivo.")
            except:
                print("ERROR: Debe ingresar un valor numérico entero.")
            time.sleep(WAIT)

        eliminado = False
        for v in videojuego:
            if v["codigo"] == codigo:
                videojuegos.remove(v)
                print("Videojuego eliminado correctamente.")
                eliminado = True
        if not eliminado:
            print("Videojuego no encontrado.")
        time.sleep(WAIT)
    elif opt == "5":
        print("Saliendo del programa.")
        time.sleep(WAIT)
        break
    else:
        print("ERROR: Opción incorrecta. Debe indicar un número entero desde las opciones disponibles en el menú.")
    time.sleep(WAIT)
