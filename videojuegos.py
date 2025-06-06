# Código videojuegos con uso de listas y diccionarios.

videojuegos = []

plataformas = ("PC", "PS5", "Xbox Series X/S", "Nintendo Switch")

mani_menu = """--- MENÚ DE VIDEOJUEGOS
1. Registrar videojuego.
2. Ver videojugos.
3. Modificar videojuego.
4. Eliminar videojuego.
5. Salir."""

while True:
    print(mani_menu)

    opt = input("Seleccione una opción (1-5): ")

    if opt == "1":
        codigo = int(input("Ingrese el código del videojuego: "))
        nombre = input("Ingrese el nombre del videojuego: ")
        genero = input("Ingrese el género del videojuego: ")

        print("Plataformas disponible:")
        print("1. PC")
        print("2. PS5")
        print("3. Xbox Series X/S")
        print("4. Nintendo Swtich")

        plataforma_codigo = int(input("Seleccione el núnmero de la plartaforma: "))
        plataforma = plataformas[plataforma_codigo - 1]

        videojuego = {
            "codigo" : codigo,
            "nombre" : nombre,
            "genero" : genero,
            "plataforma" : plataforma
        }

        videojuegos.append(videojuegos)
        print("Videojuego registrado correctamente.")

    elif opt == "2":
        if len(videojuegos) == 0:
            print("No hay videojuegos registrados.")
        else:
            print("\n--- LISTA DE VIDEOJUEGOS ---")
            for v in videojuegos:
                print(f"Código: {v['codigo']} | Nombre: {v['nombre']} | Género: {v['genero']} | Plataforma: {v['plataforma']}")
    
    elif opt == "3":
        codigo = int(input("Ingrese el código del videojuego a modificar: "))
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
    elif opt == "4":
        pass
    elif opt == "5":
        print("Saliendo del programa.")
        break
    else:
        print("ERROR: Opción incorrecta. Debe indicar un número entero desde las opciones disponibles en el menú.")
