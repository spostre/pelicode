import json
import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica

libros_usados = []
peliculas_usadas = []
musicas_usada = []

def add_menu():
    screen.limpiar_pantalla()
    print('Añadir un Nuevo Elemento')
    print('¿Qué tipo de elemento deseas añadir?')
    print('1. Libro')
    print('2. Película')
    print('3. Música')
    print('4. Regresar al Menú Principal')
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if (opcion == 1):
                add_libro()
            elif (opcion == 2):
                add_pelicula()
            elif (opcion == 3):
                add_musicas()
            elif (opcion == 4):
                main.main()
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def add_libro():
    screen.limpiar_pantalla()

    libros_data = core.readDataFile(libros)
    confirmed = True
    print('Añadir Libro')
    while confirmed == True:
        try:

            tituloL = input("Ingrese el título del libro: ")

            if (not tituloL.isalpha()):
                print("El título debe contener solo letras.")
                screen.pausar_pantalla()
                continue
            elif (tituloL in libros_usados):
                print("El libro ya esta almacenado. Por favor, ingrese un título diferente.")
                screen.pausar_pantalla()
                continue

            autor = input("Ingrese el autor del libro: ")

            if (not autor.isalpha()):
                print("El autor debe contener solo letras.")
                screen.pausar_pantalla()
                continue

            genero = input("Ingrese el género del libro: ")

            if (not genero.isalpha()):
                print("El género debe contener solo letras.")
                screen.pausar_pantalla()
            else:
                confirmed = False

        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
            screen.pausar_pantalla()
            continue

    print('Quiere calificar la pelicula? y/n')
    calificar = input("Ingrese 'y' para sí o 'n' para no: ").lower()
    
    id_libro = f"L{len(libros_data) + 1:03d}"

    if (calificar == 'y'):
        try:
            calificacion = int(input("Ingrese la calificación del libro (1-5): "))
            if (1 <= calificacion <= 5):
                libro = {
                    "titulo": tituloL,
                    "autor": autor,
                    "genero": genero,
                    "calificacion": calificacion
                }

                libros_data[id_libro] = libro

                libros_usados.append(tituloL)

            else:
                print("La calificación debe estar entre 1 y 5.")
                screen.pausar_pantalla()
                return calificar
               

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 5.")
            screen.pausar_pantalla()
            return calificar
    
    else:
            
    
        libro = {
            "titulo": tituloL,
            "autor": autor,
            "genero": genero,
        }

        libros_data[id_libro] = libro

        libros_usados.append(tituloL)
    
    core.writeDataFile(libros, libros_data)
    
    print("Libro añadido exitosamente.")
    screen.pausar_pantalla()
    main.main()  

def add_pelicula():
    screen.limpiar_pantalla()
    peliculas_data = core.readDataFile(peliculas)

    confirmed = True
    print('Añadir Película')
    while confirmed == True:
        try:
            tituloP = input("Ingrese el título de la película: ")

            if (not tituloP.isalpha()):
                print("El título debe contener solo letras.")
                screen.pausar_pantalla()
                continue
            elif (tituloP in peliculas_usadas):
                print("La película ya está almacenada. Por favor, ingrese un título diferente.")
                screen.pausar_pantalla()
                continue

            director = input("Ingrese el director de la película: ")

            if (not director.isalpha()):
                print("El director debe contener solo letras.")
                screen.pausar_pantalla()
                continue

            genero = input("Ingrese el género de la película: ")

            if (not genero.isalpha()):
                print("El género debe contener solo letras.")
                screen.pausar_pantalla()
            else:
                confirmed = False

        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
            screen.pausar_pantalla()
            continue

    print('¿Quiere calificar la película? y/n')
    calificar = input("Ingrese 'y' para sí o 'n' para no: ").lower()

    id_pelicula = f"P{len(peliculas_data) + 1:03d}"

    if (calificar == 'y'):
        try:
            calificacion = int(input("Ingrese la calificación de la película (1-5): "))
            if (1 <= calificacion <= 5):
                pelicula = {
                    "titulo": tituloP,
                    "director": director,
                    "genero": genero,
                    "calificacion": calificacion
                }

                peliculas_data[id_pelicula] = pelicula

                peliculas_usadas.append(tituloP)

            else:
                print("La calificación debe estar entre 1 y 5.")
                screen.pausar_pantalla()
                return calificar

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 5.")
            screen.pausar_pantalla()
            return calificar
    
    else:
        pelicula = {
            "titulo": tituloP,
            "director": director,
            "genero": genero,
        }

        peliculas_data[id_pelicula] = pelicula

        peliculas_usadas.append(tituloP)

    core.writeDataFile(peliculas, peliculas_data)

    print("Libro añadido exitosamente.")
    screen.pausar_pantalla()
    main.main()  

def add_musicas():
    screen.limpiar_pantalla()
    musicas_data = core.readDataFile(musica)

    confirmed = True
    print('Añadir Música')
    while confirmed == True:
        try:
            tituloM = input("Ingrese el título de la música: ")

            if (not tituloM.isalpha()):
                print("El título debe contener solo letras.")
                screen.pausar_pantalla()
                continue
            elif (tituloM in musicas_usada):
                print("La música ya está almacenada. Por favor, ingrese un título diferente.")
                screen.pausar_pantalla()
                continue

            artista = input("Ingrese el artista de la música: ")

            if (not artista.isalpha()):
                print("El artista debe contener solo letras.")
                screen.pausar_pantalla()
                continue

            genero = input("Ingrese el género de la música: ")

            if (not genero.isalpha()):
                print("El género debe contener solo letras.")
                screen.pausar_pantalla()
            else:
                confirmed = False

        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
            screen.pausar_pantalla()
            continue
    
    print('¿Quiere calificar la música? y/n')
    calificar = input("Ingrese 'y' para sí o 'n' para no: ").lower()

    id_musica = f"M{len(musicas_data) + 1:03d}"
    
    if (calificar == 'y'):
        try:
            calificacion = int(input("Ingrese la calificación de la música (1-5): "))
            if (1 <= calificacion <= 5):
                musicas = {
                    "titulo": tituloM,
                    "artista": artista,
                    "genero": genero,
                    "calificacion": calificacion
                }

                musicas_data[id_musica] = musicas

                musicas_usada.append(tituloM)

            else:
                print("La calificación debe estar entre 1 y 5.")
                screen.pausar_pantalla()
                return calificar

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 5.")
            screen.pausar_pantalla()
            return calificar
        
    else:
        musicas = {
            "titulo": tituloM,
            "artista": artista,
            "genero": genero,
        }

        musicas_data[id_musica] = musicas

        musicas_usada.append(tituloM)

    core.writeDataFile(musica, musicas_data)
    print("Música añadida exitosamente.")
    screen.pausar_pantalla()
    main.main()

