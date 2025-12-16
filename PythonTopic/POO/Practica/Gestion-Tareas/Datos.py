import time
import os
import pyttsx3
from  GestorDeTareas import Categorias , GestorDeTareas , Tarea




def hablador(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()





gestor_tarea =  GestorDeTareas()

tarea1 = Tarea("jugar" , 'pepe')

gestor_tarea.guardar_tarea(tarea1)

def preguntar_tarea(texto):
    texto =  texto.capitalize()
    while True:
        pregunta = input(texto).strip().lower()
        if pregunta:
            return pregunta


def pregunta_opciones(opcion):
    opcion = opcion.capitalize()
    while True:
        try:
            respuesta = int(input(opcion))
            if respuesta:
                return respuesta
        except ValueError:
            print("Opcion no valida")

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')


def detalle_tarea(tarea_encontrada):
    while True:
        print("___________ DETALLE DE LA TAREA _________________ ")
        print(tarea_encontrada.mostrar_informacion())
        edit_tarea = pregunta_opciones('1:CAMBIAR ESTADO 2: CAMBIAR EL TITULO 3 : CAMBIAR LA DESCRIPCION 4: VOLVER AL MENU ANTERIOR')
        if edit_tarea == 1:
            new_estado = input(f'Porfavor Ingrese el nuevo estado de la tarea {tarea_encontrada.titulo}')
            tarea_encontrada.cambiar_estado(new_estado)
        elif edit_tarea == 2:
            new_name = input('Ingrese el nuevo nombre de la tarea')
            if new_name:
                tarea_encontrada.cambiar_titulo(new_name)
                hablador('tarea haz sido cambiada')
                print('tarea haz sido cambiada')
            else:
                print('error al cambiar el nombre')
        elif edit_tarea == 3:
            new_descripcion = input('Ingrese el descripcion de la tarea')
            if new_descripcion:
                tarea_encontrada.cambiar_descripcion(new_descripcion)
            else:
                print("Error al cambiar descripcion")
        elif edit_tarea == 4:
            break

def menu_tarea():
    while True:
        print('-------------------------------------------')
        gestor_tarea.mostrar_tareas()
        opcion =  pregunta_opciones('1:CREAR UNA NUEVA TAREA  , 2:SELECIONAR TAREA 3:SALIR')
        if opcion == 1:
            titulo = preguntar_tarea('Ingrese el titulo de la tarea: ')
            descripcion =  preguntar_tarea('Ingrese el descripcion de la tarea: ')
            tarea = Tarea(titulo, descripcion)
            gestor_tarea.guardar_tarea(tarea)
            opcion = input('Desea Asiganarle una categoria: Si/No')
            if opcion.lower() == 'si':
                if gestor_tarea.categorias == []:
                    print('no hay categorias')
                    opcion_categoria = input(f'deseas crear una nueva categoria para la tarea {tarea.titulo} Si/No:  ')
                    if opcion_categoria.lower() == 'si':
                        menu_tarea(True)
                else:
                    

            print('Tarea Ha sido creada exitosamente')

        elif opcion == 2:
            titulo = preguntar_tarea('INGRESE EL NOMBRE DE LA TAREA: ')
            existe_tarea , tarea_encontrada = gestor_tarea.buscar_tarea(titulo)
            if existe_tarea:
                detalle_tarea(tarea_encontrada)
            else:
                print('Error al buscar la tarea')
        elif opcion == 3:
            break


def menu_categoria(crear=None):
    print("_________________________________")
    opcion = int(input('1:CREAR CATEGORIA  2:VER TODAS LAS CATEGORIAS:  3:'))
    if opcion == 1 or crear:
        nombre = input('Ingrese el nombre de la categoria: ')




def main():
    while True:
        print("Bienvenido al tu gestor de Tareas")
        opcion = pregunta_opciones('1 MENU DE TAREAS , 2 MENU DE CATEGORIAS: ')
        if opcion == 1:
            menu_tarea()
        elif opcion == 2:
            pass
        else:
            print("Error al menu de opciones")






main()











