# ⚙️ Bloques else y finally
# Bloque	Cuándo se ejecuta
# else	Solo si NO hubo error
# finally	Siempre, haya error o no

try:
    n = int(input("Ingresa un número: "))
except ValueError:
    print("Error: Debes ingresar un número válido")
else:
    print("Número ingresado correctamente:", n)
finally:
    print("Fin del programa")
