from lib2to3.pytree import Base
import psycopg2

class BaseDatos:

    def __init__(self, baseDatos: str)-> None:
        self.cursor = None
        self.baseDatos = baseDatos
        self.conexion = None
        self.conectar()
      
    def conectar(self):
        try:
            print('Base: ',self.baseDatos)
            self.conexion = psycopg2.connect(host='localhost', 
                                            database=str(self.baseDatos),
                                            user='postgres', 
                                            password='root', 
                                            port=5432)
            print('La conexión se ha realizado')
            self.cursor = self.conexion.cursor()

        except:
            print('Error no se pudo conectar a esa instancia de la base de datos')

    def insertarUsuario(self,nombre, apellido, edad, sexo, correo, formacion):
        idU=nombre
        valores = (idU,nombre, apellido,edad, sexo, correo, formacion)
        sentenciaInsert = '''INSERT INTO public."Usiarios"(
            id, nombre, apellido, edad, sexo, correo, formacion)
	        VALUES (%s, %s, %s, %s, %s, %s, %s);
            '''
        self.cursor.execute(sentenciaInsert,valores)
        self.conexion.commit()

    def obtenerDatosUsuarios(self):
        self.cursor.execute('SELECT * FROM public."Usiarios";')
        datosUsuarios = self.cursor.fetchall();
        #for data in datosUsuarios:
            #print(data)
        return datosUsuarios