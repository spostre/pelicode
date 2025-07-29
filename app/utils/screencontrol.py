import os

#Limpia la terminal para mas orden
def limpiar_pantalla():
    
    os.system('cls' if os.name == 'nt' else 'clear')

#Pausa la ejecución hasta que el usuario presione Enter.
def pausar_pantalla():
    
    input("Presione Enter para continuar...")