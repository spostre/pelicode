import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica

def del_menu():
    screen.limpiar_pantalla()

    print("Eliminar Elemento")
    print("1. Eliminar Libro")
    print("2. Eliminar Película")
    print("3. Eliminar Música")
    print("4. Volver al Menú Principal")

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if (opcion == 1):
                del_libro()
            elif (opcion == 2):
                del_pelicula()
            elif (opcion == 3):
                del_musica()
            elif (opcion == 4):
                main.main()
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def del_libro():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    
    print('¿Qué libro deseas eliminar?')

    for key in libros_data.keys():
        print(f"{key}: {libros_data[key]['titulo']}")

    while True:
        try:
            key_libro = input("Seleccione el libro a eliminar: ").upper()

            if (key_libro in libros_data):
                del libros_data[key_libro]

                core.writeDataFile(libros, libros_data)

                print(f"Libro {key_libro} eliminado exitosamente.")
                screen.pausar_pantalla()
                break

            else:
                print("Código no válido. Intente de nuevo.")

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número o el código del libro.")
    main.main()

def del_pelicula():
    screen.limpiar_pantalla()
    peliculas_data = core.readDataFile(peliculas)
    
    print('¿Qué película deseas eliminar?')

    for key in peliculas_data.keys():
        print(f"{key}: {peliculas_data[key]['titulo']}")

    while True:
        try:
            key_pelicula = input("Seleccione la película a eliminar: ").upper()

            if (key_pelicula in peliculas_data):
                del peliculas_data[key_pelicula]

                core.writeDataFile(peliculas, peliculas_data)

                print(f"Pelicula {key_pelicula} eliminada exitosamente.")
                screen.pausar_pantalla()
                break

            else:
                print("Código no válido. Intente de nuevo.")

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número o el código de la película.")
    main.main()

def del_musica():
    screen.limpiar_pantalla()
    musica_data = core.readDataFile(musica)
    
    print('¿Qué música deseas eliminar?')

    for key in musica_data.keys():
        print(f"{key}: {musica_data[key]['titulo']}")

    while True:
        try:
            key_musica = input("Seleccione la música a eliminar: ").upper()

            if (key_musica in musica_data):
                del musica_data[key_musica]

                core.writeDataFile(musica, musica_data)

                print(f"Música {key_musica} eliminada exitosamente.")
                screen.pausar_pantalla()
                break

            else:
                print("Código no válido. Intente de nuevo.")

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número o el código de la música.")
    main.main()