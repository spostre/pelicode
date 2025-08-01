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
    print('6. Hardcore')
    print('7. Electronica')
    print('8. Rock')
    print('9. Jazz')
    print('10. Clasica')
    print('0. Regresar al Menú Principal')

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
        cat_hardcore()
    elif (opcion == '7'):
        cat_electronica()
    elif (opcion == '8'):
        cat_rock()
    elif (opcion == '9'):
        cat_jazz()
    elif (opcion == '10'):
        cat_clasica()
    elif (opcion == '0'):
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

    print('Libros de Fantasía:')
    for libro in libros_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]

        if (libro['genero'] == 'Fantasia'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            
    
    print('Películas de Fantasía:')
    for pelicula in peliculas_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]

        if (pelicula['genero'] == 'Fantasia'):

            tabla.append([pelicula['titulo'], pelicula['director']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

def cat_ciencia():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    print('Libros de Ciencia:')
    for libro in libros_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]

        if (libro['genero'] == 'Ciencia'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Ciencia:')
    for pelicula in peliculas_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]

        if (pelicula['genero'] == 'Ciencia'):

            tabla.append([pelicula['titulo'], pelicula['director']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
        
    screen.pausar_pantalla()
    main.main()

def cat_romance():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    print('Libros de Romance:')
    for libro in libros_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]
        if (libro['genero'] == 'Romance'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Romance:')
    for pelicula in peliculas_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]
        if (pelicula['genero'] == 'Romance'):

            tabla.append([pelicula['titulo'], pelicula['director']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

def cat_misterio():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    print('Libros de Misterio:')
    for libro in libros_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]

        if (libro['genero'] == 'Misterio'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Misterio:')
    for pelicula in peliculas_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]
        if (pelicula['genero'] == 'Misterio'):

            tabla.append([pelicula['titulo'], pelicula['director']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

def cat_accion():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    

    print('Libros de Acción:')
    for libro in libros_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]

        if (libro['genero'] == 'Accion'):

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    print('Películas de Acción:')
    for pelicula in peliculas_data.values():
        tabla = []
        headers = ["Titulo", "Autor/Director/Artista"]

        if (pelicula['genero'] == 'Accion'):

            tabla.append([pelicula['titulo'], pelicula['director']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

def cat_hardcore():
    screen.limpiar_pantalla()
    musica_data = core.readDataFile(musica)

    print('Música Hardcore:')
    tabla = []
    headers = ["Titulo", "Artista"]
    for cancion in musica_data.values():
        if 'genero' in cancion and cancion['genero'] == 'Hardcore':
            tabla.append([cancion['titulo'], cancion['artista']])
    if tabla:
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron canciones de este género.")
        
    screen.pausar_pantalla()

def cat_electronica():
    screen.limpiar_pantalla()
    musica_data = core.readDataFile(musica)

    print('Música Electrónica:')
    tabla = []
    headers = ["Titulo", "Artista"]
    for cancion in musica_data.values():
        if 'genero' in cancion and cancion['genero'] == 'Electronica':
            tabla.append([cancion['titulo'], cancion['artista']])
    if tabla:
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron canciones de este género.")
        
    screen.pausar_pantalla()

def cat_rock():
    screen.limpiar_pantalla()
    musica_data = core.readDataFile(musica)

    print('Música Rock:')
    tabla = []
    headers = ["Titulo", "Artista"]
    for cancion in musica_data.values():
        if 'genero' in cancion and cancion['genero'] == 'Rock':
            tabla.append([cancion['titulo'], cancion['artista']])
    if tabla:
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron canciones de este género.")
        
    screen.pausar_pantalla()

def cat_jazz():
    screen.limpiar_pantalla()
    musica_data = core.readDataFile(musica)

    print('Música Jazz:')
    tabla = []
    headers = ["Titulo", "Artista"]
    for cancion in musica_data.values():
        if 'genero' in cancion and cancion['genero'] == 'Jazz':
            tabla.append([cancion['titulo'], cancion['artista']])
    if tabla:
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron canciones de este género.")
        
    screen.pausar_pantalla()

def cat_clasica():
    screen.limpiar_pantalla()
    musica_data = core.readDataFile(musica)

    print('Música Clásica:')
    tabla = []
    headers = ["Titulo", "Artista"]
    for cancion in musica_data.values():
        if 'genero' in cancion and cancion['genero'] == 'Clasica':
            tabla.append([cancion['titulo'], cancion['artista']])
    if tabla:
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron canciones de este género.")
        
    screen.pausar_pantalla()