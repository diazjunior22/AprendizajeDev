# 🧹 1. Eliminar toda la lista
# Si quieres borrar completamente la lista (ya no existirá en memoria):

numeros = [1, 2, 3, 4]
del numeros  # elimina la lista completa


# 🪣 2. Vaciar una lista (sin eliminarla)
# Si quieres dejar la lista vacía, pero seguir usando la variable:
numeros = [1, 2, 3, 4]
numeros.clear()
print(numeros)  # []


# 🎯 3. Eliminar un elemento por posición (índice)
# Si sabes la posición del elemento:

numeros = [10, 20, 30, 40]
del numeros[2]
print(numeros)  # [10, 20, 40]



# 🧩 4. Eliminar un elemento por valor
# Si sabes el valor del elemento, no el índice:

frutas = ["manzana", "pera", "uva"]
frutas.remove("pera")
print(frutas)  # ["manzana", "uva"]


# 🪄 5. Eliminar y obtener el valor al mismo tiempo
# pop() elimina por índice y devuelve el valor eliminado:

colores = ["rojo", "verde", "azul"]
color_eliminado = colores.pop(1)
print(color_eliminado)  # "verde"
print(colores)  # ["rojo", "azul"]
# 👉 Si no le das índice, elimina el último elemento.




# 🔁 6. Eliminar varios elementos con comprensión o filtro
# Puedes crear una nueva lista sin los valores que quieras eliminar:

numeros = [1, 2, 3, 4, 5]
numeros = [n for n in numeros if n != 3]
print(numeros)  # [1, 2, 4, 5]