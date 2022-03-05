# Clases con métodoss y atributos

class Personaje:
    # Atributos (caracteristicas)
    def __init__(self, nombre, tipo, edad):
        # Siempre se va a ejecutar
        # Es lo primero en ejecutarse
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
    
    # Métodos especiales get y set
    def getNombrePersonaje(self):
        return self.nombre
    
    def setNombrePersonaje(self,nuevoNombre : str):
        self.nombre = nuevoNombre

    # Metodos (acciones)
    def saludar(self):
        print(f'Hola, soy un personaje \n Mi nombre es {self.nombre} y soy un {self.tipo}')

personaje1 = Personaje('Batman','Héroe',35)
print(personaje1.edad)
print(personaje1.nombre)
print(personaje1.tipo)

personaje1.saludar()
print('Nombre antes del set',personaje1.getNombrePersonaje())
personaje1.setNombrePersonaje('Venom')
print('Nombre despues del set',personaje1.getNombrePersonaje())

