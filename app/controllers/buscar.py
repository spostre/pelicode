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

    for libro in libros_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]

        if (titulo in libro['titulo'].lower()):
            print('LIBRO:')

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    for pelicula in peliculas_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]

        if (titulo in pelicula['titulo'].lower()):
            print('PELICULA:')

            tabla.append([pelicula['titulo'], pelicula['director']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    for cancion in musica_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]

        if (titulo in cancion['titulo'].lower()):
            print('CANCION:')

            tabla.append([cancion['titulo'], cancion['artista']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    if (not found):
        print("No se encontraron resultados.")

    screen.pausar_pantalla()
    search_menu()

def search_autor():
    screen.limpiar_pantalla()
    autor = input("Ingrese el autor/director/artista a buscar: ").lower()
    
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    found = False

    for libro in libros_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]

        if (autor in libro['autor'].lower()):
            print('LIBRO:')

            tabla.append([libro['titulo'], libro['autor']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            

    for pelicula in peliculas_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]

        if (autor in pelicula['director'].lower()):
            print('PELICULA:')

            tabla.append([pelicula['titulo'], pelicula['director']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    for cancion in musica_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]

        if (autor in cancion['artista'].lower()):
            print('CANCION:')

            tabla.append([musica['titulo'], musica['artista']])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
            found = True
            


    if (not found):
        print("No se encontraron resultados.")

    screen.pausar_pantalla()
    search_menu()

def search_genero():
    screen.limpiar_pantalla()
    confirm = True
    
    while confirm == True:
        print("1. Fantasia")
        print("2. Ciencia")
        print("3. Romance")
        print("4. Misterio")
        print("5. Accion")
        print('6. Hardcore')
        print('7. Electronica')
        print('8. Rock')
        print('9. Jazz')
        print('10. Clasica')
        print('0. Regresar al Menú Principal')
        try:
            opcion = int(input("Ingrese el género a buscar: "))
            if opcion == 1:
                genero = "fantasia"
                confirm = False
            elif opcion == 2:
                genero = "ciencia"
                confirm = False
            elif opcion == 3:
                genero = "romance"    
                confirm = False
            elif opcion == 4:
                genero = "misterio"
                confirm = False
            elif opcion == 5:
                genero = "accion"
                confirm = False
            elif opcion == 6:
                genero = "hardcore"
                confirm = False
            elif opcion == 7:
                genero = "electronica"
                confirm = False
            elif opcion == 8:
                genero = "rock"
                confirm = False
            elif opcion == 9:
                genero = "jazz"
                confirm = False
            elif opcion == 10:
                genero = "clasica"
                confirm = False
            elif opcion == 0:
                main.main()
        except ValueError:
            print("Entrada no válida. Ingrese un número.")
            continue
    
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)

    for libro in libros_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]
        
        if genero in libro.get('genero', '').lower():
            print('LIBRO:')

            tabla.append([libro['titulo'], libro['autor'], "Libro"])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    for pelicula in peliculas_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]

        if genero in pelicula.get('genero', '').lower():
            print('PELICULA:')

            tabla.append([pelicula['titulo'], pelicula['director'], "Película"])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    for cancion in musica_data.values():
        tabla = []
        headers = ["Título", "Autor/Director/Artista"]
        
        if genero in cancion.get('genero', '').lower():
            print('CANCION:')

            tabla.append([cancion['titulo'], cancion['artista'], "Música"])
            print(tabulate(tabla, headers=headers, tablefmt="grid"))

    if tabla:
        print(f"Resultados para el género: {genero.capitalize()} ---")
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print(f"No se encontraron resultados para el género '{genero}'.")
        
    screen.pausar_pantalla()
    search_menu()