# Resolución ejercicio
from audioop import mul


class Multa:
    def __init__(self, nombreMulta, tipo):
        self.nombreMulta = nombreMulta
        self.tipo = tipo
        self.valor = 0

    def multar(self):

        if self.tipo == 'Leve':
            self.valor = 100
        elif self.tipo == 'Grave':
            self.valor == 300

class Registro:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.listaMultas = []

    def registrar(self, multa: Multa):
        self.listaMultas.append(multa)

    def setNombre(self, nuevoNombre: str):
        if nuevoNombre != self.nombre:
            self.nombre = nuevoNombre
        else:
            print('No se puede actualizar con el mismo nombre')

    def __str__(self) -> str:
        return f'El ciudadano: {self.nombre} con matricula {self.matricula} tiene las siguientes multas: {self.listaMultas}'

registroAndres = Registro('Andres', 'ABC-123')

print(registroAndres.__str__())

multa1 = Multa('Exceso Velocidad', 'Grave')
registroAndres.registrar(multa1)
print(registroAndres.__str__())

