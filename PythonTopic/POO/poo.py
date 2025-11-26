class Persona():
    estado = "Activo"  #Atributo de clase
    
    #Constructor init 
    def __init__(self, nombre, edad):
        #Atributos de la instancia
        self.nombre = nombre
        self.edad = edad    
        self.__dni = 0  #Atributo privado - encapsulamiento
        
        #methods get y set para el atributo privado escapulado
    def get_dni(self):
        return self.__dni
        
    def set_dni(self, nuevo_dni):
        self.__dni = nuevo_dni
        
    #Método de instancia
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    
    
    

#Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30) #objeto persona1
print(persona1.saludar())  #Llamada al método de instancia

#Acceder al atributo de clase
print(f"Estado de la persona: {Persona.estado}")

#Acceder al atributo privado mediante el método get
print(f"DNI de la persona: {persona1.get_dni()}")
#Modificar el atributo privado mediante el método set
persona1.set_dni('87654321B')
print(f"DNI modificado de la persona: {persona1.get_dni()}")