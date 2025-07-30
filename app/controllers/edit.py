import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica

def edit_menu():
    
    screen.limpiar_pantalla()
                                                                                                
    print("Editar Elemento")
    print("1. Editar por Título")
    print("2. Editar por Autor/Director/Artista")
    print("3. Editar por Género")
    print('4. Editar por Calificación')
    print("5. Volver al Menú Principal")

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if (opcion == 1):
                edit_titulo()
            elif (opcion == 2):
                edit_autor()
            elif (opcion == 3):
                edit_genero()
            elif (opcion == 4):
                main.main()
                
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def edit_titulo():
    screen.limpiar_pantalla()
    
    libros_data = core.readDataFile(libros)
    peliculas_data = core.readDataFile(peliculas)
    musica_data = core.readDataFile(musica)
    
    encontrado = False
    titulo_a_buscar = input("Ingrese el título del elemento a editar: ").lower()

    for libro in libros_data.values():
        if (titulo_a_buscar in libro['titulo'].lower()):
            encontrado = True
            print(f"Libro encontrado: {libro['titulo']} por {libro['autor']}")
            nuevo_titulo = input("Ingrese el nuevo titulo del libro: ")
            libro['titulo'] = nuevo_titulo
            
            core.writeDataFile(libros, libros_data)
            
            print(f"¡Título del libro actualizado a '{nuevo_titulo}'!")
            break

    if (not encontrado):
        for pelicula in peliculas_data.values():
            if titulo_a_buscar in pelicula['titulo'].lower():
                encontrado = True
                print(f"Pelicula encontrada: {pelicula['titulo']} dirigida por {pelicula['director']}")
                nuevo_titulo = input("Ingrese el nuevo titulo de la película: ")
                pelicula['titulo'] = nuevo_titulo
                core.writeDataFile(peliculas, peliculas_data)
                print(f"¡Título de la película actualizado a '{nuevo_titulo}'!")
                break

    if (not encontrado):
        for cancion in musica_data.values():
            if (titulo_a_buscar in cancion['titulo'].lower()):
                encontrado = True
                print(f"Canción encontrada: {cancion['titulo']} por {cancion['artista']}")
                nuevo_titulo = input("Ingrese el nuevo titulo de la canción: ")
                cancion['titulo'] = nuevo_titulo
                core.writeDataFile(musica, musica_data)
                print(f"¡Título de la canción actualizado a '{nuevo_titulo}'!")
                break

    if (not encontrado):
        print("No se encontró ningún elemento con ese título.")
    
    screen.pausar_pantalla()
    main.main()