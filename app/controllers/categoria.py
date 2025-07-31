import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica
from tabulate import tabulate

def cat_menu():
    screen.limpiar_pantalla()

    print('Categorías')
    print('1. Fantasia ')
    print('2. Ciencia')
    print('3. Romance')
    print('4. Misterio')
    print('5. Accion')
    print('6. Regresar al Menú Principal')

    opcion = input('Seleccione una opción: ')

    if (opcion == '1'):
        cat_fantasia()
    elif (opcion == '2'):
        cat_ciencia()
    elif (opcion == '3'):
        cat_romance()
    elif (opcion == '4'):
        cat_misterio()
    elif (opcion == '5'):
        cat_accion()
    elif (opcion == '6'):
        main.main()
    else:
        print('Opción no válida. Intente de nuevo.')
        screen.pausar_pantalla()
        cat_menu()

def cat_fantasia():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    tabla = []
    headers = ["Título", "Autor/Director/Artista"]

    print('Libros de Fantasía:')
    for libro in libros_data.values():
        if (libro['genero'].lower() == 'fantasía'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Fantasía:')
    for pelicula in peliculas_data.values():
        if (pelicula['genero'].lower() == 'fantasía'):

            tabla.append([pelicula['titulo'], pelicula['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    print('Música de Fantasía:')
    for musicas in musica_data.values():
        if (musicas['genero'].lower() == 'fantasía'):

            tabla.append([musicas['titulo'], musicas['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

def cat_ciencia():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    tabla = []
    headers = ["Titulo", "Autor/Director/Artista"]

    print('Libros de Ciencia:')
    for libro in libros_data.values():
        if (libro['genero'].lower() == 'ciencia'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Ciencia:')
    for pelicula in peliculas_data.values():
        if (pelicula['genero'].lower() == 'ciencia'):

            tabla.append([pelicula['titulo'], pelicula['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    print('Música de Ciencia:')
    for musicas in musica_data.values():
        if (musicas['genero'].lower() == 'ciencia'):

            tabla.append([musicas['titulo'], musicas['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
        
    screen.pausar_pantalla()
    main.main()

def cat_romance():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    tabla = []
    headers = ["Titulo", "Autor/Director/Artista"]

    print('Libros de Romance:')
    for libro in libros_data.values():
        if (libro['genero'].lower() == 'romance'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Romance:')
    for pelicula in peliculas_data.values():
        if (pelicula['genero'].lower() == 'romance'):

            tabla.append([pelicula['titulo'], pelicula['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    print('Música de Romance:')
    for musicas in musica_data.values():
        if (musicas['genero'].lower() == 'Romance'):

            tabla.append([musicas['titulo'], musicas['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

def cat_misterio():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    tabla = []
    headers = ["Titulo", "Autor/Director/Artista"]

    print('Libros de Misterio:')
    for libro in libros_data.values():
        if (libro['genero'].lower() == 'misterio'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Misterio:')
    for pelicula in peliculas_data.values():
        if (pelicula['genero'].lower() == 'misterio'):

            tabla.append([pelicula['titulo'], pelicula['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    print('Música de Misterio:')
    for musicas in musica_data.values():
        if (musicas['genero'].lower() == 'misterio'):

            tabla.append([musicas['titulo'], musicas['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

def cat_accion():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    tabla = []
    headers = ["Titulo", "Autor/Director/Artista"]

    print('Libros de Acción:')
    for libro in libros_data.values():
        if (libro['genero'].lower() == 'acción'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Acción:')
    for pelicula in peliculas_data.values():
        if (pelicula['genero'].lower() == 'acción'):

            tabla.append([pelicula['titulo'], pelicula['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    print('Música de Acción:')
    for musicas in musica_data.values():
        if (musicas['genero'].lower() == 'acción'):

            tabla.append([musicas['titulo'], musicas['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

    