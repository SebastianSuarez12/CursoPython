# Herencia

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def registrado(self):
        print('Personaje registrado!!!')

class SuperHero(Personaje):
    def __init__(self, nombre, virtud= 'Bondadoso'):
        super().__init__(nombre)
        self.virtud = virtud

    def registrado(self):
        print('Superheroe registrado')

    def salvarMundo(self):
        print('Estoy salvando al mundo')
    
    def pelear(self):
        print('Peleando por la justicia')

class Villano(Personaje):
    def __init__(self, nombre, defecto= 'ambicioso'):
        super().__init__(nombre)
        self.defecto = defecto

    def pelear(self):
        print('Peleando por destruir el mundo')

personaje = Personaje('Personaje random')
personaje.registrado()
superheroe = SuperHero('SpiderMan', 'Honesto')
superheroe.registrado()
superheroe.salvarMundo()
villano = Villano('Guason')
villano.pelear()

