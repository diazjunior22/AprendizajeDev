# 🔹 3. Guardar Datos Como JSON

# JSON se usa para guardar datos tipo diccionarios/tablas.

# Ejemplo guardar usuarios en data.json:

import json

usuarios = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "Ana", "edad": 30}
]

with open("data.json", "w") as archivo:
    json.dump(usuarios, archivo, indent=4)


# El indent=4 lo hace bonito y legible.

# 🔹 4. Leer JSON

with open("data.json", "r") as archivo:
    datos = json.load(archivo)

print(datos)

# 🔹 5. Añadir un usuario al JSON

# # 1. Leer lo que ya existe
with open("data.json", "r") as archivo:
    usuarios = json.load(archivo)

# 2. Agregar nuevo usuario
nuevo_usuario = {"nombre": "Carlos", "edad": 28}
usuarios.append(nuevo_usuario)

# 3. Guardar de nuevo
with open("data.json", "w") as archivo:
    json.dump(usuarios, archivo, indent=4)