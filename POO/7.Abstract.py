from abc import ABC, abstractmethod

# Interfaces -> solo métodos yo no especifique la implementación de los métodos
# Métodos que aun no son implementados son conocidos como abstractos
# Para poder tener una interfaz necesariamente se necesita al menos un método abstracto
# Clases -> atributos y métodos


class Animal(ABC):
    @abstractmethod
    def darInformacion(self):
        pass

# Herencia -> Métodos


class Mamifero(Animal):
    def darInformacion(self):
        print('Me alimento de leche ')


class Reptil(Animal):
    def darInformacion(self):
        print('Soy de sangre fria')


mamifero = Mamifero()
mamifero.darInformacion()

reptil = Reptil()
reptil.darInformacion()
