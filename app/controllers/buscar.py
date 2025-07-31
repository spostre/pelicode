import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica
from tabulate import tabulate

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

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    for pelicula in peliculas_data.values():
        if (titulo in pelicula['titulo'].lower()):

            tabla.append([pelicula['titulo'], pelicula['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    for cancion in musica_data.values():
        if (titulo in cancion['titulo'].lower()):

            tabla.append([cancion['titulo'], cancion['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


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

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            

    for pelicula in peliculas_data.values():
        if (autor in pelicula['director'].lower()):

            tabla.append([pelicula['titulo'], pelicula['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    for cancion in musica_data.values():
        if (autor in cancion['artista'].lower()):

            tabla.append([musica['titulo'], musica['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


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

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

            found = True
            


    for pelicula in peliculas_data.values():
        if (genero in pelicula['genero'].lower()):

            tabla.append([pelicula['titulo'], pelicula['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    for cancion in musica_data.values():
        if (genero in cancion['genero'].lower()):
            
            tabla.append([cancion['titulo'], cancion['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    if (not found):
        print("No se encontraron resultados.")

    screen.pausar_pantalla()
    main.main()