import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica
#from tabulate import tabulate

def search_menu():

    screen.limpiar_pantalla()

    print("Buscar Elemento")
    print("1. Buscar por Título")
    print("2. Buscar por Autor/Director/Artista")
    print("3. Buscar por Género")
    print("4. Volver al Menú Principal")

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if (opcion == 1):
                search_titulo()
            elif (opcion == 2):
                search_autor()
            elif (opcion == 3):
                search_genero()
            elif (opcion == 4):
                main.main()
                
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def search_titulo():
    screen.limpiar_pantalla()
    titulo = input("Ingrese el título a buscar: ").lower()
    
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    found = False

    tabla = []
    headers = ["Título", "Autor/Director/Artista"]

    for libro in libros_data.values():
        if (titulo in libro['titulo'].lower()):
            print(f"Libro encontrado: {libro['titulo']} por {libro['autor']}")
            found = True
            #tabulate


    for pelicula in peliculas_data.values():
        if (titulo in pelicula['titulo'].lower()):
            print(f"Pelicula encontrada: {pelicula['titulo']} dirigida por {pelicula['director']}")
            found = True
            #tabulate


    for cancion in musica_data.values():
        if (titulo in cancion['titulo'].lower()):
            print(f"Canción encontrada: {cancion['titulo']} por {cancion['artista']}")
            found = True
            #tabulate


    if (not found):
        print("No se encontraron resultados.")

    screen.pausar_pantalla()
    main.main()

def search_autor():
    screen.limpiar_pantalla()
    autor = input("Ingrese el autor/director/artista a buscar: ").lower()
    
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    found = False

    tabla = []
    headers = ["Título", "Autor/Director/Artista"]

    for libro in libros_data.values():
        if (autor in libro['autor'].lower()):
            print(f"Libro encontrado: {libro['titulo']} por {libro['autor']}")
            found = True
            #tabulate

    for pelicula in peliculas_data.values():
        if (autor in pelicula['director'].lower()):
            print(f"Pelicula encontrada: {pelicula['titulo']} dirigida por {pelicula['director']}")
            found = True
            #tabulate


    for cancion in musica_data.values():
        if (autor in cancion['artista'].lower()):
            print(f"Canción encontrada: {cancion['titulo']} por {cancion['artista']}")
            found = True
            #tabulate


    if (not found):
        print("No se encontraron resultados.")

    screen.pausar_pantalla()
    main.main()

def search_genero():
    screen.limpiar_pantalla()
    genero = input("Ingrese el género a buscar: ").lower()
    
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    found = False

    tabla = []
    headers = ["Título", "Autor/Director/Artista"]

    for libro in libros_data.values():
        if (genero in libro['genero'].lower()):
            print(f"Libro encontrado: {libro['titulo']} por {libro['autor']}")
            found = True
            #tabulate


    for pelicula in peliculas_data.values():
        if (genero in pelicula['genero'].lower()):
            print(f"Pelicula encontrada: {pelicula['titulo']} dirigida por {pelicula['director']}")
            found = True
            #tabulate


    for cancion in musica_data.values():
        if (genero in cancion['genero'].lower()):
            print(f"Canción encontrada: {cancion['titulo']} por {cancion['artista']}")
            found = True
            #tabulate


    if (not found):
        print("No se encontraron resultados.")

    screen.pausar_pantalla()
    main.main()