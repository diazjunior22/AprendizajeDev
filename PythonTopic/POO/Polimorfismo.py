# Qué es el polimorfismo

# Polimorfismo = "muchas formas"

# En POO significa que una misma función o método puede tener comportamientos diferentes, dependiendo de la clase que lo use.




class Animal():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass  #Método genérico, se implementará en las subclases
    
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hacer_sonido(self):
        return "Guau Guau"
    
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def hacer_sonido(self):
        return "Miau Miau"  
    



gato1 = Gato("Misu")
perro1 = Perro("Rex")

saludar = gato1.hacer_sonido()  #Llamada al método de Gato
perro1.hacer_sonido()  #Llamada al método de Perro

print(saludar)