# 🔤 1. upper() — Todo en mayúsculas
texto = "hola"
print(texto.upper())  # "HOLA"


#🔤 2. lower() — Todo en minúsculas
texto = "HoLa"
print(texto.lower())  # "hola"

#🔤 3. capitalize() — Primera letra en mayúscula
texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"

#🔤 4. title() — Cada palabra con mayúscula inicial
texto = "hola mundo python"
print(texto.title())  # "Hola Mundo Python"

#🔤 5. strip() — Elimina espacios al inicio y final
texto = "  hola  "
print(texto.strip())  # "hola"


#También existen:

#🔤 6. replace() — Reemplazar texto
texto = "Python es difícil"
print(texto.replace("difícil", "fácil"))  # "Python es fácil"

#🔤 7. split() — Divide el texto en una lista
texto = "uno,dos,tres"
print(texto.split(","))  # ["uno", "dos", "tres"]

#🔤 8. join() — Une elementos de una lista
lista = ["Python", "es", "genial"]
print(" ".join(lista))  # "Python es genial"

#🔤 9. find() — Busca una palabra y devuelve la posición
texto = "aprendiendo python"
print(texto.find("python"))  # 12
#Si no existe, devuelve -1.


#🔤 10. startswith() y endswith() — Comprueba inicio o fin
print("hola mundo".startswith("hola"))  # True
print("hola mundo".endswith("mundo"))   # True

# 🔤 11. count() — Cuenta cuántas veces aparece algo
texto = "python python python"
print(texto.count("python"))  # 3

# 🔤 12. len() (NO es método, pero muy usado)
texto = "hola"
print(len(texto))  # 4





# | Método         | Acción                  |
# | -------------- | ----------------------- |
# | `upper()`      | Convertir a mayúsculas  |
# | `lower()`      | Convertir a minúsculas  |
# | `capitalize()` | Primera letra mayúscula |
# | `title()`      | Mayúscula cada palabra  |
# | `strip()`      | Quitar espacios         |
# | `replace()`    | Reemplazar texto        |
# | `split()`      | Convertir a lista       |
# | `join()`       | Unir lista en string    |
# | `find()`       | Buscar texto            |
# | `count()`      | Contar apariciones      |
# | `startswith()` | ¿Empieza con...?        |
# | `endswith()`   | ¿Termina con...?        |
# | `len()`        | Largo del string        |
