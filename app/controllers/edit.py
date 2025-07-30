import utils.screencontrol as screen
import utils.corefiles as core
import main as main
from data.config import libros, peliculas, musica

def edit_menu():
    screen.limpiar_pantalla()

    print("Editar Elemento")
    print("1. Editar Libro")
    print("2. Editar Película")
    print("3. Editar Música")
    print("4. Volver al Menú Principal")

    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if (opcion == 1):
                edit_libro()
            elif (opcion == 2):
                edit_pelicula()
            elif (opcion == 3):
                edit_musica()
            elif (opcion == 4):
                main.main()
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def edit_libro():
    screen.limpiar_pantalla()
    libros_data = core.readDataFile(libros)
    global key_libro
    
    print('Que libro deseas editar?')
    for libro in libros_data.items():
        print(f"{libro[0]}")

    while True:
        try:
            key_libro = input("Seleccione el libro a editar: ").upper()

            if (key_libro in libros_data):
                screen.limpiar_pantalla()

                print(f"Libro seleccionado: {libros_data[key_libro]['titulo']} por {libros_data[key_libro]['autor']}")
                print("\n¿Qué aspecto del libro desea editar?")
                print("1. Título")
                print("2. Autor")
                print("3. Género")
                print("4. Calificación")
                print("5. Volver al Menú de Edición")

                while True:
                    try:
                        sub_opcion = int(input("Seleccione una opción: "))
                        if sub_opcion == 1:
                            edit_libro_titulo()
                        elif sub_opcion == 2:
                            edit_libro_autor()
                        elif sub_opcion == 3:
                            edit_libro_genero()
                        elif sub_opcion == 4:
                            edit_libro_calificacion()
                        elif sub_opcion == 5:
                            edit_menu()
                        else:
                            print("Opción no válida. Intente de nuevo.")
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número.")
            else:
                print("Codigo no valido. Intente de nuevo.")
                continue

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número o el título del libro.")

def edit_libro_titulo():
    screen.limpiar_pantalla()
    
    libros_data = core.readDataFile(libros)

    for libro in libros_data.values():
        
        nuevo_titulo = input("Ingrese el nuevo titulo del libro: ")
        libro['titulo'] = nuevo_titulo
        
        core.writeDataFile(libros, libros_data)
        
        print(f"¡Título del libro actualizado a '{nuevo_titulo}'!")
        break

    screen.pausar_pantalla()
    main.main()

    #POR TERMINAR /// Se edita siempre el primer libro sin importar el libro seleccionado