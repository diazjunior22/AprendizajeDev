# 3. Herencia (Inheritance)
# La herencia es el mecanismo que permite a una nueva clase (clase hija o subclase) heredar atributos y métodos de una clase existente (clase padre o superclase).
# Propósito: Reutilización de código. Permite crear una jerarquía "es un tipo de" (is-a relationship).
# Ejemplo: La clase Camioneta podría heredar de la clase Coche, reutilizando atributos como marca y métodos como arrancar(), pero agregando atributos propios como capacidad_carga.


class Coche():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"El coche {self.marca} {self.modelo} ha arrancado." 
    
    def detener(self):
        return f"El coche {self.marca} {self.modelo} se ha detenido."
    
    
class Camioneta(Coche):  #Camioneta hereda de Coche
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)  #Llamada al constructor de la clase padre
        self.capacidad_carga = capacidad_carga  #Atributo propio de Camioneta

    def cargar(self, peso):
        if peso <= self.capacidad_carga:
            return f"Cargando {peso} kg en la camioneta {self.marca} {self.modelo}."
        else:
            return f"No se puede cargar {peso} kg. Capacidad máxima es {self.capacidad_carga} kg." 
        
    
auto1 = Coche("Toyota", "Corolla")
print(auto1.arrancar())

camioneta1 = Camioneta("Ford", "F-150", 1000)
print(camioneta1.arrancar())  #Método heredado de Coche

camioneta1.cargar(800)  #Método propio de Camioneta
print(camioneta1.cargar(1200))  #Intento de sobrecarga