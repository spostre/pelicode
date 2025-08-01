import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica
from tabulate import tabulate

def list_menu():

    screen.limpiar_pantalla()

    print("---Ver Todos los Elementos---")
    
    print("¿Qué categoría deseas ver?")
    print("1. Ver Todos los Libros")
    print("2. Ver Todas las Películas")
    print("3. Ver Toda la Música")
    print("4. Ver todos los Elementos")
    print("5. Regresar al Menú Principal")
  
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if (opcion == 1):
                list_libros()
            elif (opcion == 2):
                list_peliculas()
            elif (opcion == 3):
                list_musica()
            elif (opcion == 4):
                list_all()
            elif (opcion == 5):
                main.main()

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue

def list_libros():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    
    if (not libros_data):
        print("No hay libros almacenados.")
    else:
        print("Lista de Libros:")

        for libro in libros_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not libro.get('calificacion')):
                libro['calificacion'] = 'N/A'
                tabla.append([libro['titulo'], libro['autor'], libro['genero'], libro['calificacion']])
                print(tabulate(tabla, headers=headers, tablefmt="grid"))
                
            else:
                tabla.append([libro['titulo'], libro['autor'], libro['genero'], libro['calificacion']])
                print(tabulate(tabla, headers=headers, tablefmt="grid"))
    
    screen.pausar_pantalla()
    main.main()

def list_peliculas():
    screen.limpiar_pantalla()
    peliculas_data = core.readDataFile(peliculas)
    
    if (not peliculas_data):
        print("No hay películas almacenadas.")
    else:
        print("Lista de Películas:")

        for pelicula in peliculas_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not pelicula.get('calificacion')):
                pelicula['calificacion'] = 'N/A'
                tabla.append([pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['calificacion']])
                print(tabulate(tabla, headers=headers, tablefmt="grid"))
                
            else:
                tabla.append([pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['calificacion']])
                print(tabulate(tabla, headers=headers, tablefmt="grid"))


    screen.pausar_pantalla()
    main.main()

def list_musica():
    screen.limpiar_pantalla()
    musica_data = core.readDataFile(musica)
    print("Lista de Canciones:")

    for musicas in musica_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

        if (not musicas.get('calificacion')):
            musicas['calificacion'] = 'N/A'
            tabla.append([musicas['titulo'], musicas['artista'], musicas['genero'], musicas['calificacion']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            
        else:
            tabla.append([musicas['titulo'], musicas['artista'], musicas['genero'], musicas['calificacion']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

def list_all():

    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)   
    musica_data = core.readDataFile(musica)



    if (not libros_data):#Tabla sin libros

        print("No hay libros almacenados.")
        for pelicula in peliculas_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not pelicula.get('calificacion')):
                pelicula['calificacion'] = 'N/A'
                tabla.append([pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['calificacion'], 'Película'])
            else:
                tabla.append([pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['calificacion'], 'Película'])

        for cancion in musica_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not cancion.get('calificacion')):
                cancion['calificacion'] = 'N/A'
                tabla.append([cancion['titulo'], cancion['artista'], cancion['genero'], cancion['calificacion'], 'Música'])
            else:
                tabla.append([cancion['titulo'], cancion['artista'], cancion['genero'], cancion['calificacion'], 'Música'])

        print(tabulate(tabla, headers=headers, tablefmt="grid"))
            

    elif (not peliculas_data):#Tabla sin peliculas
        print("No hay peliculas almacenadas.")
        for libro in libros_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not libro.get('calificacion')):
                libro['calificacion'] = 'N/A'
                tabla.append([libro['titulo'], libro['autor'], libro['genero'], libro['calificacion'], 'Libro'])
            else:
                tabla.append([libro['titulo'], libro['autor'], libro['genero'], libro['calificacion'], 'Libro'])
        for cancion in musica_data.values():
            if (not cancion.get('calificacion')):
                cancion['calificacion'] = 'N/A'
                tabla.append([cancion['titulo'], cancion['artista'], cancion['genero'], cancion['calificacion'], 'Música'])
            else:
                tabla.append([cancion['titulo'], cancion['artista'], cancion['genero'], cancion['calificacion'], 'Música'])

        print(tabulate(tabla, headers=headers, tablefmt="grid"))

    elif (not musica_data):#Tabla sin musica
        print("No hay música almacenada.")
        for libro in libros_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not libro.get('calificacion')):
                libro['calificacion'] = 'N/A'
                tabla.append([libro['titulo'], libro['autor'], libro['genero'], libro['calificacion'], 'Libro'])
            else:
                tabla.append([libro['titulo'], libro['autor'], libro['genero'], libro['calificacion'], 'Libro'])

        for pelicula in peliculas_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not pelicula.get('calificacion')):
                pelicula['calificacion'] = 'N/A'
                tabla.append([pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['calificacion'], 'Película'])
            else:
                tabla.append([pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['calificacion'], 'Película'])

        print(tabulate(tabla, headers=headers, tablefmt="grid"))



    else: #Tabla completa
        for libro in libros_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not libro.get('calificacion')):
                libro['calificacion'] = 'N/A'
                tabla.append([libro['titulo'], libro['autor'], libro['genero'], libro['calificacion'], 'Libro'])
            else:
                tabla.append([libro['titulo'], libro['autor'], libro['genero'], libro['calificacion'], 'Libro'])

        for pelicula in peliculas_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not pelicula.get('calificacion')):
                pelicula['calificacion'] = 'N/A'
                tabla.append([pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['calificacion'], 'Película'])
            else:
                tabla.append([pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['calificacion'], 'Película'])
        
        for cancion in musica_data.values():
            tabla = []
            headers = ["Título", "Autor/Director/Artista", "Género", "Calificación", "Tipo"]

            if (not cancion.get('calificacion')):
                cancion['calificacion'] = 'N/A'
                tabla.append([cancion['titulo'], cancion['artista'], cancion['genero'], cancion['calificacion'], 'Música'])
            else:
                tabla.append([cancion['titulo'], cancion['artista'], cancion['genero'], cancion['calificacion'], 'Música'])

    print(tabulate(tabla, headers=headers, tablefmt="grid"))

    screen.pausar_pantalla()
    main.main()

