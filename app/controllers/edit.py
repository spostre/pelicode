import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica

def edit_menu():
    screen.limpiar_pantalla()

    print("Editar Elemento")
    print("1. Editar Libro")
    print("2. Editar Película")
    print("3. Editar Música")
    print("4. Volver al Menú Principal")

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if (opcion == 1):
                edit_libro()
            elif (opcion == 2):
                edit_pelicula()
            elif (opcion == 3):
                edit_musica()
            elif (opcion == 4):
                main.main()
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

#Libro
def edit_libro():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    global key_libro
    
    print('Que libro deseas editar?')
    for libro in libros_data.items():
        print(f"{libro[0]}")

    while True:
        try:
            key_libro = input("Seleccione el libro a editar: ").upper()

            if (key_libro in libros_data):
                screen.limpiar_pantalla()

                print(f"Libro seleccionado: {libros_data[key_libro]['titulo']} por {libros_data[key_libro]['autor']}")
                print("\n¿Qué aspecto del libro desea editar?")
                print("1. Título")
                print("2. Autor")
                print("3. Género")
                print("4. Calificación")
                print("5. Volver al Menú de Edición")

                while True:
                    try:
                        sub_opcion = int(input("Seleccione una opción: "))
                        if sub_opcion == 1:
                            edit_libro_titulo()
                        elif sub_opcion == 2:
                            edit_libro_autor()
                        elif sub_opcion == 3:
                            edit_libro_genero()
                        elif sub_opcion == 4:
                            edit_libro_calificacion()
                        elif sub_opcion == 5:
                            edit_menu()
                        else:
                            print("Opción no válida. Intente de nuevo.")
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número.")
            else:
                print("Codigo no valido. Intente de nuevo.")
                continue

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número o el título del libro.")

def edit_libro_titulo():

    global key_libro
    libros_data = core.readDataFile(libros)

    nuevo_titulo = input("Ingrese el nuevo titulo del libro: ")

    libros_data[key_libro]['titulo'] = nuevo_titulo
    
    core.writeDataFile(libros, libros_data)
    
    print(f"¡Título del libro con ID '{key_libro}' actualizado a '{nuevo_titulo}'!")
    screen.pausar_pantalla()
    main.main()

def edit_libro_autor():

    global key_libro
    libros_data = core.readDataFile(libros)

    nuevo_autor = input("Ingrese el nuevo autor del libro: ")

    libros_data[key_libro]['autor'] = nuevo_autor
    core.writeDataFile(libros, libros_data)

    print(f"¡Autor del libro con ID '{key_libro}' actualizado!")
    screen.pausar_pantalla()
    main.main()

def edit_libro_genero():
    global key_libro
    libros_data = core.readDataFile(libros)

    print("Ingrese el género del libro:\n1. Fantasía\n2. Ciencia\n3. Romance\n4. Misterio\n5. Accion ")
    genero = int(input('Seleccione una opcion: '))
    if (genero == 1):
        genero = 'Fantasia'
    elif (genero == 2):
        genero = 'Ciencia'
    elif (genero == 3):
        genero = 'Romance'
    elif (genero == 4):
        genero = 'Misterio'
    elif (genero == 5):
        genero = 'Acción'
    else:
        print("Opción no válida. Intente de nuevo.")
        screen.pausar_pantalla()
        edit_libro_genero()

    libros_data[key_libro]['genero'] = genero
    core.writeDataFile(libros, libros_data)

    print(f"¡Género del libro con ID '{key_libro}' actualizado!")
    screen.pausar_pantalla()
    main.main()

def edit_libro_calificacion():
    global key_libro
    libros_data = core.readDataFile(libros)

    while True:
        try:
            nueva_calificacion = int(input("Ingrese la nueva calificación (1-5): "))
            if (1 <= nueva_calificacion <= 5):
                libros_data[key_libro]['calificacion'] = nueva_calificacion
                core.writeDataFile(libros, libros_data)
                print(f"¡Calificación del libro con ID '{key_libro}' actualizada!")
                screen.pausar_pantalla()
                return
            else:
                print("Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")
    

#Pelicula
def edit_pelicula():
    global key_pelicula
    screen.limpiar_pantalla()
    peliculas_data = core.readDataFile(peliculas)

    if (not peliculas_data):
        print("No hay películas registradas para editar.")
        screen.pausar_pantalla()
        return

    print("--- Seleccione la Película a Editar ---")
    for id_pelicula, data_pelicula in peliculas_data.items():
        print(f"{id_pelicula}: {data_pelicula['titulo']}")

    while True:
        key_pelicula = input("Seleccione el ID de la película a editar: ").upper()
        if key_pelicula in peliculas_data:
            break
        else:
            print("ID no válido. Intente de nuevo.")

    while True:
        screen.limpiar_pantalla()
        print(f"Editando: {peliculas_data[key_pelicula]['titulo']}")
        print("¿Qué aspecto de la película desea editar?")
        print("1. Título")
        print("2. Director")
        print("3. Género")
        print("4. Calificación")
        print("5. Volver")

        try:
            sub_opcion = int(input("Seleccione una opción: "))
            if sub_opcion == 1:
                edit_pelicula_titulo()
            elif sub_opcion == 2:
                edit_pelicula_director()
            elif sub_opcion == 3:
                edit_pelicula_genero()
            elif sub_opcion == 4:
                edit_pelicula_calificacion()
            elif sub_opcion == 5:
                edit_menu()
            else:
                print("Opción no válida.")
                screen.pausar_pantalla()
        except ValueError:
            print("Entrada no válida. Ingrese un número.")
            screen.pausar_pantalla()
    

def edit_pelicula_titulo():
    global key_pelicula
    peliculas_data = core.readDataFile(peliculas)

    nuevo_titulo = input("Ingrese el nuevo titulo de la película: ")

    peliculas_data[key_pelicula]['titulo'] = nuevo_titulo
    core.writeDataFile(peliculas, peliculas_data)

    print(f"¡Título de la película con ID '{key_pelicula}' actualizado!")
    screen.pausar_pantalla()

def edit_pelicula_director():
    global key_pelicula
    peliculas_data = core.readDataFile(peliculas)

    nuevo_director = input("Ingrese el nuevo director de la película: ")

    peliculas_data[key_pelicula]['director'] = nuevo_director
    core.writeDataFile(peliculas, peliculas_data)

    print(f"¡Director de la película con ID '{key_pelicula}' actualizado!")
    screen.pausar_pantalla()

def edit_pelicula_genero():
    global key_pelicula
    peliculas_data = core.readDataFile(peliculas)

    print("Ingrese el género del libro:\n1. Fantasía\n2. Ciencia\n3. Romance\n4. Misterio\n5. Accion ")
    genero = int(input('Seleccione una opcion: '))
    if (genero == 1):
        genero = 'Fantasia'
    elif (genero == 2):
        genero = 'Ciencia'
    elif (genero == 3):
        genero = 'Romance'
    elif (genero == 4):
        genero = 'Misterio'
    elif (genero == 5):
        genero = 'Acción'
    else:
        print("Opción no válida. Intente de nuevo.")
        screen.pausar_pantalla()
        edit_pelicula_genero()

    peliculas_data[key_pelicula]['genero'] = genero
    core.writeDataFile(peliculas, peliculas_data)

    print(f"¡Género de la película con ID '{key_pelicula}' actualizado!")
    screen.pausar_pantalla()

def edit_pelicula_calificacion():
    global key_pelicula
    peliculas_data = core.readDataFile(peliculas)

    while True:
        try:
            nueva_calificacion = int(input("Ingrese la nueva calificación (1-5): "))

            if (1 <= nueva_calificacion <= 5):
                peliculas_data[key_pelicula]['calificacion'] = nueva_calificacion
                core.writeDataFile(peliculas, peliculas_data)
                print(f"\n¡Calificación de la película con ID '{key_pelicula}' actualizada!")
                screen.pausar_pantalla()
                return
            else:
                print("Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")

#Musica
def edit_musica():
    global key_musica
    screen.limpiar_pantalla()
    musica_data = core.readDataFile(musica)

    if (not musica_data):
        print("No hay canciones registradas para editar.")
        screen.pausar_pantalla()
        return

    print("--- Seleccione la Canción a Editar ---")
    for id_musica, data_musica in musica_data.items():
        print(f"{id_musica}: {data_musica['titulo']}")

    while True:
        key_musica = input("\nSeleccione el ID de la canción a editar: ").upper()
        if key_musica in musica_data:
            break
        else:
            print("ID no válido. Intente de nuevo.")

    while True:
        screen.limpiar_pantalla()
        print(f"Editando: {musica_data[key_musica]['titulo']}")
        print("\n¿Qué aspecto de la canción desea editar?")
        print("1. Título")
        print("2. Artista")
        print("3. Género")
        print("4. Calificación")
        print("5. Volver")

        try:
            sub_opcion = int(input("Seleccione una opción: "))
            if sub_opcion == 1:
                edit_musica_titulo()
            elif sub_opcion == 2:
                edit_musica_artista()
            elif sub_opcion == 3:
                edit_musica_genero()
            elif sub_opcion == 4:
                edit_musica_calificacion()
            elif sub_opcion == 5:
                edit_menu()
            else:
                print("Opción no válida.")
                screen.pausar_pantalla()
        except ValueError:
            print("Entrada no válida. Ingrese un número.")
            screen.pausar_pantalla()

def edit_musica_titulo():
    global key_musica
    musica_data = core.readDataFile(musica)
    
    nuevo_titulo = input("Ingrese el nuevo titulo de la canción: ")

    musica_data[key_musica]['titulo'] = nuevo_titulo
    core.writeDataFile(musica, musica_data)

    print(f"¡Título de la canción con ID '{key_musica}' actualizado!")
    screen.pausar_pantalla()

def edit_musica_artista():
    global key_musica
    musica_data = core.readDataFile(musica)

    nuevo_artista = input("Ingrese el nuevo artista de la canción: ")

    musica_data[key_musica]['artista'] = nuevo_artista
    core.writeDataFile(musica, musica_data)

    print(f"¡Artista de la canción con ID '{key_musica}' actualizado!")
    screen.pausar_pantalla()

def edit_musica_genero():
    global key_musica
    musica_data = core.readDataFile(musica)

    print("Ingrese el género de la musica:\n1. Hardcore\n2. Electronica\n3. Rock\n4. Jazz\n5. Clasica ")
    genero = int(input('Seleccione una opcion: '))
    if (genero == 1):
        genero = 'Hardcore'
    elif (genero == 2):
        genero = 'Electronica'
    elif (genero == 3):
        genero = 'Rock'
    elif (genero == 4):
        genero = 'Jazz'
    elif (genero == 5):
        genero = 'Clasica'
    else:
        print("Opción no válida. Intente de nuevo.")
        screen.pausar_pantalla()
        edit_musica_genero
   

    musica_data[key_musica]['genero'] = genero
    core.writeDataFile(musica, musica_data)

    print(f"¡Género de la canción con ID '{key_musica}' actualizado!")
    screen.pausar_pantalla()

def edit_musica_calificacion():
    global key_musica
    musica_data = core.readDataFile(musica)

    while True:
        try:
            nueva_calificacion = int(input("Ingrese la nueva calificación (1-5): "))
            if (1 <= nueva_calificacion <= 5):
                musica_data[key_musica]['calificacion'] = nueva_calificacion
                core.writeDataFile(musica, musica_data)
                print(f"\n¡Calificación de la canción con ID '{key_musica}' actualizada!")
                screen.pausar_pantalla()
                return
            else:
                print("Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")