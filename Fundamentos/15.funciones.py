# Funciones -> def

# A (regla de correspondencia) -> B 
# a -> f -> b

# Procedimeinto  (funcion vacia)
def saludar():
    print('Hola!!')

    saludar()

edades = [18,5,20,22,17,14.5,2]

# Funciones
# 1. Recibir parametros
def esMayorEdad(edad: int):
    if edad >= 18:
        return True
    else:
        return False

for i in edades:
    print(esMayorEdad(i))

# 2. Recibir varios parametros 

def saludar2(nombre: str, apellido: str):
    print(f'Saludos {nombre} {apellido}')

saludar2('Andres','Suarez')

# 3. Parametros por defecto
def saludar3(nombre = 'Hector', apellido = 'Zambrano'):
    return f'Saludos {nombre} {apellido}'

print(saludar3())
print(saludar3('Andres'))
print(saludar3(apellido = 'Real'))
print(saludar3('Fernando', 'Real'))

# 4. Llamar a una función dentro de otra

def saludar4():
    print('Hola con todos')
    print(saludar3())

saludar4()

# Documentación

def calcularCubo(numero : int):
    '''
    Permite calcular el cudo de un numero
    numero: Número netero
    return: El cubo de la entrada
    '''
    return numero**3

print(calcularCubo(3))
print(calcularCubo.__doc__)

# Funcion args
# *args
# numero indefinido de valores
def listarAlumnos(*alumnos):
    print(f'Alumno: {alumnos}')

listarAlumnos('Anderson')
listarAlumnos('Anderson', 'Andrés', 'Bryan', 'Janeth', 'Jeremy')

def listarAlumnos2(*alumnos):
    for alumno in alumnos:
        print(f'Alumnos: {alumno}')

listarAlumnos2('Anderson')
listarAlumnos2('Anderson', 'Andrés', 'Bryan', 'Janeth', 'Jeremy')

# **kargs
# Numero indefinido de varibales de diferente tipo

def listaAlumnos3(**alumnos):
    print('La edad es: ', alumnos['edad'])


listaAlumnos3(nombre = 'Andres', apellido = 'Suarez', edad = 19)