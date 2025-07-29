import utils.screencontrol as screen
import controllers.añadir as add
import controllers.lista as list

def main():

    while True:
        opcion = menu()
        if (opcion == 1):
            add.add_menu()
        elif (opcion == 2):
            list.list_menu()
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            pass
        elif (opcion == 5):
            pass
        elif (opcion == 6):
            pass
        elif (opcion == 7):
            pass
        elif (opcion == 8):
            print("Saliendo del programa...")
            break

            
            

def menu():

    print('Administrador de Colección')

    print('1. Añadir un Nuevo Elemento')
    print('2. Ver Todos los Elementos')
    print('3. Buscar un Elemento')
    print('4. Editar un Elemento')
    print('5. Eliminar un Elemento')
    print('6. Ver Elementos por Categoría')
    print('7. Guardar y Cargar Colección')
    print('8. Salir')
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if 0 <= opcion <= 8:
                return opcion
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()