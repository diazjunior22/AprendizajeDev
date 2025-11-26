from PIL.TiffImagePlugin import IFDRational

from  GestorDeTareas import Categorias , GestorDeTareas , Tarea


gestor_tarea =  GestorDeTareas()


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



save_tarea = []



while True:
    try:
        print('--BIENVENIDO GESTOR DE TAREAS---:\n ---QUE DESEAS HACER:')
        opcion = int(input('1:MENU TAREAS  | 2: MENU CATEGORIA'))
        while True:
            if opcion == 1:
                print('--MENU DE  TAREA  TAREAS---')
                gestor_tarea.mostrar_tareas()
                print("-------------------------------------------------")
                opcion = int(input('1:CREAR TAREA | 2:Selecionar Tarea:   |3: VOLVER AL MENU ANTERIOR   '))
                if opcion == 1:
                    print("---------------------------------------------")
                    titulo = preguntar_tarea('Ingrese el titulo del tarea: ')
                    descripcion = preguntar_tarea('Ingrese la descripcion del tarea: ')
                    tarea = Tarea(titulo, descripcion)
                    gestor_tarea.guardar_tarea(tarea)
                    print('Tarea guardada exito.')
                if opcion == 2:
                    try:
                        opcion_tarea = preguntar_tarea('porfavor ingrese el nombre de la tarea:' )
                        is_tarea , tarea_encontrada = gestor_tarea.buscar_tarea(opcion_tarea)
                        if is_tarea:
                            while True:
                                print('_________________________________')
                                print(tarea_encontrada.mostrar_informacion())
                                edit_tarea =  int(input('1:Cambiar Estado 2:Editar Nombre  3:Editar Descripcion:  4:Volver al Menu Anterior '))
                                if edit_tarea == 1:
                                    new_estado = input(f'Porfavor Ingrese el nuevo estado de la tarea {tarea_encontrada.titulo}')
                                    tarea_encontrada.cambiar_estado(new_estado)
                                if edit_tarea == 2:
                                    new_name = input('Ingrese el nuevo nombre de la tarea')
                                    if new_name :
                                      tarea_encontrada.cambiar_titulo(new_name)
                                    else:
                                        print('error al cambiar el nombre')
                                if edit_tarea == 3:
                                    new_descripcion = input('Ingrese el descripcion de la tarea')
                                    if new_descripcion :
                                        tarea_encontrada.cambiar_descripcion(new_descripcion)
                                    else:
                                        print("Error al cambiar descripcion")
                                if opcion == 4:
                                    break
                                else:
                                    continue
                        else:
                            print('Tarea no encontrada.')
                    except ValueError:
                            pass
    except  ValueError:
            print('Valor no valido.')





