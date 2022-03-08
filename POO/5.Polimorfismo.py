# Polimorfismo 
# Adecuar los comportamientos en cada una de las clases
from Personaje import Personaje, nombreArchivo
    
class SuperHeroe(Personaje):
    def __init__(self, nombre, virtud= 'Bueno'):
        super().__init__(nombre)
        self.virtud = virtud
    
    def saludar(self):
        print('Salvando al mundo')

class Villano(Personaje):
    def __init__(self, nombre, defecto= 'Codicioso'):
        super().__init__(nombre)
        self.defecto = defecto
    
    def saluda(self):
        print('Acabando con el mundo')

print(nombreArchivo())

personaje = Personaje(nombre= 'Personaje 1')
personaje.saludar()

superheroe = SuperHeroe('Spider')
villano = Villano('Guason')

superheroe.saludar()
villano.saluda()