# 🔹 1. open() — Abrir Archivos
# open() siempre recibe al menos dos cosas:

# archivoc = open("archivo.txt", "modo")


# | Modo   | Significa       | Detalles                                |
# | ------ | --------------- | --------------------------------------- |
# | `"r"`  | Leer            | Error si el archivo no existe           |
# | `"w"`  | Escribir        | Crea archivo, borra contenido si existe |
# | `"a"`  | Agregar         | Escribe al final, no borra nada         |
# | `"r+"` | Leer y escribir | No borra contenido                      |
# | `"w+"` | Leer y escribir | Borra todo y escribe desde cero         |


archivo = open("hola.txt", "w")
archivo.write("Hola mundo")
archivo.close()





# 🔹 2. Leer Archivos
archivo = open("hola.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()


# ➡️ También puedes leer línea por línea:

with open("hola.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
        
# with se usa para que Python cierre el archivo automáticamente (es la forma profesional).


letras ='hola mundo este es el mejor regalo'
with open('prueba.txt' , 'w' ) as archivo:
    for letra in letras:
        archivo.write(letra)