# 🚦 ¿Qué es el manejo de errores?
# Cuando Python encuentra un error, normalmente detiene la ejecución del programa.
# Con try/except puedes detectar el error, controlarlo y evitar que el programa se caiga.



divir =  10

try:
    divir =  10  / 0
    print("resultado")
except :
    print("hubo un error")
    
    


# 🎯 Capturar tipos específicos de errores (MUY IMPORTANTE)
# Nunca uses except: solo, porque atrapa errores inesperados. Mejor:

try:
    numero = int("hola")
except ValueError:
    print("No se pudo convertir a número")


# # Errores comunes para capturar:
# | Error               | Cuándo ocurre                       |
# | ------------------- | ----------------------------------- |
# | `ValueError`        | Conversión inválida (`int("hola")`) |
# | `ZeroDivisionError` | División entre cero                 |
# | `FileNotFoundError` | Archivo no existe                   |
# | `TypeError`         | Tipos incompatibles                 |
# | `KeyError`          | Clave no existe en un diccionario   |
# | `IndexError`        | Índice fuera de rango               |




# 🧨 Obtener el mensaje exacto del error

# Esto es profesional:

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error:", e)


# Salida:

# Error: division by zero




# # 🔁 Reintentar operación (patrón profesional)
# # Ejemplo útil para entrada de datos:

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print("Edad inválida. Intenta otra vez.")

print("Tu edad es:", edad)



# 🧠 Crear errores personalizados (raise)
# Permite lanzar errores manualmente.

def retirar(dinero):
    if dinero < 0:
        raise ValueError("No puedes retirar valores negativos")

retirar(-10)

# Salida:
# ValueError: No puedes retirar valores negativos

# 🛠 Manejo de errores con archivos
try:
    with open("archivo.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe")
