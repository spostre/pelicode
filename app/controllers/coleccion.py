import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica

libros_usados = []
peliculas_usadas = []
musicas_usada = []

libros_coleccion = []


def array_menu():
    screen.limpiar_pantalla()

    print('A que colección deseas acceder?')
    print('1. Libros')
    print('2. Películas')
    print('3. Música')
    print('4. Volver al Menú Principal')

    while True:
        try:
            opcion = int(input('Seleccione una opción: '))
            if (opcion == 1):
                array_libros()
            elif (opcion == 2):
                array_peliculas()
            elif (opcion == 3):
                array_musica()
            elif (opcion == 4):
                main.main()
            else:
                print('Opción no válida. Intente de nuevo.')
        except ValueError:
            print('Entrada no válida. Por favor, ingrese un número.')

def array_libros():
    screen.limpiar_pantalla()

    libros_data = core.readDataFile(libros)
    
    repeat = True

    while repeat == True:
        screen.limpiar_pantalla()
        print('Añadir Libro')
        
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

            print("Ingrese el género del libro:\n1. Fantasía\n2. Ciencia\n3. Romance\n4. Misterio\n5. Accion ")
            genero = int(input('Seleccione una opcion: '))
            if (genero == 1):
                genero = 'Fantasía'
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
                continue

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
                    libros_coleccion.append(libros_data)


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
            libros_coleccion.append(libros_data)

            libros_usados.append(tituloL)
        
        print('Libro añadido exitosamente a la colección.')
        print('Quieres añadir otro libro? y/n')
        op = input("Ingrese 'y' para sí o 'n' para no: ").lower()
        if (op == 'y'):
            repeat = True
        else:
            repeat = False
        
        
    core.writeDataFile(libros, libros_data)
    print('Coleccion guardada y actualizada.')

    screen.pausar_pantalla()
    main.main()  

def array_peliculas():
    screen.limpiar_pantalla()

    peliculas_data = core.readDataFile(peliculas)
    
    repeat = True

    while repeat == True:
        screen.limpiar_pantalla()
        print('Añadir Película')
        
        try:

            tituloP = input("Ingrese el título de la película: ")

            if (not tituloP.isalpha()):
                print("El título debe contener solo letras.")
                screen.pausar_pantalla()
                continue
            elif (tituloP in peliculas_usadas):
                print("La película ya esta almacenada. Por favor, ingrese un título diferente.")
                screen.pausar_pantalla()
                continue

            director = input("Ingrese el director de la película: ")

            if (not director.isalpha()):
                print("El director debe contener solo letras.")
                screen.pausar_pantalla()
                continue

            print("Ingrese el género de la película:\n1. Fantasía\n2. Ciencia\n3. Romance\n4. Misterio\n5. Accion ")
            genero = int(input('Seleccione una opcion: '))
            if (genero == 1):
                genero = 'Fantasía'
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
                continue

        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
            screen.pausar_pantalla()
            continue

        print('Quiere calificar la pelicula? y/n')
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
        print('Película añadida exitosamente a la colección.')
        print('Quieres añadir otra pelicula? y/n')
        op = input("Ingrese 'y' para sí o 'n' para no: ").lower()
        if (op == 'y'):
            repeat = True
        else:
            repeat = False
    core.writeDataFile(peliculas, peliculas_data)
    print('Coleccion guardada y actualizada.')
    screen.pausar_pantalla()
    main.main()

def array_musica():
    screen.limpiar_pantalla()

    musica_data = core.readDataFile(musica)
    
    repeat = True

    while repeat == True:
        screen.limpiar_pantalla()
        print('Añadir Música')
        
        try:

            tituloM = input("Ingrese el título de la música: ")

            if (not tituloM.isalpha()):
                print("El título debe contener solo letras.")
                screen.pausar_pantalla()
                continue
            elif (tituloM in musicas_usada):
                print("La música ya esta almacenada. Por favor, ingrese un título diferente.")
                screen.pausar_pantalla()
                continue

            artista = input("Ingrese el artista de la música: ")

            if (not artista.isalpha()):
                print("El artista debe contener solo letras.")
                screen.pausar_pantalla()
                continue

            print("Ingrese el género de la música:\n1. Pop\n2. Rock\n3. Jazz\n4. Clásica\n5. Hip-Hop ")
            genero = int(input('Seleccione una opcion: '))
            if (genero == 1):
                genero = 'Pop'
            elif (genero == 2):
                genero = 'Rock'
            elif (genero == 3):
                genero = 'Jazz'
            elif (genero == 4):
                genero = 'Clásica'
            elif (genero == 5):
                genero = 'Hip-Hop'
            else:
                print("Opción no válida. Intente de nuevo.")
                screen.pausar_pantalla()
                continue

        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
            screen.pausar_pantalla()
            continue

        print('Quiere calificar la musica? y/n')
        calificar = input("Ingrese 'y' para sí o 'n' para no: ").lower()
        
        id_musica = f"M{len(musica_data) + 1:03d}"

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
                    musica_data[id_musica] = musicas
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

            musica_data[id_musica] = musicas
            musicas_usada.append(tituloM)
        print('Música añadida exitosamente a la colección.')
        print('Quieres añadir otra musica? y/n')
        op = input("Ingrese 'y' para sí o 'n' para no: ").lower()
        if (op == 'y'):
            repeat = True
        else:
            repeat = False
    core.writeDataFile(musica, musica_data)
    print('Coleccion guardada y actualizada.')
    screen.pausar_pantalla()
    main.main()
    