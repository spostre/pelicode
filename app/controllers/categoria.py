import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica

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
        cat_misterio()
    elif (opcion == '4'):
        cat_comedia()
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
        if libro['genero'].lower() == 'fantasía':
            print(f"{libro['titulo']} por {libro['autor']}")
    
    print('Películas de Fantasía:')
    for pelicula in peliculas_data.values():
        if pelicula['genero'].lower() == 'fantasía':
            print(f"{pelicula['titulo']} dirigida por {pelicula['director']}")

    print('Música de Fantasía:')
    for musicas in musica_data.values():
        if musicas['genero'].lower() == 'fantasía':
            print(f"{musicas['titulo']} por {musicas['artista']}")

    screen.pausar_pantalla()
    main.main()

def cat_ciencia():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    print('Libros de Ciencia:')
    for libro in libros_data.values():
        if libro['genero'].lower() == 'ciencia':
            print(f"{libro['titulo']} por {libro['autor']}")
    
    print('Películas de Ciencia:')
    for pelicula in peliculas_data.values():
        if pelicula['genero'].lower() == 'ciencia':
            print(f"{pelicula['titulo']} dirigida por {pelicula['director']}")

    print('Música de Ciencia:')
    for musicas in musica_data.values():
        if musicas['genero'].lower() == 'ciencia':
            print(f"{musicas['titulo']} por {musicas['artista']}")
        
    screen.pausar_pantalla()
    main.main()

def cat_misterio():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    print('Libros de Romance:')
    for libro in libros_data.values():
        if libro['genero'].lower() == 'romance':
            print(f"{libro['titulo']} por {libro['autor']}")
    
    print('Películas de Romance:')
    for pelicula in peliculas_data.values():
        if pelicula['genero'].lower() == 'romance':
            print(f"{pelicula['titulo']} dirigida por {pelicula['director']}")

    print('Música de Romance:')
    for musicas in musica_data.values():
        if musicas['genero'].lower() == 'Romance':
            print(f"{musicas['titulo']} por {musicas['artista']}")

    screen.pausar_pantalla()
    main.main()

def cat_comedia():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    print('Libros de Misterio:')
    for libro in libros_data.values():
        if libro['genero'].lower() == 'misterio':
            print(f"{libro['titulo']} por {libro['autor']}")
    
    print('Películas de Misterio:')
    for pelicula in peliculas_data.values():
        if pelicula['genero'].lower() == 'misterio':
            print(f"{pelicula['titulo']} dirigida por {pelicula['director']}")

    print('Música de Misterio:')
    for musicas in musica_data.values():
        if musicas['genero'].lower() == 'misterio':
            print(f"{musicas['titulo']} por {musicas['artista']}")

    screen.pausar_pantalla()
    main.main()

def cat_accion():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    print('Libros de Acción:')
    for libro in libros_data.values():
        if libro['genero'].lower() == 'acción':
            print(f"{libro['titulo']} por {libro['autor']}")
    
    print('Películas de Acción:')
    for pelicula in peliculas_data.values():
        if pelicula['genero'].lower() == 'acción':
            print(f"{pelicula['titulo']} dirigida por {pelicula['director']}")

    print('Música de Acción:')
    for musicas in musica_data.values():
        if musicas['genero'].lower() == 'acción':
            print(f"{musicas['titulo']} por {musicas['artista']}")

    screen.pausar_pantalla()
    main.main()

    #AÑADIR TABULATE