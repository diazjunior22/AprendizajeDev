from datetime import datetime
import time

from pydantic_core.core_schema import none_schema


# Quick Suggestions
class GestorDeTareas:
    def __init__(self):
        self.tareas = []  # Lista para almacenar las tareas
        self.categorias = []  # Lista para almacenar las categorías

    def mostrar_categorias(self):
        if self.categorias == []:
            print("No hay categorías disponibles.")

        else:
            print("Categorías disponibles:")
            for categoria in self.categorias:
                print(f"- {categoria.nombre}")

    def buscar_categoria(self, categoria_name: str):
        for cat in self.categorias:
            if cat.nombre == categoria_name.lower():
                return True
            else:
                return False

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def mostrar_tareas_Categorias(self):
        for categoria in self.categorias:
            if categoria.tareas:
                for tarea in categoria.tareas:
                    print(f'Categoria: {categoria.nombre}')
                    print(tarea.mostrar_informacion())
                    print('___________________________________')

        else:
            print('Aun no hay alguna Tarea Gestrada a ninguna categoria  categoria ')

    def guardar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if self.tareas == []:
            print("No hay tareas guardadas.")
        else:
            print("______Tareas guardadas:_____")
            for tarea in self.tareas:
                print(tarea)

    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print(f"La tarea '{tarea}' no se encontró.")

    def buscar_tarea(self, tarea_name):
        for tarea in self.tareas:
            if tarea.titulo == tarea_name.lower():
                return True, tarea
        return None

class Tarea():
    def __init__(self,titulo, descripcion):
        self.titulo = titulo.lower()
        self.descripcion = descripcion.lower()
        self.descripcion = descripcion
        self.estado = "Pendiente"
        self.fecha_creacion = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def mostrar_estado(self):
        return f"La tarea '{self.titulo}' está {self.estado}."

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado de la tarea '{self.titulo}' ha sido cambiado a {self.estado}.")

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
        print(f"La descripción de la tarea '{self.titulo}' ha sido actualizada.")

    def cambiar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def mostrar_titulo(self):
        print(f'{self.titulo}')

    def mostrar_informacion(self):
        return f"Tarea: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}\nFecha de creación: {self.fecha_creacion}"



    def __str__(self):
        return f'{self.titulo} , {self.descripcion}'


class TareaPrioritaria(Tarea):
    def __init__(self, titulo, descripcion, prioridad):
        super().__init__(titulo, descripcion)
        self.prioridad = prioridad  # Nuevo atributo para la prioridad de la tarea

    def __str__(self):
        return f"Tarea Prioritaria: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}\nPrioridad: {self.prioridad}\nFecha de creación: {self.fecha_creacion}"


class Categorias:
    def __init__(self, nombre = None):
        self.nombre = nombre.lower()
        self.tareas = []

    def __str__(self):
        return f"Categorias: {self.nombre}"



    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        # print(f"Tarea '{tarea.titulo}' agregada a la categoría '{self.nombre}'.")

    def mostrar_tarea_por_categoria(self):
        print(f'Tareas de la Categoria: {self.nombre}')
        for t in self.tareas:
            print(t.mostrar_informacion())
            print("-------")


gestion = GestorDeTareas()

tarea = Tarea('cantar', 'I')
peliar = Tarea('Peliar', 'J')
cagar = Tarea('Cagar', 'J')

gestion.guardar_tarea(peliar)
gestion.guardar_tarea(cagar)

print(gestion.buscar_tarea('S'))
